#!/usr/bin/env python3
"""
Core updater module for PyNinja - Enhanced version with better error handling
"""

import sys
import os
import asyncio
import logging
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
import json
from datetime import datetime
import traceback

# Rich imports for enhanced CLI
try:
    from rich.console import Console
    from rich.logging import RichHandler
    from rich.traceback import install
    install(show_locals=True)
except ImportError:
    Console = None
    RichHandler = None

# Initialize console
console = Console() if Console else None

class PyNinjaError(Exception):
    """Base exception for PyNinja errors"""
    pass

class SecurityError(PyNinjaError):
    """Security-related errors"""
    pass

class DependencyError(PyNinjaError):
    """Dependency-related errors"""
    pass

class ConfigurationError(PyNinjaError):
    """Configuration-related errors"""
    pass

@dataclass
class UpdateResult:
    """Result of an update operation"""
    success: bool
    package_name: str
    old_version: str
    new_version: str
    error_message: Optional[str] = None
    security_fixes: List[str] = None
    
    def __post_init__(self):
        if self.security_fixes is None:
            self.security_fixes = []

class EnhancedLogger:
    """Enhanced logging with context and structured output"""
    
    def __init__(self, name: str = "pyninja", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Clear existing handlers
        self.logger.handlers.clear()
        
        # Add rich handler if available, otherwise use standard
        if RichHandler:
            handler = RichHandler(
                console=console,
                show_time=True,
                show_path=True,
                rich_tracebacks=True
            )
        else:
            handler = logging.StreamHandler()
            
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        # File handler for persistent logging
        log_file = Path("pyninja.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
    
    def info(self, message: str, **kwargs):
        self.logger.info(message, extra=kwargs)
    
    def warning(self, message: str, **kwargs):
        self.logger.warning(message, extra=kwargs)
    
    def error(self, message: str, **kwargs):
        self.logger.error(message, extra=kwargs)
    
    def debug(self, message: str, **kwargs):
        self.logger.debug(message, extra=kwargs)
    
    def critical(self, message: str, **kwargs):
        self.logger.critical(message, extra=kwargs)

class EnhancedUpdater:
    """Enhanced core updater with improved error handling and features"""
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.logger = EnhancedLogger("updater")
        
        # Results tracking
        self.update_results: List[UpdateResult] = []
        self.security_issues: List[Dict] = []
        self.modernization_suggestions: List[Dict] = []
    
    async def update_package(self, package_name: str, target_version: Optional[str] = None) -> UpdateResult:
        """Update a single package with comprehensive error handling"""
        try:
            self.logger.info(f"Starting update for {package_name}")
            
            # Get current version
            current_version = await self._get_current_version(package_name)
            
            # Get package info
            package_info = await self._fetch_package_info(package_name)
            
            # Determine target version
            if not target_version:
                target_version = await self._get_latest_stable_version(package_info)
            
            # Perform the update
            success = await self._perform_update(package_name, target_version)
            
            result = UpdateResult(
                success=success,
                package_name=package_name,
                old_version=current_version or "unknown",
                new_version=target_version
            )
            
            self.update_results.append(result)
            self.logger.info(f"Update completed for {package_name}: {current_version} -> {target_version}")
            
            return result
            
        except Exception as e:
            error_msg = f"Failed to update {package_name}: {str(e)}"
            self.logger.error(error_msg)
            
            result = UpdateResult(
                success=False,
                package_name=package_name,
                old_version="unknown",
                new_version="unknown",
                error_message=error_msg
            )
            
            self.update_results.append(result)
            return result
    
    async def _get_current_version(self, package_name: str) -> Optional[str]:
        """Get currently installed version"""
        try:
            import subprocess
            result = subprocess.run([
                sys.executable, "-m", "pip", "show", package_name
            ], capture_output=True, text=True, check=True)
            
            for line in result.stdout.split('\n'):
                if line.startswith('Version:'):
                    return line.split(':', 1)[1].strip()
        except subprocess.CalledProcessError:
            pass
        return None
    
    async def _fetch_package_info(self, package_name: str) -> Dict:
        """Fetch package information from PyPI"""
        import aiohttp
        
        async with aiohttp.ClientSession() as session:
            url = f"https://pypi.org/pypi/{package_name}/json"
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise DependencyError(f"Package {package_name} not found on PyPI")
    
    async def _get_latest_stable_version(self, package_info: Dict) -> str:
        """Get latest stable version from package info"""
        try:
            from packaging.version import parse as parse_version
            
            releases = package_info.get("releases", {})
            stable_versions = []
            
            for version in releases.keys():
                try:
                    parsed = parse_version(version)
                    if not parsed.is_prerelease:
                        stable_versions.append(parsed)
                except Exception:
                    continue
            
            if stable_versions:
                return str(max(stable_versions))
            else:
                return package_info.get("info", {}).get("version", "unknown")
                
        except Exception as e:
            self.logger.warning(f"Error determining latest version: {e}")
            return package_info.get("info", {}).get("version", "unknown")
    
    async def _perform_update(self, package_name: str, version: str) -> bool:
        """Perform the actual package update"""
        try:
            import subprocess
            
            # Construct pip command
            cmd = [sys.executable, "-m", "pip", "install", f"{package_name}=={version}"]
            
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            self.logger.debug(f"Pip output: {result.stdout}")
            return True
            
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Pip install failed: {e.stderr}")
            return False
    
    def generate_report(self) -> Dict:
        """Generate comprehensive update report"""
        successful_updates = [r for r in self.update_results if r.success]
        failed_updates = [r for r in self.update_results if not r.success]
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_packages": len(self.update_results),
                "successful_updates": len(successful_updates),
                "failed_updates": len(failed_updates),
                "security_issues_found": len(self.security_issues),
                "modernization_opportunities": len(self.modernization_suggestions)
            },
            "successful_updates": [
                {
                    "package": r.package_name,
                    "old_version": r.old_version,
                    "new_version": r.new_version
                } for r in successful_updates
            ],
            "failed_updates": [
                {
                    "package": r.package_name,
                    "error": r.error_message
                } for r in failed_updates
            ],
            "security_issues": self.security_issues,
            "modernization_suggestions": self.modernization_suggestions,
            "config": self.config
        }
        
        return report
    
    def display_report(self, report: Dict):
        """Display formatted report"""
        if console:
            from rich.table import Table
            from rich.panel import Panel
            
            # Summary panel
            summary = report["summary"]
            console.print(Panel.fit(f"""
[bold green]PyNinja Update Report[/bold green]

Package Updates: {summary['total_packages']}
Successful: {summary['successful_updates']}
Failed: {summary['failed_updates']}
Security Issues: {summary['security_issues_found']}
Modernization Opportunities: {summary['modernization_opportunities']}
            """.strip()))
        
        else:
            # Fallback to simple print
            print(f"PyNinja Update Report - {report['timestamp']}")
            print(f"Total: {report['summary']['total_packages']}, "
                  f"Success: {report['summary']['successful_updates']}, "
                  f"Failed: {report['summary']['failed_updates']}")

