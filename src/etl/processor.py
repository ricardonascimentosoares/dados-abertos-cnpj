import os
import duckdb
from src.config.metadata import METADATA
from src.config.paths import DUCKDB_FILE
from src.etl.sql_templates import SQL_INSERT_TEMPLATES, AUX_TABLES_SQL
from src.utils.utils import convert_to_utf8

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "output", "logs")
os.makedirs(LOG_DIR, exist_ok=True)


def create_table_if_not_exists(conn, table_name, metadata):
    columns_def = ", ".join([f"{col} {dtype}" for col, dtype in metadata.items()])
    conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_def});")
    conn.execute(f"TRUNCATE TABLE {table_name};")

def create_aux_tables():
    with duckdb.connect(DUCKDB_FILE) as conn:
        for sql in AUX_TABLES_SQL:
            conn.execute(sql)
        print("Auxiliar tables created or already exist.")


def process_folder(folder_name, folder_path):
    """Process each folder using its specific SQL transformation."""
    print(f"Processing folder: {folder_name}")
    metadata = METADATA.get(folder_name)
    if not metadata:
        print(f"Skipping folder '{folder_name}' (no metadata available).")
        return

    sql_template = SQL_INSERT_TEMPLATES.get(folder_name)
    if not sql_template:
        print(f"No SQL template for folder '{folder_name}'. Skipping.")
        return

    # Only use column names for DuckDB's read_csv
    column_names = list(metadata.keys())

    all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]
    if not all_files:
        print(f"No files found in folder '{folder_name}'.")
        return

    try:
        with duckdb.connect(DUCKDB_FILE) as conn:
            create_table_if_not_exists(conn, folder_name, metadata)
            for csv_file in all_files:
                print(f"Inserting file: {csv_file}")
                utf8_file = convert_to_utf8(csv_file)
                # Pass only column names to the template
                sql = sql_template.format(csv_file=utf8_file, metadata=column_names)
                conn.execute(sql)
                os.remove(utf8_file)
            print(f"Finished processing folder: {folder_name}")
    except Exception as e:
        print(f"Error processing folder '{folder_name}': {e}")
