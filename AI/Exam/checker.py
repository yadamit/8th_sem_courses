from answers import *

if NAME == "YOUR NAME HERE!!!":
  print ("MUST RECORD NAME!")
  exit()
if STUDENTID == "YOUR ID HERE!!!":
  print ("MUST RECORD STUDENT ID!")
  exit()
if LOCATION == "YOUR LOCATION HERE!!!":
  print ("MUST RECORD LOCATION!")
  exit()
# EXERCISE 1

if not isinstance(answer1,str):
  print ("Type error in Exercise 1: Must be string (answer1)")
  exit()


# EXERCISE 2

if not isinstance(answer2,tuple):
  print ("Type error in Exercise 2: Must be tuple ( , , , , ) (answer2)")
  exit()


if len(answer2) != 5:
  print ("Type error in Exercise 2: Tuple must have 5 elements (answer2)")
  exit()


answer2_0 = answer2[0]
if answer2_0 != True and answer2_0 != False and answer2_0 != DontKnow:
  print ("Type error in Exercise 2: Must be True, False or DontKnow (answer2_0)")
  exit()


answer2_1 = answer2[1]
if answer2_1 != True and answer2_1 != False and answer2_1 != DontKnow:
  print ("Type error in Exercise 2: Must be True, False or DontKnow (answer2_1)")
  exit()


answer2_2 = answer2[2]
if answer2_2 != True and answer2_2 != False and answer2_2 != DontKnow:
  print ("Type error in Exercise 2: Must be True, False or DontKnow (answer2_2)")
  exit()


answer2_3 = answer2[3]
if answer2_3 != True and answer2_3 != False and answer2_3 != DontKnow:
  print ("Type error in Exercise 2: Must be True, False or DontKnow (answer2_3)")
  exit()


answer2_4 = answer2[4]
if answer2_4 != True and answer2_4 != False and answer2_4 != DontKnow:
  print ("Type error in Exercise 2: Must be True, False or DontKnow (answer2_4)")
  exit()


# EXERCISE 3

if not isinstance(answer3,tuple):
  print ("Type error in Exercise 3: Must be tuple ( , , , ) (answer3)")
  exit()


if len(answer3) != 4:
  print ("Type error in Exercise 3: Tuple must have 4 elements (answer3)")
  exit()


answer3_0 = answer3[0]
if not isinstance(answer3_0,int):
  print ("Type error in Exercise 3: Must be integer (answer3_0)")
  exit()


answer3_1 = answer3[1]
if not isinstance(answer3_1,int):
  print ("Type error in Exercise 3: Must be integer (answer3_1)")
  exit()


answer3_2 = answer3[2]
if not isinstance(answer3_2,int):
  print ("Type error in Exercise 3: Must be integer (answer3_2)")
  exit()


answer3_3 = answer3[3]
if not isinstance(answer3_3,int):
  print ("Type error in Exercise 3: Must be integer (answer3_3)")
  exit()


# EXERCISE 4

if not isinstance(answer4,tuple):
  print ("Type error in Exercise 4: Must be tuple ( , , ) (answer4)")
  exit()


if len(answer4) != 3:
  print ("Type error in Exercise 4: Tuple must have 3 elements (answer4)")
  exit()


answer4_0 = answer4[0]
if not isinstance(answer4_0,tuple):
  print ("Type error in Exercise 4: Must be tuple ( , ) (answer4_0)")
  exit()


if len(answer4_0) != 2:
  print ("Type error in Exercise 4: Tuple must have 2 elements (answer4_0)")
  exit()


answer4_0_0 = answer4_0[0]
if not isinstance(answer4_0_0,(float,int)):
  print ("Type error in Exercise 4: Must be numeric value (answer4_0_0)")
  exit()


answer4_0_1 = answer4_0[1]
if not isinstance(answer4_0_1,(float,int)):
  print ("Type error in Exercise 4: Must be numeric value (answer4_0_1)")
  exit()


answer4_1 = answer4[1]
if not isinstance(answer4_1,tuple):
  print ("Type error in Exercise 4: Must be tuple ( , ) (answer4_1)")
  exit()


if len(answer4_1) != 2:
  print ("Type error in Exercise 4: Tuple must have 2 elements (answer4_1)")
  exit()


answer4_1_0 = answer4_1[0]
if not isinstance(answer4_1_0,(float,int)):
  print ("Type error in Exercise 4: Must be numeric value (answer4_1_0)")
  exit()


answer4_1_1 = answer4_1[1]
if not isinstance(answer4_1_1,(float,int)):
  print ("Type error in Exercise 4: Must be numeric value (answer4_1_1)")
  exit()


