from collections import namedtuple

#DataIngestion

DataIngestionArtifact = namedtuple("DataIngestionArtifact",
                                   [
                                       "train_file_path",
                                       "is_ingested",
                                       "message"
                                   ])