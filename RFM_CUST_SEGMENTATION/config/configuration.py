import os, sys
from RFM_CUST_SEGMENTATION.exception import CustomException
from RFM_CUST_SEGMENTATION.logger import logging
from RFM_CUST_SEGMENTATION.entity.config_entity import *
from RFM_CUST_SEGMENTATION.entity.artifact_entity import *
from RFM_CUST_SEGMENTATION.constant import *
from RFM_CUST_SEGMENTATION.utils.utils import read_yaml_file

class Configuration:
    def __init__ (self,
                  config_file_path:str = CONFIG_FILE_PATH)
