# PyPI Upload Guide - Step by Step 🚀

This guide will walk you through uploading your PyNinja package to PyPI so you can install it anywhere with `pip install pyninja`.

## Prerequisites

1. **Create PyPI Account**
   - Go to https://pypi.org/account/register/
   - Create an account and verify your email
   - Go to https://test.pypi.org/account/register/ (for testing)
   - Create an account on TestPyPI as well

2. **Generate API Tokens** (Recommended over username/password)
   - Go to https://pypi.org/manage/account/token/
   - Click "Add API token"
   - Give it a name like "PyNinja Upload"
   - Set scope to "Entire account" (or specific project later)
   - **SAVE THE TOKEN** - you won't see it again!
   - Repeat for TestPyPI: https://test.pypi.org/manage/account/token/

## Step 1: Install Build Tools

```bash
# Install required tools
pip install --upgrade pip
pip install build twine

# Or install in virtual environment (recommended)
python -m venv upload_env
source upload_env/bin/activate  # On Windows: upload_env\Scripts\activate
pip install --upgrade pip build twine
```

## Step 2: Prepare Your Package

Your package structure should look like this (already set up):
```
PyNinja/
├── pyninja/
│   ├── __init__.py
│   ├── cli.py
│   ├── data/
│   └── templates/
├── setup.py
├── pyproject.toml
├── requirements.txt
├── MANIFEST.in
├── LICENSE
├── README.md
└── tests/
```

## Step 3: Update Version Number

Before each upload, update the version in:
1. `setup.py` (line 23): `version="1.0.0"`
2. `pyproject.toml` (line 113): `version = "1.0.0"`
3. `pyninja/__init__.py`: `__version__ = "1.0.0"`

Use semantic versioning (e.g., 1.0.0 → 1.0.1 → 1.1.0 → 2.0.0)

## Step 4: Clean Previous Builds

```bash
# Remove old build artifacts
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/
```

## Step 5: Build the Package

```bash
# Build source and wheel distributions
python -m build

# This creates:
# dist/pyninja-X.X.X.tar.gz (source distribution)
# dist/pyninja-X.X.X-py3-none-any.whl (wheel distribution)
```

## Step 6: Test Upload to TestPyPI (Recommended)

```bash
# Upload to TestPyPI first to test
python -m twine upload --repository testpypi dist/*

# When prompted:
# Username: __token__
# Password: [paste your TestPyPI API token]
```

## Step 7: Test Installation from TestPyPI

```bash
# Test install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ pyninja

# Test the installation
pyninja --help
py-ninja --version
```

## Step 8: Upload to Production PyPI

If TestPyPI upload works:

```bash
# Upload to production PyPI
python -m twine upload dist/*

# When prompted:
# Username: __token__
# Password: [paste your PyPI API token]
```

## Step 9: Test Production Installation

```bash
# Install from production PyPI
pip install pyninja

# Test it works
pyninja --help
```

## Step 10: Set Up .pypirc (Optional)

Create `~/.pypirc` to avoid entering credentials each time:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TESTPYPI_TOKEN_HERE
```

Then upload with:
```bash
python -m twine upload --repository testpypi dist/*  # For testing
python -m twine upload dist/*                        # For production
```

## Automation Script

Create `upload.sh` for automated uploads:

```bash
#!/bin/bash
set -e

echo "🧹 Cleaning old builds..."
rm -rf build/ dist/ *.egg-info/

echo "📦 Building package..."
python -m build

echo "🧪 Uploading to TestPyPI..."
python -m twine upload --repository testpypi dist/*

echo "✅ TestPyPI upload complete!"
echo "Test with: pip install --index-url https://test.pypi.org/simple/ pyninja"
echo ""
echo "To upload to production PyPI, run:"
echo "python -m twine upload dist/*"
```

Make it executable:
```bash
chmod +x upload.sh
./upload.sh
```

## Troubleshooting

### Common Issues:

1. **"File already exists" error**
   - You can't upload the same version twice
   - Increment version number in setup.py, pyproject.toml, and __init__.py

2. **"Invalid or non-existent authentication"**
   - Check your API token is correct
   - Make sure username is `__token__` (with underscores)

3. **"Package name already taken"**
   - Choose a different package name in setup.py
   - Check availability at https://pypi.org/project/YOUR_PACKAGE_NAME/

4. **Missing files in package**
   - Check MANIFEST.in includes all necessary files
   - Verify package_data in setup.py

### Verification Commands:

```bash
# Check package contents before upload
python -m tarfile -l dist/pyninja-*.tar.gz

# Check wheel contents
python -m zipfile -l dist/pyninja-*.whl

# Validate package metadata
python -m twine check dist/*
```

## Best Practices

1. **Always test on TestPyPI first**
2. **Use semantic versioning**
3. **Keep detailed CHANGELOG.md**
4. **Use API tokens instead of passwords**
5. **Test installation in clean environment**
6. **Include comprehensive README.md**
7. **Add proper classifiers in setup.py**

## After Upload Success

Your package will be available at:
- https://pypi.org/project/pyninja/
- Anyone can install with: `pip install pyninja`
- Updates appear within minutes

## Next Steps

1. Set up GitHub Actions for automated PyPI uploads
2. Configure branch protection and release workflows
3. Add badges to README.md
4. Monitor download statistics on PyPI
5. Respond to user issues and feature requests

---

🎉 **Congratulations!** Your package is now available worldwide via `pip install pyninja`