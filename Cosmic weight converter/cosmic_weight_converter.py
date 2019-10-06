# ©Compiler's Bro , don't be scared it's just a symbol !!☺!!  
#check for a valid user name !!
print(" \n $$$$$$$$$$$$$$$$$$$ Welocome to Cosmic Weight Converter $$$$$$$$$$$$$$$$$$$$ \n")
name = str(input("Please enter your name !!! \n"))
if len(name) < 2:
   print(" Please enter a valid name !! \n")
elif len(name) > 50 :
    print("Your name is pretty long !! \n")
else:
    print(f"{name} , that's a nice name !! \n")

#ask for the user weight in Kgs
user_weight = int(input(f"Hey , {name} , can you please tell me your weight in Kilograms ?? \n"))
print(f"So you weigh {user_weight}Kg , that's nice \n")
#ask for user inputs to compute the calculations and display the messeges !!!
user_input = input(''' Where on Universe do you like to find your weight ?\n
01. If (M)oon ----> press "M"
02. If (Me)rcury ----> press "ME"
03. If (V)enus ----> press "V"
04. If (E)arth ----> press "E"
05. If (Ma)rs -----> press "MA"
06. If (J)upiter -----> press "J"
07. If (S)aturn ----> press "S"
08. If (U)ranus ----> press "U"
09. If (N)eptune -----> press "N" 
10. To (Q)uit ----> press "Q" \n \n ''')

#Computaions !!!!

if user_input.upper() == "M":
    moon_weight = round(user_weight//9.8) * 1.622
    print(f"Hey {name} , you weigh {moon_weight} luna on moon !!! \n")
elif user_input.upper() == "ME":
    mercury_weight = round(user_weight//9.8)*3.7
    print(f"Hey {name} , you weigh {mercury_weight} Kg on Mercury \n")
elif user_input.upper() == "V":
    venus_weight = round(user_weight//9.8)*8.87
    print(f"Hey {name} , you weigh {venus_weight} Kg on Venus \n")
elif user_input.upper() == "E":
    print(f"You think I'm a fool !!! , {user_weight} Kg you'r too heavy for Earth !!!\n")
elif user_input.upper() == "MA":
    mars_mass = round(user_weight//9.8)*3.711
    print(f" Hey {name} , you weigh {mars_mass} marshian on Mars !! \n")
elif user_input.upper() == "J":
    jy_mass = round(user_weight//9.8)*24.79
    print(f"Hey {name} , you weigh {jy_mass} Kg on Jupiter \n")
elif user_input.upper() == "S" :
    sat_mass = round(user_weight//9.8)*10.44
    print(f"Hey {name} , you have {sat_mass} rings on Saturn !!! \n")
elif user_input.upper() == "U":
    uran_mass = round(user_weight//9.8)*8.87
    print(f" Hey {name} , you weigh {uran_mass} Kg on Uranus !!! \n")
elif user_input.upper() == "N":
    net_mass = round(user_weight//9.8)*11.15
    print(f" Hey {name} , you weigh {net_mass} Kg on Neptune !! \n")
elif user_input.upper() == "Q":
    print(f"Be carefull you may enconuter an Alien.............. bye....bye !!! \n")
else:
    print("Ohh no , I'm sorry you are sucked up by a 'BLACK HOLE' !!!!! \n")
#end of computing
#Thank you for coping our code , hope you add some more functions !!! 