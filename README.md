# Dataiku GitOps Demo Project

This repository is part of a Proof of Concept (POC) demonstrating how to implement GitOps for Dataiku projects. It accompanies the blog article titled "Implementing GitOps for Dataiku: A Hands-On Guide," which provides a step-by-step walkthrough of setting up a GitOps workflow using Dataiku, GitHub, and custom GitHub Actions.

## Overview

The goal of this POC is to showcase how GitOps can be used to manage Dataiku projects across different environments (development, staging, and production) using Git as the single source of truth. By leveraging GitHub Actions, this project automates the CI/CD pipeline, ensuring that changes are tested and deployed consistently and reliably.

## Key Components

### GitHub Workflows

This repository includes GitHub workflows that automate the CI/CD process:

- **PR Workflow (`.github/workflows/pr.yml`)**: This workflow is triggered by pull requests to the `prod` branch. It runs tests in the staging environment to ensure that changes are production-ready before they are merged.

- **Release Workflow (`.github/workflows/release.yml`)**: This workflow is triggered by pushes to the `prod` branch. It deploys the changes to the production environment and runs tests to verify the deployment.

### Test Script (`tests.py`)

The `tests.py` script is a crucial part of the GitOps workflow. It defines the tests that are run in the staging and production environments to validate the changes. The script uses the Dataiku API to execute a specific recipe and check for successful execution.

## Resources

- [Blog Article: Implementing GitOps for Dataiku: A Hands-On Guide](#) (Link to the blog article)
- [GitHub Action Repository](https://github.com/qcastel/dataiku-gitops-github-action) (Link to the GitHub Action repository)

## Conclusion

This demo project provides a practical example of how GitOps can be implemented for Dataiku projects. By following the steps outlined in the blog article and using the resources provided in this repository, you can set up a GitOps workflow that enhances your deployment process with consistency, reliability, and collaboration.
