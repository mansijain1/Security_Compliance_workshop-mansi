# CORE CONCEPTS– Day 4


## 📦 Pipeline Integration

### 1. Why is it important to run Trivy scans (for OS packages and dependencies) as part of the CI/CD pipeline instead of only scanning after deployment?

Running Trivy during the CI/CD pipeline ensures that known vulnerabilities in operating system packages and application dependencies are caught before the code is deployed to production. This prevents vulnerable containers or packages from being shipped, reducing the attack surface early.

> **Benefit**: Fails fast and blocks insecure builds from being promoted further, following the **shift-left security** principle.

---

### 2. Why is it important to run security scans (SAST, dependency scanning, DAST) directly in the CI/CD pipeline instead of only during production?

Security scans in the CI/CD pipeline allow for:

- **Early detection** of vulnerabilities in source code (SAST), libraries (dependency scanning), and application behavior (DAST).
- **Prevention** of vulnerable code reaching production environments.
- **Continuous security** integrated with developer workflows.

Delaying these scans until production introduces risk and technical debt. CI/CD integration enforces **automated, scalable, and repeatable** security checks.

---

## Tool Roles and Complementarity

### 3. How do Bandit, Semgrep, Trivy, and OWASP ZAP complement each other in the pipeline?

Each tool targets a different layer of the application stack. Together, they provide **comprehensive coverage**:

| Tool         | Scan Type      | What it Detects (Example)                                               |
|--------------|----------------|--------------------------------------------------------------------------|
| **Bandit**   | Static (SAST)  | Hardcoded passwords, use of insecure libraries in Python code           |
| **Semgrep**  | Static (SAST)  | Insecure patterns like unsanitized input passed to SQL queries or `eval` |
| **Trivy**    | Dependency/OS  | CVEs in OS packages (e.g., `openssl`) and third-party Python libraries   |
| **OWASP ZAP**| Dynamic (DAST) | Live application issues like reflected XSS, open redirects               |

> These tools do not overlap significantly — they **complement each other** by scanning different layers of the system.

---

## Developer/DevOps Actionability

### 4. If Trivy reports a HIGH severity vulnerability in a base image or Bandit flags hardcoded secrets, what should the developer or DevOps engineer do next?

#### Trivy – High Vulnerability in Base Image:
- Update the base image to a patched version (`python:3.9-slim-bullseye`, etc.)
- Rebuild and re-scan the image to confirm the vulnerability is resolved
- Document and justify if any vulnerability is to be temporarily accepted (with mitigations)

#### Bandit – Hardcoded Secrets Detected:
- Remove secrets from code immediately
- Rotate any exposed secrets or keys (e.g., API keys, passwords)
- Clean the Git history using tools like `git filter-repo` or `BFG Repo-Cleaner`
- Move secrets to a secure manager (AWS Secrets Manager, HashiCorp Vault, etc.)

> Never ignore or commit secrets — even if the code is in a private repository.

