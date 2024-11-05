atm=int(input("enter your amout:"))

note1=atm//100
note2=(atm%100)//50
note3=((atm%100)%50)//10
print("note of hundred rupee:",note1)
print("note of 50 rupee:",note2)
print("note of 10 rupee:",note3)