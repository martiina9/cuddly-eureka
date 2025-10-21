import os
import json

def find_all_json_files (files_dir: str):
    all_json_fpaths= []
    for fname in os.listdir(files_dir):
        if fname.endswith(".json"):
            all_json_fpaths.append(fname)
    return all_json_fpaths


def read_json(json_fpath: str):
    with open(json_fpath, mode ="r", encoding="utf-8") as json_file:
        return json.load(json_file)

def rewrite_to_csv():
    pass

def main():
    folder = "lekce"
    all_json_fpaths = find_all_json_files(folder)
    print(all_json_fpaths)
    find_all_json_files(folder)
    for fpath in all_json_fpaths:
        contents = read_json(fpath)
        print(fpath)
        print(contents)

main()