import yaml
import pandas as pd
from RFM_CUST_SEGMENTATION.constant import *
import os

def write_schema_yaml(csv_file):
    # Read CSV file and get number of columns and column names
    df = pd.read_csv(csv_file)
    num_cols = len(df.columns)
    column_names = df.columns.tolist()
    column_dtypes = df.dtypes.astype(str).tolist()  # Convert data types to string for YAML compatibility

    # Create schema dictionary
    schema = {
        "FileName": os.path.basename(csv_file),
        "NumberOfColumns": num_cols,
        "ColumnNames": dict(zip(column_names, column_dtypes))
    }
    file_path = SCHEMA_FILE_PATH
    # Write schema to schema.yaml file
    with open(file_path, "w") as file:
        yaml.dump(schema, file)

# Call the function with the CSV file path
write_schema_yaml(r"research/Online Retail.csv")