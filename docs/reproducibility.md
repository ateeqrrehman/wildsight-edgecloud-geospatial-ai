\# Reproducibility



\## Objective



This document defines how to reproduce the WildSight EdgeCloud workflow in a consistent environment.



\## Environment



Recommended environment:



\- Python 3.10 or newer

\- AWS CLI configured locally

\- Kaggle API configured locally

\- Required Python packages installed from `requirements.txt`



\## Dataset Reproducibility



Use a fixed dataset subset when comparing experiments. Record the species folder, image count, image resolution, dataset source, and dataset access date.



\## Configuration Reproducibility



Track:



\- AWS region

\- SageMaker endpoint name

\- S3 bucket name

\- DynamoDB table name

\- EventBridge rules

\- SNS notification target

\- Dataset subset

\- Model artifact version



\## Experiment Reproducibility



Each experiment should record:



\- Experiment ID

\- Dataset subset

\- Image count

\- Batch size

\- Endpoint configuration

\- Runtime

\- Average latency

\- Throughput

\- Detection metrics

\- Notes



\## Output Validation



A successful run should produce:



\- Uploaded S3 image objects

\- DynamoDB prediction records

\- SNS notifications

\- GeoJSON artifact

\- Flattened JSON artifact



\## Future Improvements



\- Add dataset version control

\- Add automated benchmark scripts

\- Add CI validation for core Python modules

\- Add experiment tracking through MLflow or a similar tool

\- Add deterministic test fixtures

