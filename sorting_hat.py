gryffindor = 0 
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Q1) Do you like Dawn or Dusk?")
print("  1) Dawn")
print("  2) Dusk")
q1 = int(input("Enter your answer 1 or 2:  "))
  
if q1 == 1:
  gryffindor += 1
  ravenclaw += 1
elif q1 == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print("Wrong input.")



print("Q2) When I'm dead, i want people to remember me as:")
print("  1) The Good")
print("  2) The Great")
print("  3) The Wise")
print("  4) The Bold")
q2 = int(input("Enter your answer 1-4: "))

if q2 == 1:
  hufflepuff += 2
elif q2 == 2:
  slytherin += 2
elif q2 == 3:
  ravenclaw += 2
elif q2 == 4:
  gryffindor +=2
else:
  print("Wrong input.")



print("Q3) Which kind of instrument most pleases your ear?")
print("  1) The violin")
print("  2) The trumpet")
print("  3) The piano")
print("  4) The drum")
q3 = int(input("Enter your answer 1-4: "))

if q3 == 1:
  slytherin += 4
elif q3 == 2:
  hufflepuff += 4
elif q3 == 3:
  ravenclaw += 4
elif q3 == 4:
  gryffindor += 4
else:
  print("Wrong input.")

print(f"Gryffindor score: {gryffindor}")
print(f"Ravenclaw score: {ravenclaw}")
print(f"Hufflepuff score: {hufflepuff}")
print(f"Slytherin score: {slytherin}")

if gryffindor > ravenclaw and gryffindor > hufflepuff  and gryffindor > slytherin:
  print(f"Gryffindor won with {gryffindor} points.")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff  and ravenclaw > slytherin:
  print(f"Ravenclaw won with {ravenclaw} points.")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw  and hufflepuff > slytherin:
  print(f"Hufflepuff won with {hufflepuff} points.")  
elif slytherin > gryffindor and slytherin > hufflepuff  and slytherin > ravenclaw:
  print(f"Slytherin won with {slytherin} points.")
