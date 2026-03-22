import csv
import sys
import os


def show_files(path):
    folder = os.path.dirname(path) or "."
    print(f"Files in directory '{folder}':")
    try:
        for f in os.listdir(folder):
            print(f)
    except:
        print("Cannot access directory")


def load_csv(path):
    with open(path, "r", newline="", encoding="utf-8") as file:
        return list(csv.reader(file))


def save_csv(path, data):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def apply_change(data, change):
    parts = change.split(",", 2)

    if len(parts) != 3:
        print(f"Invalid format: {change}")
        return

    try:
        x = int(parts[0])
        y = int(parts[1])
        value = parts[2]
    except:
        print(f"Invalid numbers: {change}")
        return

    if y >= len(data) or y < 0:
        print(f"Row out of range: {y}")
        return

    if x >= len(data[y]) or x < 0:
        print(f"Column out of range: {x}")
        return

    data[y][x] = value


def display(data):
    for row in data:
        print(",".join(row))


def main():
    if len(sys.argv) < 3:
        print("Usage: python reader.py <src> <dst> <changes>")
        return

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.exists(src) or not os.path.isfile(src):
        print("Error: file not found")
        show_files(src)
        return

    data = load_csv(src)

    for change in changes:
        apply_change(data, change)

    print("Modified CSV:")
    display(data)

    save_csv(dst, data)
    print(f"Saved to {dst}")


if __name__ == "__main__":
    main()