answer4_2 = answer4[2]
if not isinstance(answer4_2,tuple):
  print ("Type error in Exercise 4: Must be tuple ( , ) (answer4_2)")
  exit()


if len(answer4_2) != 2:
  print ("Type error in Exercise 4: Tuple must have 2 elements (answer4_2)")
  exit()


answer4_2_0 = answer4_2[0]
if not isinstance(answer4_2_0,(float,int)):
  print ("Type error in Exercise 4: Must be numeric value (answer4_2_0)")
  exit()


answer4_2_1 = answer4_2[1]
if not isinstance(answer4_2_1,(float,int)):
  print ("Type error in Exercise 4: Must be numeric value (answer4_2_1)")
  exit()


# EXERCISE 5

if not isinstance(answer5,tuple):
  print ("Type error in Exercise 5: Must be tuple ( , ) (answer5)")
  exit()


if len(answer5) != 2:
  print ("Type error in Exercise 5: Tuple must have 2 elements (answer5)")
  exit()


answer5_0 = answer5[0]
if not isinstance(answer5_0,(float,int)):
  print ("Type error in Exercise 5: Must be numeric value (answer5_0)")
  exit()


answer5_1 = answer5[1]
if not isinstance(answer5_1,(float,int)):
  print ("Type error in Exercise 5: Must be numeric value (answer5_1)")
  exit()


# EXERCISE 6

if not isinstance(answer6,tuple):
  print ("Type error in Exercise 6: Must be tuple ( , , , ) (answer6)")
  exit()


if len(answer6) != 4:
  print ("Type error in Exercise 6: Tuple must have 4 elements (answer6)")
  exit()


answer6_0 = answer6[0]
if not isinstance(answer6_0,(float,int)):
  print ("Type error in Exercise 6: Must be numeric value (answer6_0)")
  exit()


answer6_1 = answer6[1]
if not isinstance(answer6_1,(float,int)):
  print ("Type error in Exercise 6: Must be numeric value (answer6_1)")
  exit()


answer6_2 = answer6[2]
if not isinstance(answer6_2,(float,int)):
  print ("Type error in Exercise 6: Must be numeric value (answer6_2)")
  exit()


answer6_3 = answer6[3]
if not isinstance(answer6_3,(float,int)):
  print ("Type error in Exercise 6: Must be numeric value (answer6_3)")
  exit()


# EXERCISE 7

if not isinstance(answer7,tuple):
  print ("Type error in Exercise 7: Must be tuple ( , , , , ) (answer7)")
  exit()


if len(answer7) != 5:
  print ("Type error in Exercise 7: Tuple must have 5 elements (answer7)")
  exit()


answer7_0 = answer7[0]
if not isinstance(answer7_0,(float,int)):
  print ("Type error in Exercise 7: Must be numeric value (answer7_0)")
  exit()


answer7_1 = answer7[1]
if not isinstance(answer7_1,(float,int)):
  print ("Type error in Exercise 7: Must be numeric value (answer7_1)")
  exit()


answer7_2 = answer7[2]
if not isinstance(answer7_2,(float,int)):
  print ("Type error in Exercise 7: Must be numeric value (answer7_2)")
  exit()


answer7_3 = answer7[3]
if not isinstance(answer7_3,(float,int)):
  print ("Type error in Exercise 7: Must be numeric value (answer7_3)")
  exit()


answer7_4 = answer7[4]
if not isinstance(answer7_4,(float,int)):
  print ("Type error in Exercise 7: Must be numeric value (answer7_4)")
  exit()


# EXERCISE 8

if not isinstance(answer8,tuple):
  print ("Type error in Exercise 8: Must be tuple ( , , , ) (answer8)")
  exit()


if len(answer8) != 4:
  print ("Type error in Exercise 8: Tuple must have 4 elements (answer8)")
  exit()


answer8_0 = answer8[0]
if answer8_0 != True and answer8_0 != False and answer8_0 != DontKnow:
  print ("Type error in Exercise 8: Must be True, False or DontKnow (answer8_0)")
  exit()


answer8_1 = answer8[1]
if answer8_1 != True and answer8_1 != False and answer8_1 != DontKnow:
  print ("Type error in Exercise 8: Must be True, False or DontKnow (answer8_1)")
  exit()


answer8_2 = answer8[2]
if answer8_2 != True and answer8_2 != False and answer8_2 != DontKnow:
  print ("Type error in Exercise 8: Must be True, False or DontKnow (answer8_2)")
  exit()


answer8_3 = answer8[3]
if answer8_3 != True and answer8_3 != False and answer8_3 != DontKnow:
  print ("Type error in Exercise 8: Must be True, False or DontKnow (answer8_3)")
  exit()

print ("ANSWER FILE PASSED TYPE-CHECKING")
