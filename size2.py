import json
from collections import defaultdict

def process_json_data(json_filenames):
    """
    Processes JSON files containing path and size information, storing directory totals.

    Args:
        json_filenames: A list of filenames for the JSON files to process.

    Returns:
        A dictionary mapping directory paths to their total sizes.
    """

    directory_sizes = defaultdict(int)

    for filename in json_filenames:
        with open(filename, "r") as f:
            for line in f:
                data = json.loads(line)
                path = data["path"]
                size = data["size"]

                # Split the path and accumulate sizes
                components = path.split("/")
                for i in range(1, len(components) + 1):
                    prefix = "/".join(components[:i])
                    directory_sizes[prefix] += size

    return directory_sizes


# Example Usage
json_files = ["../projects/bptest1.dat"] # List of your JSON files
directory_sizes = process_json_data(json_files)

print(directory_sizes["zazzle"])  # Example query

with open('directory_sizes.txt', 'w') as f:
    for directory, size in directory_sizes.items():
            f.write(f"{directory} {size}\n")

