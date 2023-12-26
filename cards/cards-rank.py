cards = []
x = ['A','K','Q','J']
a = x + [str(i) for i in range(10,1,-1)]
type = ['H','S','C','D']

print(a)

# getting cards
for i in range(2,11):
	for j in type:
		cards.append(str(i) + j)
for i in x:
        for j in type:             
                cards.append(i + j)
                
ranking = {}
value = 13

for i in range(len(cards)):
	for j in range(i + 1, len(cards)):
		if cards[i][0] == cards[j][0]:
			for e in range(len(a)):
				if cards[i][0] == a[e] or cards[i][0:2] == a[e]:
					key = cards[i] + cards[j]
					ranking[key] = e
					break
					
for i in range(len(a)):
	for j in range(i + 1,len(a)):
		for f in range(len(cards)):
			for s in range(len(cards)):
				if not cards[f][0] == cards[s][0]:
					if cards[f][0] == a[i] or cards[f][0:2] == a[i]:
						if cards[s][0] == a[j] or cards[s][0:2] == a[j]:
							key = cards[f] + cards[s]
							ranking[key] = value
		value = value + 1

					
			
				
	
for k,v in ranking.items():
	print(k,v)
	
print(len(ranking))
	
