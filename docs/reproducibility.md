# Reproducibility

## Objective

This document defines how to reproduce the WildSight EdgeCloud workflow in a consistent environment.

## Environment

Recommended environment:

- Python 3.10 or newer
- AWS CLI configured locally
- Kaggle API configured locally
- Required Python packages installed from requirements.txt

## Dataset Reproducibility

Use a fixed dataset subset when comparing experiments. Record the species folder, image count, image resolution, dataset source, and dataset access date.

## Configuration Reproducibility

Track the AWS region, SageMaker endpoint name, S3 bucket name, DynamoDB table name, EventBridge rules, SNS notification target, dataset subset, and model artifact version.

## Experiment Reproducibility

Each experiment should record the experiment ID, dataset subset, image count, batch size, endpoint configuration, runtime, average latency, throughput, detection metrics, and notes.

## Output Validation

A successful run should produce uploaded S3 image objects, DynamoDB prediction records, SNS notifications, a GeoJSON artifact, and a flattened JSON artifact.

## Future Improvements

Future improvements include dataset version control, automated benchmark scripts, CI validation for core Python modules, experiment tracking, and deterministic test fixtures.
