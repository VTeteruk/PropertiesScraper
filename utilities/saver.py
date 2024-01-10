import dataclasses
import json
import os
from dataclasses import asdict


def save_dataclass_list_to_json(dataclass_list: list[dataclasses], file_path: str) -> None:
    output_dir = os.path.dirname(file_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Convert list of objects to list of dictionaries
    data_dict_list = [asdict(data_obj) for data_obj in dataclass_list]

    with open(file_path, "w") as json_file:
        json.dump(data_dict_list, json_file, indent=2)
