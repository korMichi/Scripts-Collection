### Extracts text from text file 

substring = ">reverse" # Text to search
extraction = [] # Store all text in a list
relevant_linenumbers = [] # Store all the linenumbers which contain the substring

linenum = 0
with open("201217_reverse-translation.txt", "rt") as reversion_text: # import text
    for line in reversion_text:
        linenum += 1
        extraction.append(line.rstrip("\n")) # adds text into list
        if line.find(substring) != -1: # finds all linenumbers containing the substring and stores the lines in relevant_linenumbers list
            relevant_linenumbers.append(linenum)

reverse_translation = [] # Stores the right extracted lines only
for line_num in relevant_linenumbers:
    reverse_translation.append(extraction[(line_num-1):(line_num+7)]) # Extracts the right linenumbers and stores it in reverse_translation

sequence_dict = {}
for mab in reverse_translation:
        name = ""
        sequence = ""
        n = 0
        for line in mab:
            if n == 0:
                name = line
                name = name[24:-46]
            else:
                sequence += line
            n += 1
        sequence_dict[name] = sequence