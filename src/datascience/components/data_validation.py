import os
from src.datascience import logger
import pandas as pd
from src.datascience.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True

            # Read the data
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            data_types = data.dtypes.apply(lambda x: x.name).to_dict()

            all_schema = self.config.all_schema.keys()
            actual_data_types = self.config.all_schema

            # Ensure the directory for the status file exists
            status_file_dir = os.path.dirname(self.config.STATUS_FILE)
            os.makedirs(status_file_dir, exist_ok=True)

            # Validate columns and data types
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    logging.error(f"Column {col} not in schema")
                elif data_types[col] != actual_data_types[col]:
                    validation_status = False
                    logging.error(f"Data type mismatch for column {col}")

            # Write the validation status to the file
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e

    
