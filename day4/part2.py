with open("input", "r") as f:
	deck = f.readlines() #read all at once

copies = [1 for line in deck]
for i, card in enumerate(deck): #enumerate to get index

	winning_numbers =  list(map(int, card.split('|')[0].split(':')[1].split())) #map to int for easier comparison
	player_numbers =  list(map(int, card.split('|')[1].split()))

	matches = 0
	for number in player_numbers:
		if number in winning_numbers:
			matches += 1 #no double in part 2

	for j in range(i + 1, i + matches + 1): #make compies to those in front of you
		copies[j] += 1 * copies[i]

print(sum(copies))