# WildSight EdgeCloud: Mission-Scale Wildlife Detection and Geospatial Intelligence Pipeline

**WildSight EdgeCloud** is a cloud-native AI/ML research and engineering project for automated wildlife detection, geospatial intelligence generation, and scalable model inference across AWS services. The system combines **YOLOv8 computer vision**, **Amazon SageMaker inference**, **Amazon S3 data ingestion**, **Amazon DynamoDB metadata storage**, **Amazon EventBridge orchestration**, **Amazon SNS notifications**, and **GeoJSON/BI-ready analytics artifacts** to transform camera-trap imagery into structured location intelligence.

The project is designed as an applied AI systems research pipeline, emphasizing the full lifecycle required to operationalize visual detection models: data ingestion, inference, metadata persistence, event-driven automation, geospatial enrichment, analytics export, containerized execution, orchestration readiness, and cost-aware infrastructure management.

---

## Architecture Overview

```mermaid
flowchart LR
    A[Camera Trap Dataset] --> B[Upload Simulation]
    B --> C[Amazon S3]
    C --> D[Amazon EventBridge]
    D --> E[Amazon SageMaker YOLOv8 Endpoint]
    E --> F[Amazon DynamoDB]
    F --> G[GeoJSON Generation]
    F --> H[Flattened Analytics Export]
    G --> I[Map Visualization]
    H --> J[BI Dashboard]
    D --> K[Amazon SNS Notifications]
```

---

## Repository Structure

```text
.
├── benchmarks/              # Inference profiling and benchmarking utilities
├── docs/                    # Research, architecture, observability, and reproducibility docs
├── experiments/             # Experiment tracking artifacts
├── k8s/                     # Kubernetes deployment manifests
├── lambdas/                 # Event-driven AWS Lambda workflows
├── Model/                   # YOLOv8 model artifacts and inference logic
├── src/                     # S3 ingestion and streaming utilities
├── stage2_yolov8/           # SageMaker deployment workflows
├── utils/                   # Dataset download and provisioning helpers
├── .github/workflows/       # CI validation workflows
├── Dockerfile               # Containerized execution configuration
└── README.md
```

---

## Documentation Index

| Document | Purpose |
|---|---|
| [Architecture](docs/architecture.md) | System architecture and AWS workflow |
| [Research Report](docs/research_report.md) | Research framing and methodology |
| [Benchmarking](docs/benchmarking.md) | Benchmarking and profiling strategy |
| [Model Card](docs/model_card.md) | YOLOv8 model documentation |
| [Data Card](docs/data_card.md) | Dataset structure and limitations |
| [Observability](docs/observability.md) | Monitoring and failure-mode strategy |
| [Reproducibility](docs/reproducibility.md) | Reproducibility and experiment tracking |

---

## Research Context

Wildlife monitoring programs increasingly depend on large-scale camera-trap imagery to study animal movement, habitat use, species distribution, and ecological risk. Manual image review is slow, expensive, inconsistent, and difficult to scale across large geographic regions. Raw detections alone are also insufficient for operational decision support because model outputs must be connected to location, time, metadata, and downstream visualization workflows.

This project investigates how a cloud-native computer vision pipeline can automate the conversion of raw camera-trap images into geospatial intelligence products. The system is structured around an end-to-end ML workflow where images are ingested, processed by a YOLOv8 detection model, enriched with metadata, stored in a structured database, and exported into analytics-ready formats.

---

## Research Gap

Many wildlife AI implementations focus primarily on object detection accuracy, while fewer address the operational lifecycle required to deploy computer vision systems in real environments. Important gaps include:

- Limited integration between model inference and cloud-native event orchestration
- Weak support for geospatial outputs usable by analysts and decision makers
- Insufficient attention to scalable metadata storage and downstream analytics
- Limited reproducibility guidance for cloud-based inference workflows
- Incomplete treatment of deployment tradeoffs, cost, reliability, and operational readiness

WildSight EdgeCloud addresses these gaps by treating wildlife detection as a complete AI system design problem rather than only a model prediction task.

---

## Technical Contribution

This repository contributes a reference architecture for cloud-native wildlife detection and geospatial analytics using AWS-managed services and YOLOv8 inference. The main technical contributions include:

- End-to-end image ingestion and inference workflow for camera-trap data
- YOLOv8-based object detection pipeline deployed through Amazon SageMaker
- Event-driven processing through Amazon EventBridge rules
- Prediction and metadata persistence using Amazon DynamoDB
- Automated notification workflow through Amazon SNS
- Flattened JSON generation for BI workflows
- GeoJSON generation for map-based visualization
- Docker-based containerization for reproducible runtime environments
- Kubernetes manifests for orchestration-ready deployment patterns
- Operational framing around scalability, reproducibility, cost control, security, and deployment readiness

---

## System Architecture

The pipeline follows a cloud-native, event-driven architecture:

1. **Dataset Ingestion**  
   Camera-trap imagery is retrieved from a public wildlife dataset and staged for simulation.

