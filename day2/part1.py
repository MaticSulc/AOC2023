red_max = 12
green_max = 13
blue_max = 14

valid = []

with open('input') as f:
	for line in f:
		gameIndex = line.split(':')[0].split(' ')[1]
		data = line.split(':')[1].split(';')
		
		red = green = blue = 0

		for i in data:
			colors = i.split(',')
			for j in colors:
				if 'red' in j:
					red = max(red, int(j.split(' ')[1]))
				elif 'green' in j:
					green = max(green, int(j.split(' ')[1]))
				elif 'blue' in j:
					blue = max(blue, int(j.split(' ')[1]))

		if red <= red_max and green <= green_max and blue <= blue_max:
			valid.append(gameIndex)

print(sum([int(i) for i in valid]))