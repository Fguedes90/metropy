# Installation

Metropy is available on PyPI and can be installed with pip or your favorite Python package manager.

## Requirements

- Python 3.9 or higher
- pip 20.0 or higher (for dependency resolution)

## Basic Installation

=== "Using UV (Recommended)"
    ```bash
    uv pip install metropy-rop
    ```

=== "Using pip"
    ```bash
    pip install metropy-rop
    ```

=== "Using poetry"
    ```bash
    poetry add metropy-rop
    ```

=== "Using pdm"
    ```bash
    pdm add metropy-rop
    ```

## Optional Dependencies

Metropy provides optional features that can be installed with extra dependencies:

### Pydantic Integration

For integration with Pydantic models and validation:

=== "Using UV"
    ```bash
    uv pip install "metropy-rop[pydantic]"
    ```

=== "Using pip"
    ```bash
    pip install "metropy-rop[pydantic]"
    ```

### Documentation Tools

For building the documentation locally:

=== "Using UV"
    ```bash
    uv pip install "metropy-rop[docs]"
    ```

=== "Using pip"
    ```bash
    pip install "metropy-rop[docs]"
    ```

### Development Dependencies

If you want to contribute to Metropy, install the development dependencies:

=== "Using UV"
    ```bash
    # Clone the repository
    git clone https://github.com/francis/metropy-rop.git
    cd metropy-rop

    # Create and activate a virtual environment (optional but recommended)
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

    # Install development dependencies
    uv pip install -e ".[dev,docs]"
    ```

=== "Using pip"
    ```bash
    # Clone the repository
    git clone https://github.com/francis/metropy-rop.git
    cd metropy-rop

    # Create and activate a virtual environment (optional but recommended)
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

    # Install development dependencies
    pip install -e ".[dev,docs]"
    ```

## Verifying Installation

You can verify that Metropy is installed correctly by running Python and importing the package:

```python
from metropy import Result

# Should print the version number
print(Result.__version__)
```

## Next Steps

- Follow the [Quick Start](quickstart.md) guide to learn how to use Metropy
- Read about [Basic Concepts](concepts.md) to understand Railway Oriented Programming
- Check out the [User Guide](../user-guide/result.md) for detailed documentation