\# WildSight EdgeCloud Research Report



\## Abstract



WildSight EdgeCloud investigates cloud-native computer vision for automated wildlife detection and geospatial intelligence generation. The system integrates YOLOv8 inference with AWS services including Amazon S3, Amazon SageMaker, Amazon DynamoDB, Amazon EventBridge, and Amazon SNS to convert camera-trap imagery into structured prediction records and geospatial analytics artifacts.



\## 1. Introduction



Large-scale wildlife monitoring depends on camera-trap imagery, but manual review is slow, inconsistent, and difficult to scale. This project explores how object detection, cloud-native infrastructure, and event-driven processing can be combined into an automated wildlife intelligence pipeline.



\## 2. Problem Statement



The core problem is not only detecting animals in images, but operationalizing the full workflow around image ingestion, inference, metadata persistence, geospatial transformation, notification, and analytics-ready output generation.



\## 3. Research Gap



Many computer vision implementations focus primarily on detection accuracy. Fewer systems address the deployment lifecycle required to make model outputs usable in operational settings. This project focuses on the complete AI system pipeline, including inference serving, event orchestration, storage, geospatial enrichment, observability, reproducibility, and cost-aware infrastructure management.



\## 4. Methodology



The pipeline uses a public camera-trap dataset, stages images for upload simulation, sends imagery to Amazon S3, performs YOLOv8 inference through Amazon SageMaker, stores metadata and predictions in DynamoDB, triggers automation through EventBridge, sends notifications through SNS, and exports GeoJSON and flattened JSON outputs.



\## 5. Evaluation Plan



The system can be evaluated through both model and infrastructure metrics, including precision, recall, mAP, endpoint latency, image throughput, DynamoDB write consistency, artifact generation reliability, and end-to-end pipeline runtime.



\## 6. Limitations



Current limitations include dependency on preconfigured AWS resources, simulation-based image ingestion, limited edge deployment support, and reliance on available labeled ground truth for full species-level evaluation.



\## 7. Future Work



Future work includes Kubernetes deployment, automated CI/CD validation, model monitoring, benchmark automation, drift detection, batch inference support, and deployment patterns for low-bandwidth or disconnected environments.

