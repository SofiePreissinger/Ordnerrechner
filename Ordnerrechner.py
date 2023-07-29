import os

def get_directory_size(pfad):
    total_size = 0
    with os.scandir(pfad) as entries:
        for entry in entries:
            if entry.is_file():
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_size += get_directory_size(entry.path)
    return total_size

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

def print_directory_sizes(pfad):
    total_size = get_directory_size(pfad)
    print(f"{pfad} - {format_size(total_size)}")
    with os.scandir(pfad) as entries:
        for entry in entries:
            if entry.is_dir():
                size = get_directory_size(entry.path)
                print(f"{entry.path} - {format_size(size)}")

if __name__ == "__main__":
    target_directory = input("Bitte geben Sie den Dateipfad eines Orderners ein: ")
    print("Ordner wird gescannt...\n")
    print_directory_sizes(target_directory)