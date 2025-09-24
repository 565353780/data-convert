import os

from data_convert.Method.path import removeFile


def clearTag(folder_path: str) -> bool:
    for root, _, files in os.walk(folder_path):
        for file in files:
            if not file.endswith("_start.txt"):
                continue

            removeFile(root + "/" + file)
    return True
