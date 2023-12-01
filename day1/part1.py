import re

sum = 0
with open('input') as f:
	for line in f:
		digits = re.findall(r'\d', line)
		if(len(digits) < 2):
			total = digits[0] + digits[0]
		else:
			total = digits[0] + digits[-1]
		sum += int(total)
		print(total)
		
print(sum)