cards = []
x = ['J','Q','K','A']
type = ['H','S','C','D']
for i in range(2,11):
	for j in type:
		cards.append(str(i) + j)
for i in x:
        for j in type:             
                cards.append(i + j)
                
cardsPy = []
                
for i in range(len(cards)):
	for j in range(i + 1, len(cards)):
		cardsPy.append(cards[i] + cards[j])
		
for e in cardsPy:
	print(e)	
print(len(cardsPy))


