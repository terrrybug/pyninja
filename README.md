<<<<<<< HEAD
# pyninja
=======
# PyNinja 🥷

[![PyPI version](https://badge.fury.io/py/pyninja.svg)](https://badge.fury.io/py/pyninja)
[![Python versions](https://img.shields.io/pypi/pyversions/pyninja.svg)](https://pypi.org/project/pyninja/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/pyninja)](https://pepy.tech/project/pyninja)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> **The Ultimate Python Dependency Ninja** - Silently strike outdated dependencies, eliminate security vulnerabilities, and modernize your Python projects with stealth and precision! 🥷⚡

PyNinja is a powerful, community-driven tool that revolutionizes Python dependency management. It combines security scanning, intelligent modernization, performance optimization, and automated updates into one sleek package.

## 🌟 Why PyNinja?

- **🔒 Security First**: Real-time vulnerability scanning with OSV database integration
- **🚀 Smart Modernization**: Automatically detects and suggests modern alternatives to legacy packages
- **⚡ Performance Focused**: Recommends faster, more efficient package alternatives
- **🤖 CI/CD Ready**: Generates GitHub Actions workflows and PR descriptions
- **🎯 Multi-Format Support**: Works with `requirements.txt`, `pyproject.toml`, `Pipfile`, and more
- **🧠 Intelligent Analysis**: ML-inspired scoring for compatibility and community health
- **🎨 Beautiful CLI**: Rich terminal interface with progress bars and interactive prompts

## ⚡ Quick Start

### Installation

```bash
# Install PyNinja
pip install pyninja

# Or with all optional features
pip install pyninja[all]
```

### Basic Usage

```bash
# Analyze your project (auto-detects requirements files)
pyninja

# Security-focused scan with auto-fixes
pyninja --security-first --auto-fix

# Interactive mode with modern alternatives
pyninja --interactive --modernize --performance

# Generate GitHub PR for updates
pyninja --github-pr --export-report security_report.json
```

## 🎯 Features Overview

### 🔍 Smart Analysis
- **Multi-format detection**: Automatically finds and parses requirements files
- **Dependency tree mapping**: Visualizes complex dependency relationships
- **Compatibility scoring**: Analyzes Python version compatibility
- **Community health metrics**: Evaluates package maintenance quality

### 🛡️ Security & Safety
- **Real-time vulnerability scanning** using OSV database
- **Automated security patches** with version recommendations
- **License compatibility checking** for compliance
- **Deprecation warnings** for unmaintained packages

### 🔄 Modernization Engine
- **Python 2 → 3 migration** assistance
- **Legacy package replacement** suggestions
- **Performance optimization** recommendations
- **Modern alternative discovery** (httpx vs requests, orjson vs json, etc.)

### 🤖 Automation & CI/CD
- **GitHub Actions integration** with workflow generation
- **Automated PR creation** with detailed change descriptions
- **Docker optimization** suggestions
- **Dry-run capabilities** for safe testing

## 📊 Usage Examples

### Basic Dependency Analysis

```bash
# Analyze current directory
pyninja

# Specify custom requirements file
pyninja --file custom-requirements.txt

# Target specific Python version
pyninja --python-version 3.11
```

### Security-Focused Scanning

```bash
# Security scan with immediate fixes
pyninja --security-first --auto-fix

# Strict mode (exit with error if vulnerabilities found)
pyninja --strict --security-first

# Export detailed security report
pyninja --export-report security_audit.json
```

### Modernization & Performance

```bash
# Full modernization analysis
pyninja --modernize --performance

# Interactive mode with choices
pyninja --interactive --modernize

# Preview changes without applying
pyninja --dry-run --modernize --output updated_requirements.txt
```

### CI/CD Integration

```bash
# Generate GitHub workflow
pyninja --github-pr --auto-fix

# Clear cache and run fresh analysis
pyninja --cache-clear --export-report ci_report.json
```

## 🎨 Beautiful Output

PyNinja provides rich, colorful terminal output:

```
🚀 PyNinja v1.0.0 - The Ultimate Python Dependency Ninja
📦 Found 25 packages to analyze

┌─ Summary ──────────────────┬─────────┐
│ Total Packages             │ 25      │
│ Packages with Updates      │ 12      │
│ Security Vulnerabilities   │ 3       │
│ Deprecated Packages        │ 2       │
│ Compatibility Score        │ 0.92/1.0│
│ Community Score            │ 0.88/1.0│
└────────────────────────────┴─────────┘

🚨 Security Vulnerabilities
  • requests (2.25.1) - 2 vulnerabilities
  • pillow (8.0.0) - 1 vulnerability

📅 Outdated Packages
  • numpy: 1.20.0 → 1.24.3
  • pandas: 1.3.0 → 2.0.1
  • django: 3.2.0 → 4.2.1

🚀 Modernization Opportunities
  • json: Consider orjson for 2-3x faster JSON processing
  • requests: Use httpx for async HTTP requests
```

## 🔧 Configuration

PyNinja supports various configuration options:

### Command Line Options

```bash
Options:
  -f, --file PATH                 Requirements file path
  -o, --output PATH              Output file for updated requirements
  --format [requirements.txt|pyproject.toml|pipfile]
  --auto-fix                     Automatically apply fixes
  --strict                       Exit with error if issues found
  --security-first              Prioritize security updates
  --modernize                   Suggest modern alternatives
  --performance                 Focus on performance improvements
  --python-version TEXT         Target Python version
  --github-pr                   Generate GitHub PR description
  --dry-run                     Preview changes without applying
  --interactive                 Interactive mode with prompts
  --cache-clear                 Clear cache before running
  --export-report PATH          Export detailed JSON report
  --help                        Show this message and exit
```

### Configuration File

Create a `.pyninja.toml` file in your project root:

```toml
[pyninja]
security_first = true
modernize = true
performance = false
target_python = "3.11"
auto_fix = false
strict_mode = false

[pyninja.exclude]
packages = ["legacy-package", "internal-tool"]

[pyninja.alternatives]
"old-package" = "new-package"
```

## 🌍 Supported Formats

PyNinja works with multiple dependency formats:

- **requirements.txt** - Traditional pip requirements
- **pyproject.toml** - Modern Python packaging (PEP 621)
- **Pipfile** - Pipenv format
- **poetry.lock** - Poetry dependencies
- **setup.py** - Legacy setuptools (read-only)

## 🤝 GitHub Integration

Generate automated dependency update workflows:

```bash
pyninja --github-pr
```

This creates:
- `github_pr_description.md` - PR description template
- `.github/workflows/dependencies.yml` - GitHub Actions workflow
- Detailed change analysis and security impact assessment

## 🔄 Migration Examples

### Python 2 to 3 Migration
```bash
# Before
mysql-python==1.2.5
pycrypto==2.6.1
unittest2==1.1.0

# After PyNinja analysis
PyMySQL>=3.1.0
pycryptodome>=3.17.0
# unittest2 removed (built into Python 3)
```

### Performance Modernization
```bash
# Before
requests==2.28.0
json  # built-in module

# After PyNinja suggestions
httpx>=0.24.0  # async support
orjson>=3.8.0  # 2-3x faster JSON
```

## 📈 Advanced Features

### Vulnerability Database Integration
- **OSV (Google)** - Default, comprehensive vulnerability data
- **GitHub Advisory** - GitHub's security advisory database  
- **Snyk** - Commercial vulnerability intelligence

### Performance Optimization
- **Binary wheel preferences** for faster installs
- **Compiled alternative suggestions** (e.g., orjson, uvloop)
- **Memory usage optimization** recommendations
- **Container-specific optimizations**

### Community Health Scoring
- Recent update activity
- Maintainer responsiveness  
- GitHub stars and forks
- Documentation quality
- Test coverage indicators

## 🧪 Testing & Development

```bash
# Install development dependencies
pip install pyninja[dev]

# Run tests
pytest

# Code formatting
black pyninja/
isort pyninja/

# Type checking
mypy pyninja/
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes** and add tests
4. **Run the test suite**: `pytest`
5. **Submit a pull request**

### Development Setup
```bash
git clone https://github.com/pyninja-dev/pyninja.git
cd pyninja
pip install -e .[dev]
pre-commit install
```

## 🔮 Roadmap

- [ ] **Machine Learning** integration for smarter recommendations
- [ ] **Multi-language support** (Node.js, Go, Rust dependencies)
- [ ] **IDE plugins** (VS Code, PyCharm)
- [ ] **Enterprise features** (SAML, audit logs, policy enforcement)
- [ ] **Cloud integrations** (AWS, GCP, Azure)
- [ ] **Supply chain analysis** and SBOM generation

## 📚 Documentation

- **Full Documentation**: [pyninja.dev/docs](https://pyninja.dev/docs)
- **API Reference**: [pyninja.dev/api](https://pyninja.dev/api)
- **Examples**: [github.com/pyninja-dev/examples](https://github.com/pyninja-dev/examples)
- **Blog**: [pyninja.dev/blog](https://pyninja.dev/blog)

## 🆘 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/pyninja-dev/pyninja/issues)
- **Discussions**: [Community discussions](https://github.com/pyninja-dev/pyninja/discussions)
- **Discord**: [Join our community](https://discord.gg/pyninja)
- **Email**: [community@pyninja.dev](mailto:community@pyninja.dev)

## 📜 License

PyNinja is released under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **OSV** for comprehensive vulnerability data
- **PyPI** for package metadata
- **Rich** for beautiful terminal interfaces
- **Click** for excellent CLI framework
- **Community contributors** who make PyNinja awesome

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=pyninja-dev/pyninja&type=Date)](https://star-history.com/#pyninja-dev/pyninja&Date)

---

<div align="center">

**Made with ❤️ by the PyNinja Community**

[Website](https://pyninja.dev) • [Documentation](https://pyninja.dev/docs) • [GitHub](https://github.com/pyninja-dev/pyninja) • [PyPI](https://pypi.org/project/pyninja/)

</div>
>>>>>>> a4eb837 (Initial PyNinja release with GitHub Actions CI)
