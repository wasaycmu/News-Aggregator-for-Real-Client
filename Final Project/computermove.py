'ARTIFICIAL INTELLIGENCE'

import random


def checkcapture(keymoved,yn,pos,red,black,kingr,kingb,move,n):
	global x,y
	#INTELLIGENT MOVES
	if move == "Computer" and yn == False:
		#capture test case for black
		for j in range(len(red)):
			test = red[j]
			xnot = test[0]
			ynot = test[1]


			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2

			yplus1 = int(ynot) +1 
			yplus2 = int(ynot) + 2


			

			# (x)(y)(b) taken :  (x-1)(y+1)(b) and (x-2)(y+2)(empty)
			# (x)(y)(b) taken :  (x+1)(y+1)(b) and (x+2)(y+2)(empty)
			casenot = str(xnot)+str(ynot)

			case1 = str(xminus1)+str(yplus1)
			case2 = [xminus2,yplus2]

			case3 = str(xplus1) + str(yplus1)
			case4 = [xplus2, yplus2]

			# boolcheck = intxminus1 >= 0 and intyminus1 >= 0 and intxplus1 < n and intyminus1 >= 0 and intxplus2 < n and intyminus2 >= 0



			if (case1 in black or case1 in kingb) and (case2 not in pos) and xminus1>=0 and yplus1<8 and xminus2>=0 and yplus2<8: 
					return casenot+str(case2[0])+str(case2[1])
			elif (case3 in black or case1 in kingb) and (case4 not in pos) and xplus1<8 and yplus1<8 and xplus2<8 and yplus2<8: 
					return casenot+str(case4[0])+str(case4[1])
	'Level 1'
	if move == "Computer" and yn == False:
		#capture test case for black
		for j in range(len(red)):
			test = red[j]
			xnot = test[0]
			ynot = test[1]



			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2

			yplus1 = int(ynot) +1 
			yplus2 = int(ynot) + 2


			

			# (x)(y)(b) taken :  (x-1)(y+1)(b) and (x-2)(y+2)(empty)
			# (x)(y)(b) taken :  (x+1)(y+1)(b) and (x+2)(y+2)(empty)

			casenot = str(xnot)+str(ynot)

			case1 = str(xminus1)+str(yplus1)
			case2 = [xminus2,yplus2]

			case3 = str(xplus1) + str(yplus1)
			case4 = [xplus2, yplus2]

			# boolcheck = intxminus1 >= 0 and intyminus1 >= 0 and intxplus1 < n and intyminus1 >= 0 and intxplus2 < n and intyminus2 >= 0



			if (case1 in black or case1 in kingb) and (case2 not in pos) and xminus1>=0 and yplus1<8 and xminus2>=0 and yplus2<8: 
					return casenot+str(case2[0])+str(case2[1])
			elif (case3 in black or case3 in kingb) and (case4 not in pos) and xplus1<8 and yplus1<8 and xplus2<8 and yplus2<8: 
					return casenot+str(case4[0])+str(case4[1])

		#(x)(y)(b) taken :  (x-1)(y-1)(r) and (x-2)(y-2)(empty)
		#(x)(y)(b) taken :  (x+1)(y-1)(r) and (x+2)(y-2)(empty)
		#(x)(y)(b) taken :  (x-1)(y+1)(r) and (x+2)(y+2)(empty)
		#(x)(y)(b) taken :  (x+1)(y+1)(r) and (x+2)(y+2)(empty)


		for j in range(len(kingr)):
			test = kingr[j]
			xnot = test[0]
			ynot = test[1]


			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2

			yminus2 = int(ynot) -2
			yminus1 = int(ynot) - 1 
			yplus1 = int(ynot) + 1
			yplus2 = int(ynot) + 2

			

			case1 = str(xminus1)+str(yminus1)
			case2 = [xminus2,yminus2]

			case3 = str(xplus1)+str(yminus1)
			case4 = [xplus2,yminus2]

			case5 = str(xminus1)+str(yplus1)
			case6 = [xminus2,yplus2]

			case7 = str(xplus1) + str(yplus1)
			case8 = [xplus2, yplus2]

			casenot = str(xnot)+str(ynot)

			# boolcheck = intxminus1 >= 0 and intyminus1 >= 0 and intxplus1 < n and intyminus1 >= 0 and intxplus2 < n and intyminus2 >= 0




			if (case1 in black or case1 in kingb) and (case2 not in pos) and xminus1>=0 and yminus1>=0 and xminus2>=0 and yminus2>=0:

					return casenot+str(case2[0])+str(case2[1])
			elif (case3 in black or case3 in kingb) and (case4 not in pos) and xplus1<8 and yminus1>=0 and xplus2<8 and yminus2>=0: 

					return casenot+str(case4[0])+str(case4[1])

			elif (case5 in black or case5 in kingb) and (case6 not in pos) and xminus1>=0 and yplus1<8 and xminus2>=0 and yplus2<8: 

					return casenot+str(case6[0])+str(case6[1])
			elif (case7 in black or case7 in kingb) and (case8 not in pos) and xplus1<8 and yplus1<8 and xplus2<8 and yplus2<8: 

					return casenot+str(case8[0])+str(case8[1])
	'Level 2'
	#Compulsory Normal Move and King Capture
	if move == "Computer" and kingr == [] and yn== True:
		#capture test case for black
		for j in range(len(red)):
			test = red[j]
			xnot = test[0]
			ynot = test[1]


			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2

			yplus1 = int(ynot) +1 
			yplus2 = int(ynot) + 2


			

			# (x)(y)(b) taken :  (x-1)(y+1)(b) and (x-2)(y+2)(empty)
			# (x)(y)(b) taken :  (x+1)(y+1)(b) and (x+2)(y+2)(empty)
			casenot = str(xnot)+str(ynot)

			case1 = str(xminus1)+str(yplus1)
			case2 = [xminus2,yplus2]

			case3 = str(xplus1) + str(yplus1)
			case4 = [xplus2, yplus2]

			# boolcheck = intxminus1 >= 0 and intyminus1 >= 0 and intxplus1 < n and intyminus1 >= 0 and intxplus2 < n and intyminus2 >= 0



			if (case1 in black or case1 in kingb) and (case2 not in pos) and xminus1>=0 and yplus1<8 and xminus2>=0 and yplus2<8: 
					return casenot+str(case2[0])+str(case2[1])
			elif (case3 in black or case1 in kingb) and (case4 not in pos) and xplus1<8 and yplus1<8 and xplus2<8 and yplus2<8: 
					return casenot+str(case4[0])+str(case4[1])
	'Level 3'
	if move == "Computer" and kingr != [] and yn==True:
		#capture test case for black
		for j in range(len(red)):
			test = red[j]
			xnot = test[0]
			ynot = test[1]



			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2

			yplus1 = int(ynot) +1 
			yplus2 = int(ynot) + 2


			

			# (x)(y)(b) taken :  (x-1)(y+1)(b) and (x-2)(y+2)(empty)
			# (x)(y)(b) taken :  (x+1)(y+1)(b) and (x+2)(y+2)(empty)

			casenot = str(xnot)+str(ynot)

			case1 = str(xminus1)+str(yplus1)
			case2 = [xminus2,yplus2]

			case3 = str(xplus1) + str(yplus1)
			case4 = [xplus2, yplus2]

			# boolcheck = intxminus1 >= 0 and intyminus1 >= 0 and intxplus1 < n and intyminus1 >= 0 and intxplus2 < n and intyminus2 >= 0



			if (case1 in black or case1 in kingb) and (case2 not in pos) and xminus1>=0 and yplus1<8 and xminus2>=0 and yplus2<8: 
					return casenot+str(case2[0])+str(case2[1])
			elif (case3 in black or case3 in kingb) and (case4 not in pos) and xplus1<8 and yplus1<8 and xplus2<8 and yplus2<8: 
					return casenot+str(case4[0])+str(case4[1])

		#(x)(y)(b) taken :  (x-1)(y-1)(r) and (x-2)(y-2)(empty)
		#(x)(y)(b) taken :  (x+1)(y-1)(r) and (x+2)(y-2)(empty)
		#(x)(y)(b) taken :  (x-1)(y+1)(r) and (x+2)(y+2)(empty)
		#(x)(y)(b) taken :  (x+1)(y+1)(r) and (x+2)(y+2)(empty)


		for j in range(len(kingr)):
			test = kingr[j]
			xnot = test[0]
			ynot = test[1]



			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2

			yminus2 = int(ynot) -2
			yminus1 = int(ynot) - 1 
			yplus1 = int(ynot) + 1
			yplus2 = int(ynot) + 2

			

			case1 = str(xminus1)+str(yminus1)
			case2 = [xminus2,yminus2]

			case3 = str(xplus1)+str(yminus1)
			case4 = [xplus2,yminus2]

			case5 = str(xminus1)+str(yplus1)
			case6 = [xminus2,yplus2]

			case7 = str(xplus1) + str(yplus1)
			case8 = [xplus2, yplus2]

			casenot = str(xnot)+str(ynot)

			# boolcheck = intxminus1 >= 0 and intyminus1 >= 0 and intxplus1 < n and intyminus1 >= 0 and intxplus2 < n and intyminus2 >= 0




			if (case1 in black or case1 in kingb) and (case2 not in pos) and xminus1>=0 and yminus1>=0 and xminus2>=0 and yminus2>=0:

					return casenot+str(case2[0])+str(case2[1])
			elif (case3 in black or case3 in kingb) and (case4 not in pos) and xplus1<8 and yminus1>=0 and xplus2<8 and yminus2>=0: 

					return casenot+str(case4[0])+str(case4[1])

			elif (case5 in black or case5 in kingb) and (case6 not in pos) and xminus1>=0 and yplus1<8 and xminus2>=0 and yplus2<8: 

					return casenot+str(case6[0])+str(case6[1])
			elif (case7 in black or case7 in kingb) and (case8 not in pos) and xplus1<8 and yplus1<8 and xplus2<8 and yplus2<8: 

					return casenot+str(case8[0])+str(case8[1])
	'Level 4'
	#RANDOM VALID MOVES AND NO KINGS.
	if move == "Computer" and kingr == []:
		#capture test case for black
		for j in range(len(red)):
			n = random.randrange(0,len(red))
			# print "RANDOM NUMBER",n
			# print red
			test = red[n]
			xnot = test[0]
			ynot = test[1]



			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2

			yplus1 = int(ynot) +1 
			yplus2 = int(ynot) + 2


			

			# (x)(y)(b) taken :  (x-1)(y+1)(b) and (x-2)(y+2)(empty)
			# (x)(y)(b) taken :  (x+1)(y+1)(b) and (x+2)(y+2)(empty)

			casenot = str(xnot)+str(ynot)
			case2 = [xminus1,yplus1]


			case4 = [xplus1,yplus1]
			# boolcheck = intxminus1 >= 0 and intyminus1 >= 0 and intxplus1 < n and intyminus1 >= 0 and intxplus2 < n and intyminus2 >= 0


			if (case2 not in pos) and xminus1>=0 and yplus1<8: 

					return casenot+str(case2[0])+str(case2[1])
			elif (case4 not in pos) and xplus1<8 and yplus1<8: 

					return casenot+str(case4[0])+str(case4[1])

		#MOVE WHEN THERE IS A KING AND THERE IS NO INTELLIGENT MOVE AND THE OPPONENT HAS A KING.
	'Level 5'
	#Random Move.
	if move == "Computer":
		#king preference to Move
		for j in range(len(kingr)):
			if len(kingr) == 1:
				n = 0
			else:
				n = random.randrange(0,len(red))
			test = kingr[n]
			xnot = test[0]
			ynot = test[1]

			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2

			yminus2 = int(ynot) -2
			yminus1 = int(ynot) - 1 
			yplus1 = int(ynot) + 1
			yplus2 = int(ynot) + 2

			boolcheck = xminus1>=0 and xminus2>=0 and xplus1<8 and xplus2<8 and yminus1>=0 and yminus2>=0
			
			casenot = str(xnot)+str(ynot)

			case1 = str(xminus1)+str(yminus1)
			case2 = [xminus1,yminus1]

			case3 = str(xplus1)+str(yminus1)
			case4 = [xplus1,yminus1]

			case5 = str(xminus1)+str(yplus1)
			case6 = [xminus1,yplus1]

			case7 = str(xplus1) + str(yplus1)
			case8 = [xplus1, yplus1]

			# boolcheck = intxminus1 >= 0 and intyminus1 >= 0 and intxplus1 < n and intyminus1 >= 0 and intxplus2 < n and intyminus2 >= 0




			if (case2 not in pos) and xminus1>=0 and yminus1>=0 and xminus2>=0 and yminus2>=0:
					return casenot+str(case2[0])+str(case2[1])
			elif (case4 not in pos) and xplus1<8 and yminus1>=0 and xplus2<8 and yminus2>=0: 
					return casenot+str(case4[0])+str(case4[1])
			elif (case6 not in pos) and xminus1>=0 and yplus1<8 and xminus2>=0 and yplus2<8: 
					return casenot+str(case6[0])+str(case6[1])
			elif (case8 not in pos) and xplus1<8 and yplus1<8 and xplus2<8 and yplus2<8: 
					return casenot+str(case8[0])+str(case8[1])

		#Normal piece
		for j in range(len(red)):
			test = red[j]
			xnot = test[0]
			ynot = test[1]



			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2

			yplus1 = int(ynot) +1 
			yplus2 = int(ynot) + 2


			

			# (x)(y)(b) taken :  (x-1)(y+1)(b) and (x-2)(y+2)(empty)
			# (x)(y)(b) taken :  (x+1)(y+1)(b) and (x+2)(y+2)(empty)

			case1 = str(xminus1)+str(yplus1)
			case2 = [xminus1,yplus1]

			case3 = str(xplus1) + str(yplus1)
			case4 = [xplus1, yplus1]

			casenot = str(xnot)+str(ynot)


			if (case2 not in pos) and xminus1>=0 and yplus1<8 and xminus2>=0 and yplus2<8: 
					return casenot+str(case2[0])+str(case2[1])

			elif (case4 not in pos) and xplus1<8 and yplus1<8 and xplus2<8 and yplus2<8: 
					return casenot+str(case4[0])+str(case4[1])
	'Level 7'
	#The most powerful opening move.
	return "random3243"






