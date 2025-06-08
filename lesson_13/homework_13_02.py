import json
from pathlib import Path
import logging
from json.decoder import JSONDecodeError




def validate_json_files(folder_path):
    folder = Path(folder_path)
    log_file = Path(__file__).parent / "Error.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    for file in folder.iterdir():
        if file.is_file():
            try:
                with open(file, encoding='utf-8') as f:
                    json.load(f)
                print(f"Файл валідний: {file.name}")
            except JSONDecodeError as e:
                logging.error(f"Файл {file.name} не валідний: {e}")

validate_json_files(Path(__file__).parent / "work_with_json")