import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    if "DATABRICKS_RUNTIME_VERSION" in os.environ:
        # Está rodando no Databricks
        return {
            "environment": "Databricks",
            "name_table_bronze": os.environ.get("NAME_TABLE_BRONZE", "Null"),
        }
    else:
        # Está rodando local
        return {
            "environment": "Local",
            # "base_path": os.environ.get("LOCAL_PATH_ORIGIN_VOLUMES", "Null"),
        }

cfg = get_config()