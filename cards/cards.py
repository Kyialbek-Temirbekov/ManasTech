cards = []
x = ['J','Q','K','A']
type = ['H','S','C','D']
for i in range(2,11):
	for j in type:
		cards.append(str(i) + j)
for i in x:
        for j in type:             
                cards.append(i + j)
for i in cards:
	print(i)
print(len(cards))
