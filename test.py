# Open test.txt and set to variable
#ainulindalë = open("test.txt", "r")

# Prints the text of test.txt as one line
#print(ainulindalë.read())

# Open test.txt with read privileges and set as variable "ainulindalë"
#with open("test.txt", "r") as ainulindalë:
    # For each line in ainulindalë, do the next thing
#    for line in ainulindalë:
        # Split each word into its own line
#        for word in line.split():
            # Print each word on its own line
#            print(word)

# WHAT THE FUCK DO I DO NOW

#with open("test.txt", "r") as source_file:
#    source_str = str((source_file.readline()))

#clean_text = ""
#alphabet_and_space = "abcdefghijklmnopqrstuvwxyz"
#for character in source_str:
#    if character.lower() in alphabet_and_space:
#        clean_text += character.lower()

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

