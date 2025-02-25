# Contributing to Metropy

First off, thank you for considering contributing to Metropy! It's people like you that make Metropy such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [maintainer's email].

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps
* Explain which behavior you expected to see instead and why
* Include details about your configuration and environment

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* A clear and descriptive title
* A detailed description of the proposed functionality
* Explain why this enhancement would be useful
* List any potential drawbacks
* If possible, provide a code example of how you envision using the feature

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

## Development Process

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   uv pip install -e ".[dev,docs]"
   ```

3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

4. Make your changes:
   * Write meaningful commit messages
   * Include tests
   * Update documentation as needed

5. Run the test suite:
   ```bash
   pytest
   ```

6. Check types:
   ```bash
   mypy src
   ```

7. Run linting:
   ```bash
   ruff check src tests
   ```

## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* Consider starting the commit message with an applicable emoji:
    * 🎨 `:art:` when improving the format/structure of the code
    * 🐎 `:racehorse:` when improving performance
    * 🚱 `:non-potable_water:` when plugging memory leaks
    * 📝 `:memo:` when writing docs
    * 🐛 `:bug:` when fixing a bug
    * 🔥 `:fire:` when removing code or files
    * 💚 `:green_heart:` when fixing the CI build
    * ✅ `:white_check_mark:` when adding tests
    * 🔒 `:lock:` when dealing with security
    * ⬆️ `:arrow_up:` when upgrading dependencies
    * ⬇️ `:arrow_down:` when downgrading dependencies

### Python Styleguide

* Follow PEP 8
* Use type hints
* Write docstrings in Google style
* Keep functions focused and small
* Use meaningful variable names
* Comment only when necessary
* Use f-strings for string formatting

### Documentation Styleguide

* Use Markdown for documentation
* Keep language clear and concise
* Include code examples when relevant
* Update the changelog for notable changes

## Additional Notes

### Issue and Pull Request Labels

* `bug` - Something isn't working
* `enhancement` - New feature or request
* `documentation` - Improvements or additions to documentation
* `good first issue` - Good for newcomers
* `help wanted` - Extra attention is needed
* `invalid` - Something's wrong
* `question` - Further information is requested
* `wontfix` - This will not be worked on

## Recognition

Contributors will be recognized in our changelog and README.