# Security and modernization classes (simplified for now)
class SecurityScanner:
    """Security vulnerability scanner"""
    
    def __init__(self):
        self.logger = EnhancedLogger("security")
    
    async def scan_package(self, package_name: str, version: str) -> List[Dict]:
        """Scan package for vulnerabilities"""
        return []

class ModernizationEngine:
    """Engine for suggesting modern alternatives"""
    
    MODERNIZATION_MAP = {
        'mysql-python': {'replacement': 'PyMySQL', 'reason': 'Python 3 compatible'},
        'pycrypto': {'replacement': 'pycryptodome', 'reason': 'Security fixes'},
        'PIL': {'replacement': 'Pillow', 'reason': 'Modern imaging library'},
    }
    
    def __init__(self):
        self.logger = EnhancedLogger("modernization")
    
    def get_modernization_suggestions(self, package_name: str) -> List[Dict]:
        """Get modernization suggestions"""
        suggestions = []
        normalized_name = package_name.lower().replace('_', '-')
        if normalized_name in self.MODERNIZATION_MAP:
            suggestion = self.MODERNIZATION_MAP[normalized_name].copy()
            suggestion['package'] = package_name
            suggestions.append(suggestion)
        return suggestions

# Export main classes
__all__ = [
    'EnhancedUpdater', 'UpdateResult', 'PyNinjaError',
    'SecurityError', 'DependencyError', 'ConfigurationError',
    'EnhancedLogger', 'SecurityScanner', 'ModernizationEngine'
]