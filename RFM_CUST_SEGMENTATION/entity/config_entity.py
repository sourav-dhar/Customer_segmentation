from collections import namedtuple


TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",
                                    [
                                        "pipeline_name",
                                        "artifact_dir"
                                    ])

DataIngestionConfig = namedtuple("DataIngestionConfig",
                                 [
                                    "dataset_download_url",
                                     "raw_data_dir",
                                     "ingested_dir"
                                 ])


