# Serverless-IoT-Data-Processing
This project implements a serverless architecture for processing IoT sensor data using AWS services. The system captures data from IoT sensors, processes it using AWS Lambda, and stores it in DynamoDB for further analysis. The primary goal is to create an efficient, scalable, and cost-effective solution for handling real-time IoT data.

Key Components:

AWS IoT Core: Acts as the central hub for receiving MQTT messages from IoT sensors.

AWS Lambda: Processes incoming sensor data and forwards it to the database.

Amazon DynamoDB: Stores processed IoT data for real-time and historical analysis.

Amazon CloudWatch: Monitors and logs system performance and errors.

IAM Roles & Policies: Ensures secure access to AWS resources.

Workflow:

IoT devices publish sensor data (temperature, humidity, etc.) to AWS IoT Core using MQTT.

AWS IoT Core triggers an AWS Lambda function upon receiving new data.

The Lambda function validates, processes, and stores the data in DynamoDB.

CloudWatch logs errors and performance metrics for monitoring.

Data can be analyzed or visualized using AWS services like QuickSight or external BI tools.

Expected Outcomes:

A fully serverless and scalable IoT data processing pipeline.

Low-latency data ingestion and storage.

Cost-efficient pay-as-you-go infrastructure.

Secure and fault-tolerant IoT data management.
