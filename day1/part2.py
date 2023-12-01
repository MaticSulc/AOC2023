import re

written_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0

with open('input') as f:
    for line in f:
        processed_line = []
        for i in range(len(line)): #foreach char
            found_mapping = ""
            for idx, val in enumerate(written_digits, 1): #try all mappings
                if line[i:].startswith(val):  #if mapping found
                    found_mapping = "".join([str(index) for index, value in enumerate(written_digits, 1) if line[i:].startswith(value)]) #get index of mapping
                    break
            if found_mapping:
                processed_line.append(found_mapping) #add mapping to processed line
            else:
                processed_line.append(line[i]) #add char to processed line

        #part 1 solution
        digits = re.findall(r'\d', "".join(processed_line))
        if(len(digits) < 2):
            total = digits[0] + digits[0]
        else:
            total = digits[0] + digits[-1]
        sum += int(total)
            
print(sum)