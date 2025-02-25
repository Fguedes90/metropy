# Metropy

A modern, type-safe Railway Oriented Programming (ROP) library for Python that provides a robust way to handle errors and compose operations.

## Overview

Metropy implements the Railway Oriented Programming pattern in Python, offering a more functional approach to error handling compared to traditional try/except blocks. It helps you write more maintainable and composable code by treating success and failure cases as first-class citizens.

The library is designed with Python's type system in mind, providing full type safety and IDE support while maintaining a clean, pythonic API.

## Key Features

- 🚂 **Railway Oriented Programming**: Elegant error handling with the `Result[T, E]` type
- 🔒 **Type Safety**: Full type hints support with generics and modern Python typing
- 🔗 **Functional Composition**: Chain operations with the `bind` and `map` operators
- 🎯 **Zero Dependencies**: Core functionality requires only Python 3.9+
- 🔄 **Async Support**: First-class support for async/await operations
- 🛡️ **Pydantic Integration**: Seamless integration with Pydantic for data validation
- 🎨 **Pythonic API**: Clean, intuitive interface following Python's best practices
- 🔍 **Comprehensive Error Handling**: Rich utilities for error transformation and recovery
- 📚 **Rich Documentation**: Comprehensive documentation with examples and API reference

## Installation

```bash
# Using pip with UV (recommended)
uv pip install metropy-rop

# Using pip
pip install metropy-rop

# With Pydantic integration
pip install "metropy-rop[pydantic]"

# With documentation tools
pip install "metropy-rop[docs]"
```

## Quick Start

### Basic Usage

```python
from metropy import Result, railway

@railway
def divide(a: float, b: float) -> Result[float, str]:
    if b == 0:
        return Result.failure("Division by zero")
    return Result.success(a / b)

# Simple usage
result = divide(10, 2)
print(result.unwrap_or(0))  # Output: 5.0

# Error handling
result = divide(10, 0)
print(result.unwrap_error())  # Output: "Division by zero"
```

### Function Composition

```python
from metropy import Result, bind, map

def validate_input(x: int) -> Result[int, str]:
    return (Result.success(x) 
            if x > 0 
            else Result.failure("Input must be positive"))

def double(x: int) -> int:
    return x * 2

def process_data(x: int) -> Result[str, str]:
    return Result.success(f"Result: {x}")

# Compose functions using the | operator
pipeline = (
    validate_input
    | map(double)
    | bind(process_data)
)

result = pipeline(5)
print(result.unwrap())  # Output: "Result: 10"
```

### Async Support

```python
from metropy import async_railway
from aiohttp import ClientSession

@async_railway
async def fetch_data(url: str) -> Result[dict, str]:
    async with ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return Result.success(await response.json())
            return Result.failure(f"HTTP {response.status}")

# Usage with async/await
async def main():
    result = await fetch_data("https://api.example.com/data")
    if result.is_success():
        print(f"Data: {result.unwrap()}")
    else:
        print(f"Error: {result.unwrap_error()}")
```

### Pydantic Integration

```python
from pydantic import BaseModel
from metropy.pydantic import validate_model

class User(BaseModel):
    name: str
    age: int

@validate_model(User)
def create_user(data: dict) -> Result[User, str]:
    # Validation is handled automatically by the decorator
    return Result.success(data)

# Usage
result = create_user({"name": "John", "age": 30})
print(result.unwrap().name)  # Output: "John"

# Invalid data
result = create_user({"name": "John"})  # Missing age
print(result.is_failure())  # Output: True
```

## Advanced Features

- **Error Recovery**: Use `recover` to provide fallback values
- **Error Transformation**: Transform errors with `map_error`
- **Parallel Validation**: Combine multiple results with `all_successful`
- **Debugging**: Use `tap` for logging and debugging
- **Custom Error Types**: Define your own error types with full type safety

## Development

1. Clone the repository
2. Install development dependencies:
   ```bash
   uv pip install -e ".[dev,docs]"
   ```
3. Run tests:
   ```bash
   pytest
   ```
4. Run type checks:
   ```bash
   mypy src
   ```
5. Run linting:
   ```bash
   ruff check src
   ```
6. Build documentation:
   ```bash
   # Serve documentation locally
   mkdocs serve

   # Build documentation
   mkdocs build
   ```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This library is inspired by:
- Railway Oriented Programming pattern
- Rust's `Result` type
- Haskell's `Either` monad
- F#'s Railway Oriented Programming