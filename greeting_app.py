# This program will ask your name and age and it will greet you!
# It will greet and treat you with different compliments!
# Plus, it will calculate your birthday year too!
# If you have my name and my age you will be DEAD!
# If you don't leave we don't care. YOU HAVE TO!
# And there is no room for clowns here...

import random

compliments = ["What a beautiful name!", 
               "Your name is artistic!", 
               "That name belongs in a museum!", 
               "Ohhh, your parents must be artists!"]

all_noble_users = []

user_counter = 0

while True:
    
    print("Hello, buddy! Welcome to my program!")
    
    my_name = input("What is your name, sweetheart?\n")
    
    if my_name.lower() == 'ehsan':
        
        print("HEY! That's MY name! I'll call 911, RIGHT NOW!")
        print("Okay... Whatever!")
        print("It's NOt a beautiful name AT ALL FOR YOU!")
        
        my_age2 = int(input(f"Okay... My fake version... How old are you? (IT'S NOT LIKE I DO CARE!)\n"))
        
        if my_age2 == 17:
            
            print("WHAT THE F...K!")
            print("YOU ARE A THIEF!!! A TERRIBLE ONE!")
            
        else:
            
            birthday_year2 = 2026 - my_age2
            
            print(f"Well, FUN FACT! Your birthday year is {birthday_year2}")
            print("BUT YOU WILL DIE SOOOOOON!")
            
        exit_program = input("Don't you want to leave me alone?")        
        if exit_program.lower() == 'no':              
            print("HEHE, It's MY program! I have power here!")
            print("BYE BYE, STICKY COCKROACH!")            
            break        
        elif exit_program.lower() == 'yes':            
            print("Good boy... GET OUT!")           
            break
        else:
            print("😒😒")
            break
        
    while my_name.isdigit():
        
        print("ATTENSTION: If you can't read correctly, we can pay for your LITERACY!")
        
        my_name2 = input("HAHA... write your realname, CLOWN!\n")
        
        if my_name2.isdigit():
            print("A sick clown will never be fixed...")
            continue
        else:
            print("Good Clown!")
            
            my_age3 = int(input("Now tell me your age, PSYCHO:\n"))
            
            birthday_year3 = 2026 - my_age3
            
            print(f"Well, FUN FACT! Your birthday year is {birthday_year3}")
            print("If you are able to undrestand...")
            
            exit_program = input("Don't you want to leave me alone?")
            if exit_program.lower() == 'no':    
                print("hehe... Don't be so happy, my dear clown.")
                print("There is NO ROOM for dumb clowns in the WORLD!")   
                break
                
            elif exit_program.lower() == 'yes':           
                print("Good clown... Be careful to take your brain with yourself...")            
                break
                
            else:
                print("😒😒")
                break
            
    else:
        
        print(f"It's nice to meet you {my_name}!")
        print(random.choice(compliments))
        
        my_age = int(input(f"Okay, naughty {my_name}! How old are you?\n"))
        
        if my_age < 10:
            print("Aww, a little sweet pie! My little programmer!")
        elif my_age == 17:
            print("Ohhh! We are in a same age, baby!")
        elif my_age < 20:
            print("Teenager! Best time to start coding, trust me.")
        elif my_age < 40:
            print("Adult pro max! You can conquer the coding world.")
        else:
            print("Wow! It's NEVER too late to learn. RESPECT!")
            
        birthday_year = 2026 - my_age
        
        print(f"Well, FUN FACT! Your birthday year is {birthday_year}")
        print("Damn... I'm too smart, bro...")
        
        exit_program = input("Don't you want to leave me alone?")
        if exit_program.lower() == 'no':
            print("HEHE, It's MY program! I have power here! BYE BYE!")
            break
        elif exit_program.lower() == 'yes':
            print("Good user! Bye Bye!")
            user_counter += 1
            all_noble_users.append(my_name)
            print(f"You are number {user_counter} who used this app!")
            print("Go and cry from happiness for achieving this MAGNIFICENT GLORY!")
            break
        
print(f"All the users who used the app: {all_noble_users}")        