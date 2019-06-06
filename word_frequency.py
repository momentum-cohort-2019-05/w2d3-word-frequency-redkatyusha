STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

# Import regex module
import re

# Open file, read lines
original_file = open("seneca_falls.txt", "r")
original_file = original_file.readlines()

original_file = ' '.join(original_file)

# Clean up file
original_file = original_file.lower()
clean_file = re.sub(r'[^a-z ]', "", original_file)

# Split and sort 
clean_file = clean_file.split()
clean_file = sorted(clean_file)

#print(clean_file)