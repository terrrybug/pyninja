#!/bin/bash
# PyNinja PyPI Upload Script
set -e

echo "🥷 PyNinja PyPI Upload Script"
echo "=============================="

# Check if we're in the right directory
if [ ! -f "setup.py" ] || [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: setup.py or pyproject.toml not found!"
    echo "Make sure you're in the PyNinja root directory."
    exit 1
fi

# Check if build tools are installed
if ! command -v python -m build &> /dev/null; then
    echo "❌ Error: 'build' package not found!"
    echo "Install with: pip install build"
    exit 1
fi

if ! command -v twine &> /dev/null; then
    echo "❌ Error: 'twine' package not found!"
    echo "Install with: pip install twine"
    exit 1
fi

echo "🧹 Cleaning old builds..."
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/

echo "📦 Building package..."
python -m build

echo "🔍 Validating package..."
python -m twine check dist/*

echo ""
echo "📋 Package contents:"
echo "Source distribution:"
python -m tarfile -l dist/*.tar.gz | head -10
echo ""
echo "Wheel distribution:"
python -m zipfile -l dist/*.whl | head -10

echo ""
echo "🧪 Ready to upload to TestPyPI..."
read -p "Upload to TestPyPI? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Uploading to TestPyPI..."
    python -m twine upload --repository testpypi dist/*
    
    echo ""
    echo "✅ TestPyPI upload complete!"
    echo "Test installation with:"
    echo "pip install --index-url https://test.pypi.org/simple/ pyninja"
    echo ""
    
    read -p "Upload to production PyPI? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🚀 Uploading to production PyPI..."
        python -m twine upload dist/*
        echo ""
        echo "🎉 Production PyPI upload complete!"
        echo "Your package is now available with: pip install pyninja"
    else
        echo "ℹ️  Skipping production upload."
        echo "To upload later, run: python -m twine upload dist/*"
    fi
else
    echo "ℹ️  Skipping TestPyPI upload."
    echo "To upload to TestPyPI: python -m twine upload --repository testpypi dist/*"
    echo "To upload to PyPI: python -m twine upload dist/*"
fi

echo ""
echo "🏁 Done!"