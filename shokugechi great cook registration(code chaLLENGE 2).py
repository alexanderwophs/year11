print("""Hi, welcome to shokugechki no souma, great cook.
the only cooking mmorpg in existstance!""")
name=str(input("enter your name to continue.;D "))
age=int(input("enter your actual age, there are profanity filters and people will be placed in servers based on age like 14-18"))
last_name=str(input("enter last name"))
e_Mail=str(input("enter ya email"))
correct= input("is this correct?y or n this is caps sensitive")
if correct == "y":
  print("this is you.")
  print(name)
  print(last_name)
  print(age)
  print("Have fun")
else:
  name=str(input("first name"))
  last_name=str(input("last_name"))
  age=int(input("age"))
  e_Mail=str(input("eMail"))
  correct=str(input("it this correct? y for correct any other letter for no including capital Y or words."))
  if correct != "y":
      name=str(input("first name"))
      last_name=str(input("last_name"))
      age=int(input("age"))
      e_Mail=str(input("eMail"))
      correct=str(input("it this correct? y for correct any other letter for no including capital Y or words."))
      
