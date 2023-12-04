sum = 0
with open('input') as f:
	for line in f:
		winning_numbers = line.split('|')[0].split(':')[1].split()
		my_number = line.split('|')[1].split()

		points = 0
		for number in my_number:
			if number in winning_numbers:
				if points == 0:
					points += 1
				else:
					points *= 2
		sum += points		
print(sum)