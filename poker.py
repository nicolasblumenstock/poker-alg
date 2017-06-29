from collections import Counter

f = open('poker.txt', 'r')


hands = f.read().splitlines()

hands2 = []

for i in range(len(hands)):
	hands2.append(hands[i].split())

player1hand = []
player2hand = []

for j in range(len(hands2)):
	player1hand.append(hands2[j][:len(hands2[j])/2])
	player2hand.append(hands2[j][len(hands2[j])/2:])

def countDup(array,counter):
	for c in array:
		counter[c] += 1
	return dict(counter)

def pairs(count,array):
	for k,v in count.iteritems():
		if v > 1 and v > array[1]:
			del array[:]
			array.append(k)
			array.append(v)



def handsLoop(p1Hand,p2Hand):
	highDupP1 = [0,0];
	highDupP2 = [0,0];
	for i in range(len(p1Hand)):
		cntValP1 = Counter()
		cntValP2 = Counter()
		cntSuitP1 = Counter()
		cntSuitP2 = Counter()
		tempValP1 = []
		tempSuitP1 = []
		tempValP2 = []
		tempSuitP2 = []		
		for card in range(len(p1Hand[i])):
			for item in range(0, len(p1Hand[i][card]), 2):
				tempSuitP1.append(p1Hand[i][card][item +1])
				tempValP1.append(p1Hand[i][card][item])
				tempSuitP2.append(p2Hand[i][card][item +1])
				tempValP2.append(p2Hand[i][card][item])

		compValP1 = countDup(tempValP1,cntValP1)
		compValP2 = countDup(tempValP2,cntValP2)
		compSuitP1 = countDup(tempSuitP1,cntSuitP1)
		compSuitP2 = countDup(tempSuitP2,cntSuitP2)

        print compValP1
		# pairs(compValP1,highDupP1)
		# pairs(compValP2,highDupP2)

		# print highDupP1

handsLoop(player1hand,player2hand)


cardvalues = {
    "AD": 14,
    "KD": 13,
    "QD": 12,
    "JD": 11,
    "TD": 10,
    "9D": 9,
    "8D": 8,
    "7D": 7,
    "6D": 6,
    "5D": 5,
    "4D": 4,
    "3D": 3,
    "2D": 2,
    "AC": 14,
    "KC": 13,
    "QC": 12,
    "JC": 11,
    "TC": 10,
    "9C": 9,
    "8C": 8,
    "7C": 7,
    "6C": 6,
    "5C": 5,
    "4C": 4,
    "3C": 3,
    "2C": 2,
    "AS": 14,
    "KS": 13,
    "QS": 12,
    "JS": 11,
    "TS": 10,
    "9S": 9,
    "8S": 8,
    "7S": 7,
    "6S": 6,
    "5S": 5,
    "4S": 4,
    "3S": 3,
    "2S": 2,
    "AH": 14,
    "KH": 13,
    "QH": 12,
    "JH": 11,
    "TH": 10,
    "9H": 9,
    "8H": 8,
    "7H": 7,
    "6H": 6,
    "5H": 5,
    "4H": 4,
    "3H": 3,
    "2H": 2,
}



# for card in range(len(player1hand[5])):
# 	for item in range(0, len(player1hand[5][card]), 2):
# 		tempSuitP1.append(player1hand[5][card][item +1])
# 		tempValP1.append(player1hand[5][card][item])
# 		tempSuitP2.append(player2hand[5][card][item +1])
# 		tempValP2.append(player2hand[5][card][item])





			

