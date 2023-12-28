import os,sys
from collections import namedtuple
from datetime import datetime
import pandas as pd
import uuid
from RFM_CUST_SEGMENTATION.config.configuration import Configuration
from RFM_CUST_SEGMENTATION.exception import CustomException
from RFM_CUST_SEGMENTATION.logger import logging
from RFM_CUST_SEGMENTATION.entity.config_entity import DataIngestionConfig
from RFM_CUST_SEGMENTATION.entity.artifact_entity import DataIngestionArtifact
from RFM_CUST_SEGMENTATION.components.data_ingestion import DataIngestion

class Pipeline:
    def __init__(self, config: Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            CustomException(e,sys)
            
    #data_ingestion
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config= self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            CustomException(e,sys)
            
    #pipeline
    
    def run_pipeline(self):
        
        try:
            #data ingestion
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            CustomException(e,sys) 
            
        
        
