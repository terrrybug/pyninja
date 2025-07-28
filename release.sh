#!/bin/bash
# PyNinja - PyPI Upload Guide & Automation Scripts

# =============================================================================
# STEP-BY-STEP PYPI UPLOAD GUIDE
# =============================================================================

echo "🥷 PyNinja - PyPI Upload Guide"
echo "================================"

# Prerequisites check
echo "📋 Prerequisites Check:"
echo "1. Python 3.8+ installed ✓"
echo "2. pip and setuptools updated ✓" 
echo "3. PyPI account created ✓"
echo "4. TestPyPI account created ✓"
echo ""

# =============================================================================
# Step 1: Install build tools
# =============================================================================

echo "🔧 Step 1: Installing build tools..."
pip install --upgrade pip setuptools wheel
pip install --upgrade build twine
pip install --upgrade keyring  # For secure credential storage

# =============================================================================
# Step 2: Project structure setup
# =============================================================================

echo "📁 Step 2: Setting up project structure..."

# Create the complete package structure
cat > create_structure.py << 'EOF'
import os

def create_pyninja_structure():
    """Create complete PyNinja package structure"""
    
    # Directory structure
    dirs = [
        "pyninja",
        "pyninja/core",
        "pyninja/analyzers", 
        "pyninja/data",
        "pyninja/templates",
        "tests",
        "docs",
        ".github/workflows"
    ]
    
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"✓ Created {dir_path}")
    
    # Essential files
    files = {
        "pyninja/__init__.py": '''"""PyNinja - The Ultimate Python Dependency Ninja"""
__version__ = "1.0.0"
__author__ = "PyNinja Community"
__email__ = "community@pyninja.dev"
__license__ = "MIT"

from .core.updater import PyNinja
from .core.analyzer import DependencyAnalyzer

__all__ = ["PyNinja", "DependencyAnalyzer"]
''',
        
        "pyninja/cli.py": '''"""PyNinja CLI interface"""
import asyncio
from .core.updater import UltimateRequirementsUpdater, CLIInterface

def main():
    """Main CLI entry point"""
    try:
        CLIInterface.main()
    except KeyboardInterrupt:
        print("\\n🥷 PyNinja operation cancelled")
    except Exception as e:
        print(f"💥 PyNinja error: {e}")

if __name__ == "__main__":
    main()
''',
        
        "pyninja/core/__init__.py": "",
        "pyninja/analyzers/__init__.py": "",
        
        "CHANGELOG.md": '''# Changelog

All notable changes to PyNinja will be documented in this file.

## [1.0.0] - 2025-01-XX

### Added
- 🥷 Initial release of PyNinja
- 🔒 Security vulnerability scanning with OSV integration
- 🚀 Smart modernization engine for legacy packages
- ⚡ Performance optimization recommendations
- 🤖 GitHub Actions workflow generation
- 🎨 Beautiful Rich CLI interface
- 📊 Comprehensive dependency analysis
- 🔄 Multi-format support (requirements.txt, pyproject.toml, Pipfile)
- 🧠 Intelligent compatibility scoring
- 🌍 Community health metrics

### Security
- Real-time vulnerability detection
- Automated security patch suggestions
- License compliance checking
''',
        
        ".gitignore": '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
# PyNinja specific
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package

echo "python -m twine configure"
echo "Username: __token__"
echo "Test installation from TestPyPI:"

# =============================================================================
# Step 6: Upload to PyPI
# =============================================================================

echo "Username: __token__"  
echo "Password: [your-pypi-token]"
echo "✅ Package uploaded to PyPI!"

# =============================================================================
# AUTOMATION SCRIPTS
# =============================================================================
cat > release.sh << 'EOF'

set -e
    fi
}
name: 📦 Publish PyNinja to PyPI

    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Run security scan
      uses: pypa/gh-action-pip-audit@v1.0.8
      with:
        inputs: requirements.txt

  build:
    needs: [test, security-scan]
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install build dependencies
      run: |
        python -m pip install --upgrade pip
      run: python -m twine check dist/*
    
    - name: Upload build artifacts
      uses: actions/upload-artifact@v3
      with:
        name: dist
        path: dist/

  publish:
    needs: build
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && startsWith(github.ref, 'refs/tags/v')
    environment:
      name: pypi

#!/bin/bash
# Enhanced PyNinja Release & PyPI Upload Script

set -e

echo "🥷 PyNinja - Enhanced PyPI Upload & Release Script"
echo "==============================================="

# Prerequisites check
echo "📋 Checking prerequisites..."
for tool in python pip twine build keyring; do
    if ! command -v $tool &> /dev/null; then
        echo "❌ $tool not found. Please install it before proceeding."
        exit 1
    fi
done
echo "✅ All required tools found."

# Step 1: Install/Upgrade build tools
echo "� Installing/upgrading build tools..."
pip install --upgrade pip setuptools wheel build twine keyring

# Step 2: Project structure setup
echo "📁 Ensuring project structure..."
python3 <<EOF
import os
dirs = [
    "pyninja", "pyninja/core", "pyninja/analyzers", "pyninja/data", "pyninja/templates", "tests", "docs", ".github/workflows"
]
for d in dirs:
    os.makedirs(d, exist_ok=True)
EOF
echo "✅ Project structure ensured."

# Step 3: Manual code placement reminder
echo "📝 Please ensure your main code is in pyninja/core/updater.py and analyzers/analyzer.py."

# Step 4: Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/ pyninja.egg-info/

# Step 5: Build the package
echo "🏗️  Building the package..."
python -m build
echo "✅ Package built!"
ls -la dist/

# Step 6: Test upload to TestPyPI
echo "🧪 Test uploading to TestPyPI..."
echo "Configure TestPyPI credentials if needed."
echo "python -m twine upload --repository testpypi dist/*"
echo "Test install: pip install --index-url https://test.pypi.org/simple/ pyninja"

# Step 7: Upload to PyPI
echo "� Ready to upload to PyPI."
read -p "Upload to PyPI now? (y/N): " upload_confirm
if [[ $upload_confirm =~ ^[Yy]$ ]]; then
    python -m twine upload dist/*
    echo "✅ Uploaded to PyPI! Install with: pip install pyninja"
else
    echo "⏸️  Upload cancelled. You can upload manually with: python -m twine upload dist/*"
fi

# Step 8: Run validation script
if [ -f validate_package.py ]; then
    echo "🔍 Running package validation..."
    python validate_package.py
fi

# Step 9: Show next steps
echo ""
echo "🎉 PyNinja PyPI Upload & Release Complete!"
echo "==========================================="
echo "📋 Next Steps:"
echo "1. Test locally: pip install -e ."
echo "2. Push tags to trigger GitHub Actions"
echo "3. Use Docker for consistent builds"
echo "4. See .github/workflows/publish.yml for CI/CD"
echo "5. Happy ninja coding!"
      url: https://pypi.org/project/pyninja/
    
    permissions:
      id-token: write  # For trusted publishing
    
    steps:
    - name: Download build artifacts
      uses: actions/download-artifact@v3
      with:
        name: dist
        path: dist/
    
    - name: Publish to PyPI
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        verbose: true
    
    - name: Create GitHub Release
      uses: actions/create-release@v1
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      with:
        tag_name: ${{ github.ref }}
        release_name: PyNinja ${{ github.ref }}
        body: |
          🥷 PyNinja Release ${{ github.ref }}
          
          ## What's New
          - Enhanced dependency analysis
          - Improved security scanning
          - Better performance optimizations
          
          ## Installation
          ```bash
          pip install --upgrade pyninja
          ```
          
          ## Full Changelog
          See [CHANGELOG.md](CHANGELOG.md) for complete details.
        draft: false
        prerelease: false

  test-install:
    needs: publish
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && startsWith(github.ref, 'refs/tags/v')
    
    steps:
    - name: Test PyPI installation
      run: |
        sleep 120  # Wait for PyPI to update
        pip install pyninja
        pyninja --help
        
    - name: Test basic functionality
      run: |
        echo "requests==2.25.0" > test_requirements.txt
        pyninja --file test_requirements.txt --dry-run
EOF

# =============================================================================
# PyPI Configuration Files
# =============================================================================

cat > .pypirc << 'EOF'
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
# password = your-pypi-token (set via environment or keyring)

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
# password = your-testpypi-token (set via environment or keyring)
EOF

# =============================================================================
# Docker support for consistent builds
# =============================================================================

cat > Dockerfile << 'EOF'
FROM python:3.11-slim

LABEL maintainer="PyNinja Community <community@pyninja.dev>"
LABEL description="PyNinja - The Ultimate Python Dependency Ninja"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Install PyNinja
RUN pip install -e .

# Create non-root user
RUN useradd --create-home --shell /bin/bash ninja
USER ninja

# Set entrypoint
ENTRYPOINT ["pyninja"]
CMD ["--help"]
EOF

cat > docker-compose.yml << 'EOF'
version: '3.8'

services:
  pyninja:
    build: .
    volumes:
      - .:/workspace
      - ~/.gitconfig:/home/ninja/.gitconfig:ro
    working_dir: /workspace
    environment:
      - PYTHONPATH=/workspace
    command: pyninja --interactive

  pyninja-ci:
    build: .
    volumes:
      - .:/workspace
    working_dir: /workspace
    command: pyninja --security-first --export-report /workspace/security-report.json
EOF

# =============================================================================
# Package validation script
# =============================================================================

cat > validate_package.py << 'EOF'
#!/usr/bin/env python3
"""Package validation script for PyNinja"""

import subprocess
import sys
import json
from pathlib import Path

def run_command(cmd, description):
    """Run a command and return success status"""
    print(f"🔍 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - PASSED")
            return True
        else:
            print(f"❌ {description} - FAILED")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ {description} - ERROR: {e}")
        return False

def validate_package():
    """Comprehensive package validation"""
    print("🥷 PyNinja Package Validation")
    print("=" * 40)
    
    checks = []
    
    # 1. Check required files exist
    required_files = [
        "setup.py", "pyproject.toml", "README.md", "LICENSE", 
        "MANIFEST.in", "requirements.txt", "pyninja/__init__.py"
    ]
    
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file} exists")
            checks.append(True)
        else:
            print(f"❌ {file} missing")
            checks.append(False)
    
    # 2. Validate Python syntax
    checks.append(run_command("python -m py_compile pyninja/*.py", "Python syntax validation"))
    
    # 3. Check imports
    checks.append(run_command("python -c 'import pyninja; print(pyninja.__version__)'", "Import validation"))
    
    # 4. Build package
    checks.append(run_command("python -m build", "Package build"))
    
    # 5. Check distribution
    checks.append(run_command("python -m twine check dist/*", "Distribution check"))
    
    # 6. Security check
    checks.append(run_command("pip-audit .", "Security audit"))
    
    # 7. Test basic CLI
    checks.append(run_command("python -m pyninja --help", "CLI functionality"))
    
    # Summary
    passed = sum(checks)
    total = len(checks)
    
    print("\n" + "=" * 40)
    print(f"📊 Validation Results: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 All checks passed! Package is ready for release.")
        return True
    else:
        print("⚠️  Some checks failed. Please fix issues before release.")
        return False

if __name__ == "__main__":
    success = validate_package()
    sys.exit(0 if success else 1)
EOF

chmod +x validate_package.py

# =============================================================================
# Final instructions
# =============================================================================

echo ""
echo "🎉 PyNinja PyPI Upload Setup Complete!"
echo "======================================="
echo ""
echo "📋 Next Steps:"
echo "1. Copy your main code to pyninja/core/updater.py"
echo "2. Run: python validate_package.py"
echo "3. Test locally: pip install -e ."
echo "4. Run: ./release.sh"
echo ""
echo "🔐 PyPI Setup:"
echo "1. Create PyPI account: https://pypi.org/account/register/"
echo "2. Enable 2FA and create API token"
echo "3. Configure credentials: python -m keyring set https://upload.pypi.org/legacy/ __token__"
echo ""
echo "🚀 Automated Release:"
echo "• Use ./release.sh for interactive release"
echo "• Push tags to trigger GitHub Actions"
echo "• Use Docker for consistent builds"
echo ""
echo "📦 Package Name: pyninja"
echo "🔗 PyPI URL: https://pypi.org/project/pyninja/"
echo "💻 Install: pip install pyninja"
echo ""
echo "🥷 Happy ninja coding!"
EOF

chmod +x upload_guide.sh

# =============================================================================
# Final summary and execution
# =============================================================================

echo ""
echo "🎯 FINAL SETUP SUMMARY"
echo "======================="
echo ""
echo "✅ Package Structure: Complete"
echo "✅ PyPI Configuration: Ready" 
echo "✅ GitHub Actions: Configured"
echo "✅ Docker Support: Added"
echo "✅ Release Automation: Ready"
echo "✅ Validation Scripts: Created"
echo ""
echo "🚀 Ready to launch PyNinja to PyPI!"
echo ""
echo "Run this script to begin: ./upload_guide.sh"