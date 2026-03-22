import os
import sys
import csv
import json
import pickle


class FileHandler:
    def __init__(self, path):
        self.path = path
        self.data = []

    def load(self):
        raise NotImplementedError

    def save(self, path):
        raise NotImplementedError

    def display(self):
        for row in self.data:
            print(row)

    def modify(self, x, y, value):
        try:
            self.data[y][x] = value
        except IndexError:
            print(f"Error: cannot modify cell ({x}, {y})")
            sys.exit(1)


class CSVHandler(FileHandler):
    def load(self):
        with open(self.path, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            self.data = [row for row in reader]

    def save(self, path):
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(self.data)


class JSONHandler(FileHandler):
    def load(self):
        with open(self.path, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def save(self, path):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)


class PickleHandler(FileHandler):
    def load(self):
        with open(self.path, "rb") as file:
            self.data = pickle.load(file)

    def save(self, path):
        with open(path, "wb") as file:
            pickle.dump(self.data, file)


def get_handler(path):
    ext = os.path.splitext(path)[1].lower()

    if ext == ".csv":
        return CSVHandler(path)
    elif ext == ".json":
        return JSONHandler(path)
    elif ext == ".pickle":
        return PickleHandler(path)
    else:
        print(f"Error: unsupported file type '{ext}'")
        sys.exit(1)


def show_files_in_directory(path):
    directory = os.path.dirname(path) or "."
    print(f"Files in directory '{directory}':")
    try:
        for file_name in os.listdir(directory):
            print(file_name)
    except FileNotFoundError:
        print("Directory does not exist.")


def parse_change(change_str):
    parts = change_str.split(",", 2)
    if len(parts) != 3:
        print(f"Error: invalid change format '{change_str}'")
        sys.exit(1)

    try:
        x = int(parts[0].strip())
        y = int(parts[1].strip())
        value = parts[2].strip()
        return x, y, value
    except ValueError:
        print(f"Error: invalid row or column in '{change_str}'")
        sys.exit(1)


def main():
    if len(sys.argv) < 3:
        print("Usage: python reader.py <src> <dst> [\"X,Y,value\" ...]")
        sys.exit(1)

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.exists(src) or not os.path.isfile(src):
        print(f"Error: source file '{src}' does not exist or is not a file.")
        show_files_in_directory(src)
        sys.exit(1)

    handler = get_handler(src)
    handler.load()

    for change in changes:
        x, y, value = parse_change(change)
        handler.modify(x, y, value)

    print("Modified file content:")
    handler.display()

    dst_handler = get_handler(dst)
    dst_handler.data = handler.data
    dst_handler.save(dst)

    print(f"File saved to: {dst}")


if __name__ == "__main__":
    main()