2. **Object Storage**  
   Images and associated metadata are uploaded to Amazon S3, representing a camera-trap ingestion source.

3. **Model Inference**  
   A YOLOv8 model is served through an Amazon SageMaker endpoint for wildlife detection.

4. **Metadata and Prediction Storage**  
   Image metadata and model prediction outputs are stored in Amazon DynamoDB.

5. **Event-Driven Processing**  
   Amazon EventBridge rules coordinate logging, notification, and geospatial artifact generation.

6. **Notification Layer**  
   Amazon SNS supports email-based notification of image events and classification outputs.

7. **Geospatial Analytics Layer**  
   Prediction records are transformed into flattened JSON and GeoJSON outputs for BI dashboards and web-map visualization.

---

## End-to-End ML Workflow

WildSight EdgeCloud demonstrates a full AI/ML workflow:

- Dataset acquisition through the Kaggle API
- Data staging and camera-trap upload simulation
- Cloud object storage using Amazon S3
- YOLOv8 inference through Amazon SageMaker
- Event-driven processing with Amazon EventBridge
- Prediction persistence in Amazon DynamoDB
- Notification delivery through Amazon SNS
- Export of analytics-ready artifacts for geospatial visualization
- Cost-aware cleanup of provisioned inference infrastructure

---

## Containerization and Orchestration

WildSight EdgeCloud includes containerization and orchestration-oriented deployment assets to support reproducible execution and scalable infrastructure workflows.

### Docker Support

The repository includes a Dockerfile for containerized execution of the inference and ingestion workflow. Containerization enables:

- Reproducible runtime environments
- Dependency isolation
- Portable deployment workflows
- Simplified cloud-native execution patterns
- More consistent execution across local, cloud, and CI environments

### Kubernetes Support

The repository includes Kubernetes deployment manifests for orchestration-oriented deployment patterns. These manifests demonstrate how inference services can be prepared for scalable workload management and container orchestration environments.

Potential orchestration use cases include:

- Distributed inference workloads
- Batch image processing
- Horizontal scaling experiments
- Cloud-native deployment validation
- Infrastructure portability across managed Kubernetes environments

---

## Preliminary Benchmark Results

The repository includes benchmarking utilities under `benchmarks/` and an experiment tracking template under `experiments/`. The table below is prepared for measured results after pipeline execution.

| Experiment | Images | Avg Latency | P95 Latency | Throughput | Notes |
|---|---:|---:|---:|---:|---|
| Baseline YOLOv8 Endpoint | TBD | TBD | TBD | TBD | SageMaker endpoint benchmark |
| Local Inference Baseline | TBD | TBD | TBD | TBD | Local model execution benchmark |
| Batch Ingestion Workflow | TBD | TBD | TBD | TBD | End-to-end ingestion and export benchmark |

---

## Sample Outputs

Visual output artifacts can be added under `docs/assets/` as the pipeline is executed and evaluated.

Planned artifacts include:

- `docs/assets/sample_geojson_map.png`
- `docs/assets/sample_dashboard.png`
- `docs/assets/sample_prediction_output.png`

These outputs are intended to document geospatial visualization, BI-ready analytics, and representative model prediction records.

---

## Technology Stack

| Area | Tools and Services |
|---|---|
| Computer Vision | YOLOv8 |
| Programming | Python |
| Cloud Platform | AWS |
| Model Serving | Amazon SageMaker |
| Object Storage | Amazon S3 |
| Metadata Store | Amazon DynamoDB |
| Event Orchestration | Amazon EventBridge |
| Notification System | Amazon SNS |
| Containerization | Docker |
| Orchestration | Kubernetes manifests |
| CI/CD | GitHub Actions |
| Geospatial Output | GeoJSON |
| Analytics Output | Flattened JSON for BI workflows |
| Dataset Access | Kaggle API |
| Visualization | Power BI / web-map compatible outputs |

---

## Dataset

This project uses the **Spatiotemporal Wildlife Dataset** available through Kaggle:

https://www.kaggle.com/datasets/travisdaws/spatiotemporal-wildlife-dataset?resource=download&select=images

The configuration can be used with a smaller image subset for initial testing and expanded to larger species-specific folders for broader evaluation. The pipeline is structured so additional camera-trap datasets can be integrated with limited configuration changes.

---

## Methodology

### 1. Data Collection and Preparation

The dataset is retrieved using the Kaggle API. Images are organized by species and prepared for upload simulation into the AWS ingestion layer.

### 2. Cloud Ingestion Simulation

The main workflow simulates camera-trap image uploads into Amazon S3. Each image includes metadata that supports downstream geospatial and analytical processing.

### 3. Model Inference

The pipeline uses a YOLOv8 model endpoint deployed through Amazon SageMaker. Images are passed through the endpoint to generate detection predictions.

### 4. Prediction Persistence

Inference outputs and image metadata are written to DynamoDB, enabling structured querying, downstream transformation, and analytics.

### 5. Event-Driven Automation

