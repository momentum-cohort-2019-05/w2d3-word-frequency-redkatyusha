# Open test.txt and set to variable
#ainulindalë = open("test.txt", "r")

# Prints the text of test.txt as one line
#print(ainulindalë.read())

# Open test.txt with read privileges and set as variable "ainulindalë"
#with open("test.txt", "r") as ainulindalë:
    # For each line in ainulindalë, do the next thing
    #for line in ainulindalë:
        # Split each word into its own line
        #for word in line.split():
            # Print all the words as separate lines
            #print(word)

#with open("test.txt", "r") as source_file:
#    source_str = str((source_file.readline()))

#clean_text = ""
#alphabet_and_space = "abcdefghijklmnopqrstuvwxyz"
#for character in source_str:
#    if character.lower() in alphabet_and_space:
#        clean_text += character.lower()