red_max = green_max = blue_max = sum = 0

with open('input') as f:
	for line in f:
		gameIndex = line.split(':')[0].split(' ')[1]
		data = line.split(':')[1].split(';')
		
		red_max = green_max = blue_max = 0

		for i in data:
			colors = i.split(',')
			for j in colors:
				if 'red' in j:
					red_max = max(red_max, int(j.split(' ')[1]))
				elif 'green' in j:
					green_max = max(green_max, int(j.split(' ')[1]))
				elif 'blue' in j:
					blue_max = max(blue_max, int(j.split(' ')[1]))

		power = red_max * green_max * blue_max
		sum += power

print(sum)