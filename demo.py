import os, sys
from RFM_CUST_SEGMENTATION.pipeline.pipeline import Pipeline
from RFM_CUST_SEGMENTATION.components.data_ingestion import DataIngestion
from RFM_CUST_SEGMENTATION.exception import CustomException
from RFM_CUST_SEGMENTATION.logger import logging



def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)
        
if __name__== "__main__":
    main()