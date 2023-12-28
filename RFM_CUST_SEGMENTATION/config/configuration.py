import os,sys
from RFM_CUST_SEGMENTATION.exception import CustomException
from RFM_CUST_SEGMENTATION.logger import logging
from RFM_CUST_SEGMENTATION.entity.config_entity import  TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig
from RFM_CUST_SEGMENTATION.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from RFM_CUST_SEGMENTATION.constant import *
from RFM_CUST_SEGMENTATION.constant.training_pipeline import *
from RFM_CUST_SEGMENTATION.utils.utils import read_yaml_file

class Configuration:
    
    def __init__ (self,config_file_path:str = CONFIG_FILE_PATH,current_time_stamp:str = CURRENT_TIME_STAMP):
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            CustomException(e,sys)
            
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            
            data_validation_artifact_dir = os.path.join(artifact_dir, 
                                                        DATA_VALIDATION_ARTIFACT_DIR, 
                                                        self.time_stamp)
            data_validation_config = 
        except Exception as e:
            CustomException(e,sys)
                   
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR, self.time_stamp)
            
            # constant folder  # here we call all variable that is under DATA_INGESTION_CONFIG_KEY
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            # constant folder -- in constant it is from config.yaml
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            
    #raw data
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,
                                        data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])
            
    #ingested data
            ingested_data_dir = os.path.join(data_ingestion_artifact_dir,
                                             data_ingestion_info[DATA_INGESTION_INGESTED_DATA_DIR_KEY])
            
            data_ingestion_config = DataIngestionConfig(
                dataset_download_url= dataset_download_url,
                raw_data_dir=raw_data_dir,
                ingested_data_dir=ingested_data_dir
            )
            logging.info(f"Data Ingestion pipeline Config completed : {data_ingestion_config}")
            
            return data_ingestion_config
        
        except Exception as e:
            CustomException(e,sys)
            
    def get_data_validation_config(self) -> DataValidationConfig:
        
            

            
                 
        
    def get_training_pipeline_config(self)->TrainingPipelineConfig:
            try:
                training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]

                artifact_dir = os.path.join(ROOT_DIR,
                                            training_pipeline_config[TRAINING_PIPLELINE_NAME_KEY],
                                            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])  
        
                training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)

                logging.info(f"Training pipeline Config Completed : {training_pipeline_config}")

                return training_pipeline_config

            except Exception as e:
                raise CustomException(e,sys) from e 
            
