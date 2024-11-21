from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "smooth-mason-436217-p3"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_CSV_to_BigQuery"

    template_body = {
        "jobName": "rossman_load",  # Provide a unique name for the job
        "parameters": {
            "inputFilePattern": "gs://looker-analysis/*.csv",
            "schemaJSONPath": "gs://looker-analysis/bq.json",
            "outputTable": "smooth-mason-436217-p3:rossman_store.store_sales",
            "bigQueryLoadingTemporaryDirectory": "gs://looker-analysis/BigQueryWriteTemp/",
            "badRecordsOutputTable": "smooth-mason-436217-p3:rossman_store.bq_bad_records",
            "containsHeaders": "true",
            "delimiter": ",",
            "csvFormat": "Default",
            "csvFileEncoding": "UTF-8"
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)