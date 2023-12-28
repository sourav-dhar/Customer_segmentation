import os,sys
from six.moves import urllib
from RFM_CUST_SEGMENTATION.exception import CustomException
from RFM_CUST_SEGMENTATION.logger import logging
from RFM_CUST_SEGMENTATION.entity.config_entity import DataIngestionConfig
from RFM_CUST_SEGMENTATION.entity.artifact_entity import DataIngestionArtifact
from RFM_CUST_SEGMENTATION.constant import *
from RFM_CUST_SEGMENTATION.constant.training_pipeline import data_ingestion
import zipfile
import shutil

class DataIngestion:
    def __init__(self,data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'>>'*30} Data Ingestion log started.{'<<'*30} \n\n")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            CustomException(e,sys)
            
    def download_data(self) -> str:
        try:
            #raw data directory path
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            logging.info(f' raw data directory: {raw_data_dir}')
            
            #make raw data directory
            os.makedirs(raw_data_dir, exist_ok=True)
            
            #download url
            download_url = self.data_ingestion_config.dataset_download_url + "?raw=true"
            
            #downloading the zip file
            logging.info(f"downloading file from url: {download_url}")
            urllib.request.urlretrieve(download_url, os.path.join(raw_data_dir, "data.zip"))
            logging.info("file donwloaded successfully")
            
            #extracting the zip file
            with zipfile.ZipFile(os.path.join(raw_data_dir, "data.zip"), "r") as zip_ref:
                zip_ref.extractall(raw_data_dir)
            logging.info("zip file extracted successfully")
            
            #delete the downloaded zip file
            os.remove(os.path.join(raw_data_dir, "data.zip"))
            
            #extracting the name of the csv file extracted
            #extracted csv file path (assuming it has a .csv extension)
            csv_file_path = None
            
            #get the list of data in the raw data directory
            file_list = os.listdir(raw_data_dir)
            
            #search for the csv file
            for file_name in file_list:
                if file_name.endswith(".csv"):
                    csv_file_path = os.path.join(raw_data_dir, file_name)
                    break
            #print the name of the csv file
            if csv_file_path is not None:
                csv_file_name = os.path.basename(csv_file_path)
                logging.info("csv file name: ", csv_file_name)
                
            raw_file_path = os.path.join(raw_data_dir, csv_file_name) 
            
            #copy the extracted csv from raw_data_dir ---> ingested Data dir
            
            ingested_file_path = self.data_ingestion_config.ingested_data_dir
            os.makedirs(ingested_file_path, exist_ok=True)
            
            #copy the extracted csv file
            shutil.copy2(raw_file_path, ingested_file_path)
            
            #updating file name
            #set the destination directory for ingested data
            ingested_file_path = os.path.join(self.data_ingestion_config.ingested_data_dir,csv_file_name)
            
            logging.info(f"file : {ingested_file_path} has been downloaded and extracted successfully")
            
            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path=ingested_file_path,
                is_ingested= True,
                message= f"data ingestion completed successfully"
            )
            
            return DataIngestionArtifact
            
        except Exception as e:
            CustomException(e,sys)
            
    def initiate_data_ingestion(self):
        try:
            return self.download_data()
        except Exception as e:
            CustomException(e,sys)
            