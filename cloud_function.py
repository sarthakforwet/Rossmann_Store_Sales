from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "smooth-mason-436217-p3"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://looker-analysis/udf.js",
        "JSONPath": "gs://looker-analysis/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "smooth-mason-436217-p3:rossman_store.rossman_store_sales",
        "inputFilePattern": "gs://looker-analysis/*.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://looker-analysis/BigQueryWriteTemp",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)