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
