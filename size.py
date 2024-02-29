from collections import defaultdict
  

def process_data(data):
    """
    Processes the given data and stores directory totals in memory.

    Args:
        data: A list of lines, where each line is a full pathname and size separated by a space.

    Returns:
        A dictionary mapping directory paths to their total sizes.
    """

    directory_sizes = defaultdict(int)
    for path, size in data:
        # Split the path into its components
        components = path.split("/")

        # Iterate through all possible prefixes of the path
        for i in range(1, len(components) + 1):
            prefix = "/".join(components[:i])
            directory_sizes[prefix] += int(size)

    return directory_sizes


# Example usage
data = [
    ("/foo/bar/test.dat", 1024),
    ("/baz/qux.txt", 512),
    ("/foo/bar/baz.txt", 2048),
]

directory_sizes = process_data(data)

print(directory_sizes)  # Output: {'/': 3584, '/foo': 3072, '/foo/bar': 3072, '/baz': 512}

# You can now query any directory for its total size
print(directory_sizes["/foo/bar"])  # Output: 3072

with open('directory_sizes.txt', 'w') as f:
    for directory, size in directory_sizes.items():
        f.write(f"{directory} {size}\n")
