def checkcapture(keymoved,yn,pos,red,black,kingr,kingb,move,n):
	global x,y

	#If there is no king and human moves.
	if move == "Human" and kingb == [] and yn == False:
		#capture test case for black
		for j in range(len(black)):
			# print black
			test = black[j]
			xnot = test[0]
			ynot = test[1]
			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2
			yminus2 = int(ynot) -2
			yminus1 = int(ynot) - 1 
			
			case1 = str(xminus1)+str(yminus1)
			case2 = [xminus2,yminus2]
			case3 = str(xplus1)+str(yminus1)
			case4 = [xplus2,yminus2]

			if (case1 in red or case1 in kingr) and (case2 not in pos) and xminus1>=0 and yminus1>=0 and xminus2>=0 and yminus2>=0:
					return True
			elif (case3 in red or case3 in kingr) and (case4 not in pos) and xplus1<n and yminus1>=0 and xplus2<n and yminus2>=0: 
					return True

	#If there is no king and it's AI's turn.
	if move == "Computer" and kingr == [] and yn == False:
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
			
			#How is this structured?
			#(Box X)(Box Y) (taken or not taken)
			# (x)(y)(b) taken :  (x-1)(y+1)(b) and (x-2)(y+2)(empty)
			# (x)(y)(b) taken :  (x+1)(y+1)(b) and (x+2)(y+2)(empty)

			case1 = str(xminus1)+str(yplus1)
			case2 = [xminus2,yplus2]
			case3 = str(xplus1) + str(yplus1)
			case4 = [xplus2, yplus2]

			if (case1 in black or case1 in kingb) and (case2 not in pos) and xminus1>=0 and yplus1<n and xminus2>=0 and yplus2<n: 
					return True
			elif (case3 in black or case1 in kingb) and (case4 not in pos) and xplus1<n and yplus1<n and xplus2<n and yplus2<n: 
					return True

	#If it's human's turn and there is atleast one king.
	if move == "Human" and kingb != [] and yn == False:
		#capture test case for black
		for j in range(len(black)):
			# print black
			test = black[j]
			xnot = test[0]
			ynot = test[1]

			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2
			yminus2 = int(ynot) -2
			yminus1 = int(ynot) - 1 

			case1 = str(xminus1)+str(yminus1)
			case2 = [xminus2,yminus2]
			case3 = str(xplus1)+str(yminus1)
			case4 = [xplus2,yminus2]

			if (case1 in red or case1 in kingr) and (case2 not in pos) and xminus1>=0 and yminus1>=0 and xminus2>=0 and yminus2>=0:
					return True
			elif (case3 in red or case3 in kingr) and (case4 not in pos) and xplus1<n and yminus1>=0 and xplus2<n and yminus2>=0: 
					return True

		#(x)(y)(b) taken :  (x-1)(y-1)(r) and (x-2)(y-2)(empty)
		#(x)(y)(b) taken :  (x+1)(y-1)(r) and (x+2)(y-2)(empty)
		#(x)(y)(b) taken :  (x-1)(y+1)(r) and (x+2)(y+2)(empty)
		#(x)(y)(b) taken :  (x+1)(y+1)(r) and (x+2)(y+2)(empty)

		#Capture test cases for black king.
		for j in range(len(kingb)):
			# print black
			test = kingb[j]
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

			if (case1 in red or case1 in kingr) and (case2 not in pos) and xminus1>=0 and yminus1>=0 and xminus2>=0 and yminus2>=0:					
					return True
			elif (case3 in red or case3 in kingr) and (case4 not in pos) and xplus1<n and yminus1>=0 and xplus2<n and yminus2>=0: 
					return True
			elif (case5 in red or case5 in kingr) and (case6 not in pos) and xminus1>=0 and yplus1<n and xminus2>=0 and yplus2<n: 
					return True
			elif (case7 in red or case7 in kingr) and (case8 not in pos) and xplus1<n and yplus1<n and xplus2<n and yplus2<n: 
					return True

	#If it's the computer's turn and there are no kings.
	if move == "Computer" and kingr != [] and yn == False:
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

			case1 = str(xminus1)+str(yplus1)
			case2 = [xminus2,yplus2]
			case3 = str(xplus1) + str(yplus1)
			case4 = [xplus2, yplus2]

			if (case1 in black or case1 in kingb) and (case2 not in pos) and xminus1>=0 and yplus1<n and xminus2>=0 and yplus2<n: 
					return True
			elif (case3 in black or case3 in kingb) and (case4 not in pos) and xplus1<n and yplus1<n and xplus2<n and yplus2<n: 
					return True

		#Test cases.
		#(x)(y)(b) taken :  (x-1)(y-1)(r) and (x-2)(y-2)(empty)
		#(x)(y)(b) taken :  (x+1)(y-1)(r) and (x+2)(y-2)(empty)
		#(x)(y)(b) taken :  (x-1)(y+1)(r) and (x+2)(y+2)(empty)
		#(x)(y)(b) taken :  (x+1)(y+1)(r) and (x+2)(y+2)(empty)


		for j in range(len(kingr)):
			# print black
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

			if (case1 in black or case1 in kingb) and (case2 not in pos) and xminus1>=0 and yminus1>=0 and xminus2>=0 and yminus2>=0:
					return True
			elif (case3 in black or case3 in kingb) and (case4 not in pos) and xplus1<n and yminus1>=0 and xplus2<n and yminus2>=0: 
					return True
			elif (case5 in black or case5 in kingb) and (case6 not in pos) and xminus1>=0 and yplus1<n and xminus2>=0 and yplus2<n: 
					return True
			elif (case7 in black or case7 in kingb) and (case8 not in pos) and xplus1<n and yplus1<n and xplus2<n and yplus2<n: 
					return True

	#If it's human's turn and after the first capture there can be another capture from that position.
	if move == "Human" and yn == True:
		#If a black piece is moved.
		if keymoved in black:
			test = keymoved
			xnot = test[0]
			ynot = test[1]


			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2
			yminus2 = int(ynot) -2
			yminus1 = int(ynot) - 1 

			case1 = str(xminus1)+str(yminus1)
			case2 = [xminus2,yminus2]
			case3 = str(xplus1)+str(yminus1)
			case4 = [xplus2,yminus2]

			if (case1 in red or case1 in kingr) and (case2 not in pos) and xminus1>=0 and yminus1>=0 and xminus2>=0 and yminus2>=0:
					return True
			elif (case3 in red or case3 in kingr) and (case4 not in pos) and xplus1<n and yminus1>=0 and xplus2<n and yminus2>=0: 
					return True

		#If a black king is moved.
		elif keymoved in kingb:
			test = keymoved
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

			if (case1 in red or case1 in kingr) and (case2 not in pos) and xminus1>=0 and yminus1>=0 and xminus2>=0 and yminus2>=0:
					return True
			elif (case3 in red or case3 in kingr) and (case4 not in pos) and xplus1<n and yminus1>=0 and xplus2<n and yminus2>=0: 
					return True
			elif (case5 in red or case5 in kingr) and (case6 not in pos) and xminus1>=0 and yplus1<n and xminus2>=0 and yplus2<n: 
					return True
			elif (case7 in red or case7 in kingr) and (case8 not in pos) and xplus1<n and yplus1<n and xplus2<n and yplus2<n: 
					return True
	if move == "Computer" and yn == True:
		if keymoved in red:
			test = keymoved
			xnot = test[0]
			ynot = test[1]



			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2

			yplus1 = int(ynot) +1 
			yplus2 = int(ynot) + 2

			boolcheck = xminus1>=0 and xminus2>=0 and xplus1<n and xplus2<n and yplus1<n and yplus2<n

			

			# (x)(y)(b) taken :  (x-1)(y+1)(b) and (x-2)(y+2)(empty)
			# (x)(y)(b) taken :  (x+1)(y+1)(b) and (x+2)(y+2)(empty)

			case1 = str(xminus1)+str(yplus1)
			case2 = [xminus2,yplus2]

			case3 = str(xplus1) + str(yplus1)
			case4 = [xplus2, yplus2]

			# boolcheck = intxminus1 >= 0 and intyminus1 >= 0 and intxplus1 < n and intyminus1 >= 0 and intxplus2 < n and intyminus2 >= 0


			# print case1 in positions, case2 not in box

			if (case1 in black or case1 in kingb) and (case2 not in pos) and xminus1>=0 and yplus1<n and xminus2>=0 and yplus2<n: 
					return True
			elif (case3 in black or case1 in kingb) and (case4 not in pos) and xplus1<n and yplus1<n and xplus2<n and yplus2<n: 
					return True

		elif keymoved in kingr:
			# print black
			test = keymoved
			xnot = test[0]
			ynot = test[1]

			# print x,y,c,t
			# print"xnot",xnot

			xminus1 = int(xnot) - 1
			xminus2 = int(xnot) - 2
			xplus1 = int(xnot) + 1 
			xplus2 = int(xnot) + 2

			yminus2 = int(ynot) -2
			yminus1 = int(ynot) - 1 
			yplus1 = int(ynot) + 1
			yplus2 = int(ynot) + 2

			boolcheck = xminus1>=0 and xminus2>=0 and xplus1<n and xplus2<n and yminus1>=0 and yminus2>=0
			

			case1 = str(xminus1)+str(yminus1)
			case2 = [xminus2,yminus2]

			case3 = str(xplus1)+str(yminus1)
			case4 = [xplus2,yminus2]

			case5 = str(xminus1)+str(yplus1)
			case6 = [xminus2,yplus2]

			case7 = str(xplus1) + str(yplus1)
			case8 = [xplus2, yplus2]

			# boolcheck = intxminus1 >= 0 and intyminus1 >= 0 and intxplus1 < n and intyminus1 >= 0 and intxplus2 < n and intyminus2 >= 0

	


			if (case1 in black or case1 in kingb) and (case2 not in pos) and xminus1>=0 and yminus1>=0 and xminus2>=0 and yminus2>=0:
	
					return True
			elif (case3 in black or case3 in kingb) and (case4 not in pos) and xplus1<n and yminus1>=0 and xplus2<n and yminus2>=0: 
				
					return True

			elif (case5 in black or case5 in kingb) and (case6 not in pos) and xminus1>=0 and yplus1<n and xminus2>=0 and yplus2<n: 
					return True
			elif (case7 in black or case7 in kingb) and (case8 not in pos) and xplus1<n and yplus1<n and xplus2<n and yplus2<n: 
					return True
	return False








