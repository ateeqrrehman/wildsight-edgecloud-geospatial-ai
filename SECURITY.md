# Security Policy

## Secret Management

Do not commit cloud credentials, Kaggle tokens, API keys, or environment-specific secrets to this repository.

## Recommended Practices

- Use IAM roles where possible
- Use least-privilege access policies
- Rotate credentials regularly
- Store secrets through environment variables or AWS Secrets Manager
- Exclude local configuration files through `.gitignore` and `.dockerignore`

## Infrastructure Considerations

The repository includes deployment-oriented infrastructure assets for experimentation and research workflows. Production deployments should include additional security hardening, monitoring, and access-control validation.

## Reporting Security Issues

For sensitive security-related concerns, avoid posting credentials or infrastructure details publicly. Use private communication channels when discussing vulnerabilities or deployment risks.
