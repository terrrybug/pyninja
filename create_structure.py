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
    # Essential files
    files = {
        "pyninja/__init__.py": '''"""PyNinja - The Ultimate Python Dependency Ninja"""
    except Exception as e:
        print(f"💥 PyNinja error: {e}")

if __name__ == "__main__":
    main()
''',
        
        "pyninja/core/__init__.py": "",
        "pyninja/analyzers/__init__.py": "",
        
        "pyninja/cli.py": '''"""PyNinja CLI interface"""
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
        "pyninja/core/__init__.py": "",
        "pyninja/analyzers/__init__.py": "",
        "CHANGELOG.md": '''# Changelog
- 🧠 Intelligent compatibility scoring
- 🌍 Community health metrics

### Security
- Real-time vulnerability detection
- Automated security patch suggestions
develop-eggs/
dist/
lib/
        ".gitignore": '''# Python
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
        "tests/__init__.py": "",
        "tests/test_pyninja.py": '''"""Basic tests for PyNinja"""
    
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

    }
    for file_path, content in files.items():
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"✓ Created {file_path}")
    print("\n🎉 PyNinja package structure created successfully!")

if __name__ == "__main__":
    create_pyninja_structure()
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
