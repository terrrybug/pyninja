# PyNinja 🥷 - The Ultimate Python Dependency Ninja
# Complete PyPI package setup files

# =============================================================================
# setup.py - Package configuration
# =============================================================================

from setuptools import setup, find_packages
import os

# Read README for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="pyninja-tool",
    version="1.0.1",
    author="PyNinja Community",
    author_email="community@pyninja.dev",
    description="🥷 The ultimate Python dependency ninja - automate, secure, and modernize your requirements",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/pyninja-dev/pyninja",
    project_urls={
        "Bug Tracker": "https://github.com/pyninja-dev/pyninja/issues",
        "Documentation": "https://pyninja.dev/docs",
        "Source Code": "https://github.com/pyninja-dev/pyninja",
        "Changelog": "https://github.com/pyninja-dev/pyninja/releases",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Software Distribution",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Typing :: Typed",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=22.0.0",
            "isort>=5.10.0",
            "mypy>=1.0.0",
            "flake8>=4.0.0",
            "pre-commit>=2.17.0",
        ],
        "viz": [
            "graphviz>=0.20.0",
            "matplotlib>=3.5.0",
        ],
        "github": [
            "PyGithub>=1.55.0",
            "pygit2>=1.10.0",
        ],
        "all": [
            "graphviz>=0.20.0",
            "matplotlib>=3.5.0",
            "PyGithub>=1.55.0",
            "pygit2>=1.10.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "pyninja=pyninja.cli:main",
            "py-ninja=pyninja.cli:main",
            "ninja-deps=pyninja.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "pyninja": [
            "data/*.json",
            "templates/*.yml",
            "templates/*.md",
        ],
    },
    keywords=[
        "dependencies", "requirements", "security", "vulnerability", "modernization",
        "automation", "python", "pip", "pypi", "devops", "ci-cd", "ninja"
    ],
    zip_safe=False,
)

# =============================================================================
# pyproject.toml - Modern Python packaging
# =============================================================================

PYPROJECT_TOML = '''[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pyninja"
version = "1.0.0"
description = "🥷 The ultimate Python dependency ninja - automate, secure, and modernize your requirements"
readme = "README.md"
license = {file = "LICENSE"}
authors = [
    {name = "PyNinja Community", email = "community@pyninja.dev"},
]
maintainers = [
    {name = "PyNinja Community", email = "community@pyninja.dev"},
]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
keywords = ["dependencies", "requirements", "security", "ninja", "automation"]
requires-python = ">=3.8"
dependencies = [
    "packaging>=21.0",
    "toml>=0.10.0",
    "requests>=2.25.0",
    "click>=8.0.0",
    "rich>=12.0.0",
    "aiohttp>=3.8.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "black>=22.0.0",
    "isort>=5.10.0",
    "mypy>=1.0.0",
]
viz = ["graphviz>=0.20.0", "matplotlib>=3.5.0"]
github = ["PyGithub>=1.55.0", "pygit2>=1.10.0"]
all = ["graphviz>=0.20.0", "matplotlib>=3.5.0", "PyGithub>=1.55.0", "pygit2>=1.10.0"]

[project.urls]
Homepage = "https://pyninja.dev"
Documentation = "https://pyninja.dev/docs"
Repository = "https://github.com/pyninja-dev/pyninja"
"Bug Tracker" = "https://github.com/pyninja-dev/pyninja/issues"
Changelog = "https://github.com/pyninja-dev/pyninja/releases"

[project.scripts]
pyninja = "pyninja.cli:main"
py-ninja = "pyninja.cli:main"
ninja-deps = "pyninja.cli:main"

[tool.setuptools.packages.find]
where = ["."]
include = ["pyninja*"]

[tool.setuptools.package-data]
pyninja = ["data/*.json", "templates/*.yml", "templates/*.md"]

[tool.black]
line-length = 88
target-version = ['py38']
include = '\\.pyi?$'

[tool.isort]
profile = "black"
multi_line_output = 3

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
'''

# =============================================================================
# requirements.txt - Core dependencies
# =============================================================================

REQUIREMENTS_TXT = '''packaging>=21.0
toml>=0.10.0
requests>=2.25.0
click>=8.0.0
rich>=12.0.0
aiohttp>=3.8.0
'''

# =============================================================================
# MANIFEST.in - Include additional files
# =============================================================================

MANIFEST_IN = '''include README.md
include LICENSE
include CHANGELOG.md
include requirements.txt
include pyproject.toml
recursive-include pyninja/data *.json
recursive-include pyninja/templates *.yml *.md
recursive-exclude * __pycache__
recursive-exclude * *.py[co]
'''

# =============================================================================
# LICENSE - MIT License
# =============================================================================

LICENSE = '''MIT License

Copyright (c) 2025 PyNinja Community

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# =============================================================================
# Create package structure
# =============================================================================

def create_package_structure():
    """Create the complete package structure"""
    import os
    
    # Create directories
    os.makedirs("pyninja", exist_ok=True)
    os.makedirs("pyninja/data", exist_ok=True)
    os.makedirs("pyninja/templates", exist_ok=True)
    os.makedirs("tests", exist_ok=True)
    
    # Create __init__.py files
    with open("pyninja/__init__.py", "w") as f:
        f.write('"""PyNinja - The Ultimate Python Dependency Ninja"""\n\n__version__ = "1.0.0"\n')
    
    # Create pyproject.toml
    with open("pyproject.toml", "w") as f:
        f.write(PYPROJECT_TOML)
    
    # Create requirements.txt
    with open("requirements.txt", "w") as f:
        f.write(REQUIREMENTS_TXT)
    
    # Create MANIFEST.in
    with open("MANIFEST.in", "w") as f:
        f.write(MANIFEST_IN)
    
    # Create LICENSE
    with open("LICENSE", "w") as f:
        f.write(LICENSE)
    
    print("✅ Package structure created successfully!")
    print("\nNext steps:")
    print("1. Move your main code to pyninja/cli.py")
    print("2. Create README.md (see artifact below)")
    print("3. Run: python -m build")
    print("4. Run: python -m twine upload dist/*")

if __name__ == "__main__":
    create_package_structure()