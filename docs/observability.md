\# Observability and Monitoring



\## Overview



WildSight EdgeCloud is designed as an event-driven AI pipeline. Observability is required to track ingestion, inference, storage, notifications, artifact generation, and failure recovery across the workflow.



\## Monitoring Targets



\- S3 image upload events

\- SageMaker endpoint invocation latency

\- SageMaker endpoint errors

\- DynamoDB write success rate

\- EventBridge rule execution

\- SNS notification delivery

\- GeoJSON generation success

\- Flattened JSON export success

\- End-to-end pipeline runtime



\## Recommended AWS Monitoring Tools



\- Amazon CloudWatch Logs

\- Amazon CloudWatch Metrics

\- SageMaker endpoint metrics

\- DynamoDB table metrics

\- S3 access logs

\- EventBridge rule monitoring

\- SNS delivery status logging



\## Key Metrics



| Component | Metric |

|---|---|

| SageMaker | Invocation latency |

| SageMaker | Invocation error rate |

| S3 | Object upload count |

| DynamoDB | Write latency |

| EventBridge | Trigger success |

| SNS | Delivery success |

| Pipeline | End-to-end runtime |



\## Failure Modes



Potential failure modes include:



\- Missing image metadata

\- Failed SageMaker endpoint invocation

\- DynamoDB write throttling

\- EventBridge rule misconfiguration

\- SNS subscription not confirmed

\- Invalid GeoJSON output

\- Missing local configuration

\- Interrupted dataset download



\## Future Improvements



\- Add structured JSON logging

\- Add CloudWatch dashboards

\- Add alert thresholds

\- Add automated failure recovery

\- Add tracing across pipeline stages

\- Add drift monitoring for model confidence changes

