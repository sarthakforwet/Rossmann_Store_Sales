# Import required libraries
import os
from google.cloud import storage  # Google Cloud Storage client library
from kaggle.api.kaggle_api_extended import KaggleApi  # Kaggle API for data download
import pandas as pd  # For data manipulation
import json  # For JSON operations

def download_and_upload_to_gcs():
    """
    Downloads data from Kaggle competition and uploads it to Google Cloud Storage.
    Handles the extraction of files and cleanup of unnecessary data.
    """
    # Initialize Google Cloud Storage client with service account credentials
    storage_client = storage.Client()
    
    # Set target bucket name and get bucket reference
    bucket_name = 'gcloud-pipelines'

    bucket = storage_client.bucket(bucket_name)
    
    # Download competition data using Kaggle CLI
    # Note: Requires kaggle.json credentials file in Users/khand/.kaggle/
    os.system('kaggle competitions download -c rossmann-store-sales')
    
    # Extract the downloaded zip file
    os.system('unzip rossmann-store-sales.zip')
    
    # os.system('cp kaggle.json /home/airflow/.config/')
    # Remove the sample submission file as it's not needed
    os.system('rm sample_submission.csv store.csv')

    try:
        # Iterate through all files in current directory
        for filename in os.listdir('./'):
            # Process only CSV files
            if filename.endswith('.csv'):
                
                # Pre-processing
                
                # Log the current file being processed
                print(f"Processing {filename}...")
                
                # Create a blob (file) reference in the GCS bucket
                blob = bucket.blob(filename)
                
                # Upload the file to GCS
                blob.upload_from_filename(filename)
                    
                # Log successful upload
                print(f"Successfully uploaded {filename}")            
                print("Upload complete!")
        
    except Exception as e:
        # Log any errors that occur during processing
        print(f"An error occurred: {str(e)}")
        raise  # Re-raise the exception to ensure proper error handling

def main():
    """
    Main function to orchestrate the data pipeline.
    Provides error handling and execution flow control.
    """
    try:
        # Execute the download and upload process
        download_and_upload_to_gcs()
        
    except Exception as e:
        # Log pipeline failures
        print(f"Pipeline failed: {str(e)}")
        raise  # Re-raise the exception to ensure proper error handling

# Standard boilerplate to call the main() function
if __name__ == "__main__":
    main()