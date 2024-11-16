This repository contains the code for analysis of Sales from Stores of Rossman and a forecasting model to predict the next week's sales of those stores.

Tasks done
[x] Created a script to automatically pull data from Kaggle and push it to Google Cloud.

[x] Created Cloud Function to automatically trigger whenever a new file is uploaded to the target cloud bucket, creating a dataflow job to load the data from CSV files into target BigQuery table. 

[x] Created a Composer environment and prepared a Directed Acyclic Graph using Airflow to extract the kaggle dataset and upload it to the target bucket.

[] Create a machine learning model on VertexAI Workbench taking the data from BigQuery table and training an xgboost model for the task of predicting store sales.

[] Deploy the trained model on the Model Registry to make online predictions thereby completing the pipeline.

[] Search for additional MLOps approaches to monitor model's predictions and expeirment with data drift and similar strategies.


Following is a pictorial demonstration of the complete pipeline - 

![Pipeline Image](Cloud_Pipeline.png)


Initially, I required kaggle.josn file and so I created another task in DAG and it transferrd the kaggle.json file to the cloud storage but then I removed it as it was giving error regarding the file already exists.

