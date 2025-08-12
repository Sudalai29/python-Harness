A simple Python calculator application with intentional bugs and vulnerabilities for CI/CD pipeline testing.

## Features
- Basic arithmetic operations (add, subtract, multiply, divide)
- Power calculations
- Operation history
- Advanced expression evaluation (using eval - intentionally vulnerable)
- Command execution in debug mode (intentionally vulnerable)

## Known Issues (Intentional for Demo)

### Security Vulnerabilities:
1. **Command Injection**: The `execute_command` method uses `os.system()` without input sanitization
2. **Code Injection**: The `advanced_calculate` method uses `eval()` which can execute arbitrary code
3. **Hardcoded Credentials**: Admin password is hardcoded in the class
4. **Outdated Dependencies**: requirements.txt includes vulnerable package versions

### Code Quality Issues:
1. **Division by Zero**: No error handling for division operations
2. **No Input Validation**: User inputs are not validated
3. **Dead Code**: Unused methods and variables
4. **Missing Exception Handling**: Insufficient error handling throughout
5. **Missing Test Coverage**: No tests for edge cases like division by zero

## Running the Application

```bash
python3 calculator.py
```

## Running Tests

```bash
python3 -m pytest test_calculator.py -v
```

## CI/CD Pipeline

This project includes a Harness CI pipeline that:
1. Sets up Python environment
2. Installs dependencies
3. Runs unit tests with coverage
4. Performs security scanning with Bandit
5. Checks for vulnerable dependencies with Safety
6. Runs code quality checks with flake8 and pylint
7. Performs SonarQube analysis
8. Archives all reports and artifacts

## SonarQube Integration

The pipeline is configured to work with SonarQube for:
- Code quality analysis
- Security vulnerability detection
- Code coverage reporting
- Technical debt assessment

Set the following environment variables in Harness:
- `SONAR_HOST_URL`: Your SonarQube server URL
- `SONAR_TOKEN`: Authentication token for SonarQube

## Repository Structure
```
.
├── calculator.py              # Main application
├── test_calculator.py         # Unit tests
├── requirements.txt           # Python dependencies
├── .harness/
│   └── pipeline.yaml         # Harness CI pipeline
├── sonar-project.properties  # SonarQube configuration
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## Demo Purpose

This application is specifically designed for demonstrating CI/CD pipeline capabilities and should NOT be used in production due to the intentional security vulnerabilities and bugs.
```
```

This repository structure provides a complete demo setup with:

**Intentional Vulnerabilities & Bugs:**
- Command injection via `os.system()`
- Code injection via `eval()`
- Hardcoded credentials
- Division by zero errors
- No input validation
- Outdated vulnerable dependencies
- Dead code and unused variables

**CI Pipeline Features:**
- Unit testing with coverage
- Security scanning with Bandit
- Dependency vulnerability checking with Safety
- Code quality analysis with flake8/pylint
- SonarQube integration
- Artifact archiving

**What SonarQube will detect:**
- Security hotspots and vulnerabilities
- Code smells and maintainability issues
- Bug-prone code patterns
- Test coverage gaps
- Duplicated code blocks

To use this:
1. Create a new Git repository
2. Add these files to your repo
3. Configure your Harness connector to point to the repository  
4. Set up your SonarQube server details in Harness environment variables
5. Run the pipeline to see how it detects all the intentional issues

The pipeline will run but report various security and quality issues, making it perfect for demonstrating your CI/CD and code analysis capabilities!
