attend = ["omar",'ahmed','mohmed']
for person in attend :
  print(person)
  ask = input(f"Are {person} attendded today ?").upper()
  if ask == "YES" :
    print(f"{person} attended today" )
  else :
    print(f"{person} donot attended today ")

people_attended = input("Enter names for people attened ? (sepratoed by comma) :")
confirm = people_attended.split(",")
for person in confirm :
  print("\n" + person + "\n")
  ask = input(f"are this {person} attended ?").lower()
  if ask == "yes" :
    print(f"this {person} attended ")
  elif ask == "no" :
    print(f"this {person} not attended ")
  else : 
    print(f"yoour input is {ask}  not correct")
