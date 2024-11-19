import os
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col in all_schema:
                    validation_status = True
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Validation status: {validation_status}")
                else:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as file:
                        file.write(f"Validation status: {validation_status}")
                
            return validation_status
        
        except Exception as e:
            raise e