EventBridge rules coordinate pipeline behavior, including ingestion logging, batch notification, and GeoJSON artifact creation.

### 6. Geospatial Output Generation

Prediction records are converted into:

- `wildlife_predictions_FLATTENED.json` for BI workflows
- `wildlife_predictions.geojson` for web-map visualization

---

## Evaluation Strategy

The project supports evaluation across ML quality, system performance, and operational reliability dimensions.

Potential evaluation metrics include:

- Detection confidence by species or image group
- Precision, recall, and mAP for labeled evaluation data
- End-to-end inference latency
- SageMaker endpoint response time
- Image ingestion throughput
- DynamoDB write consistency and record completeness
- Geospatial output validity
- Pipeline reliability across repeated simulation runs
- Cloud resource cost during active inference windows

---

## Operational Relevance

Although the applied domain is wildlife monitoring, the architecture is relevant to broader AI systems involving imagery, sensor events, metadata, and location-aware decision support.

Relevant application patterns include:

- Automated processing of imagery and sensor-derived data
- Cloud-native deployment of computer vision models
- Event-driven AI workflows for operational environments
- Metadata enrichment and structured prediction storage
- Location-aware intelligence generation
- Dashboard and map-based decision support
- Cost-aware management of provisioned inference infrastructure

The same design pattern can be adapted for disaster response, infrastructure inspection, environmental security, border monitoring, and other operational contexts where image data must be converted into timely analytical products.

---

## Security and Credential Handling

Do not commit cloud credentials, Kaggle tokens, or environment-specific secrets to this repository. Authentication files should remain local and should be excluded through `.gitignore` and `.dockerignore`.

For production use, prefer IAM roles, scoped permissions, temporary credentials, AWS Secrets Manager, or environment-based credential injection instead of long-lived local credential files.

---

## Configuration

Update `config.yaml` with the AWS user context, region, and notification email. Before running the pipeline, confirm that AWS resources are configured correctly, including S3 buckets, DynamoDB tables, EventBridge rules, SNS subscription settings, and SageMaker endpoint configuration.

---

## Setup and Execution

### 1. Install Dependencies

```bash
pip install kaggle boto3 pyyaml ultralytics
```

Install any additional project-specific dependencies required by the local environment.

### 2. Configure Kaggle Access

Generate a Kaggle API token and place `kaggle.json` in the local Kaggle configuration directory.

### 3. Download Dataset

Run the dataset download utility:

```bash
python utils/download_dataset.py
```

### 4. Prepare AWS Resources

Before execution, verify:

- The S3 ingestion bucket is available and old test images are removed if needed
- The DynamoDB table exists and old test records are cleared if needed
- EventBridge rules are enabled
- SNS subscription email is configured and confirmed
- SageMaker endpoint configuration is available

### 5. Create SageMaker Endpoint

In Amazon SageMaker, create an endpoint named:

```text
yolov8s
```

Use the configured YOLOv8 endpoint configuration available in the AWS environment.

### 6. Run Pipeline

Run the main workflow:

```bash
python main.py
```

During execution, the pipeline uploads images, performs inference, stores predictions, sends notifications, and generates analytics artifacts.

---

## Expected Outputs

After a successful run, the system produces:

- Uploaded image objects in the configured S3 bucket
- Metadata and prediction records in DynamoDB
- Email notifications through Amazon SNS
- `wildlife_predictions_FLATTENED.json` for BI ingestion
- `wildlife_predictions.geojson` for map visualization

---

## Cost Management

The SageMaker endpoint is provisioned infrastructure and may continue to incur cost while active. After testing or demonstration, delete the endpoint from Amazon SageMaker.

Do not delete reusable endpoint configurations, deployable models, DynamoDB tables, or other shared infrastructure unless intentionally removing the full environment.

---

## Limitations

Current limitations include:

- The pipeline depends on preconfigured AWS resources
- SageMaker endpoint costs require cleanup after testing
- The current workflow is designed for simulation-style image ingestion rather than live camera hardware integration
- Evaluation depends on available labeled ground truth for species-level performance metrics
- Edge deployment and disconnected environment support are not yet fully implemented

---

## Future Research Directions

Planned research and engineering extensions include:

- Containerized inference service using Docker
- Kubernetes deployment manifests for scalable inference workloads
- CI/CD workflow for automated testing and deployment validation
- Batch inference support for large camera-trap archives
- Edge deployment for disconnected or low-bandwidth environments
- Model monitoring and inference drift detection
- Latency and throughput benchmarking under different image-volume workloads
- Precision, recall, and mAP evaluation against labeled validation sets
- Integration with Amazon QuickSight for fully cloud-native BI visualization
- Secure deployment patterns using IAM roles and least-privilege access control

---

## Repository Scope

WildSight EdgeCloud is a research-driven AI engineering repository focused on scalable computer vision deployment, geospatial intelligence, and operational ML workflow design. The project emphasizes not only model inference, but also the system-level requirements needed to transform raw visual data into reliable, usable, and location-aware analytical products.
