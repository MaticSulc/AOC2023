
def checkNeighbors(position):

	neigh_pos = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),(1, -1), (1, 0), (1, 1))
	all_chars = ('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ':', ';', '"', '<', '>', ',', '?', '/', '`', '~')
	for i in neigh_pos:
		#check if its out of range
		if position[0] + i[0] < 0 or position[0] + i[0] >= len(data) or position[1] + i[1] < 0 or position[1] + i[1] >= len(data[0]):
			continue
		if data[position[0] + i[0]][position[1] + i[1]] in all_chars:
			return True
	
	return False



data = []
numbers =[]

with open('input') as f:
	for line in f:
		data.append(list(line))

for i in range(len(data)):
	counter = 0
	while counter < len(data[i]):
		number = ''
		if(data[i][counter].isdigit()):
			number += data[i][counter]
			for k in range(counter+1, len(data[i])):
				if(data[i][k].isdigit()):
					number += data[i][k]
				else:
					break

			valid = False
			for j in range(len(number)):
				if checkNeighbors([i, counter + j]):
					valid = True
					break
			
			if valid:
				numbers.append(number)

			counter += len(number)
		else:
			counter += 1

print(sum([int(i) for i in numbers]))