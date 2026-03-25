#02- Enhanced gussing game
import random

print("\n=====Number gussing game=====")
print("\n Choose difficulty")
print("1.Easy : 1-50")
print("2.Medium : 1-100")
print("3.Hard : 1-200")

while True:
    choice=input("\n Select your choice :")

    if choice=="1":
      a=1
      b=50
      maxAttempt=10
      current_atm=0

    elif choice=="2":
      a=1
      b=100
      maxAttempt=7
      current_atm=0

    elif choice=="3":
      a=1
      b=200
      maxAttempt=5
      current_atm=0

    else:
       print("\n Invalid choice !") 
       continue 
#generate random number
    randomNumber=random.randint(a,b)
    is_won=False

    while current_atm < maxAttempt:
        guess=int(input(f"\n Attempt {current_atm+1}/{maxAttempt} - Enter your guess : "))
        
#Display comments
        if (guess==randomNumber):
           print(f"\n Congratulations ! You guess it in {current_atm+1} attempts")  
           is_won=True
           break
        elif guess>randomNumber:
          print("\n Too high !Try again")
        else:
          print("\n Too low !Try again")
        if abs(guess-randomNumber)<=5:
           print("\n You are geting close")  
        
        current_atm =current_atm + 1

    if not is_won:
       print("\nGAME OVER !")    
       print(f"\n Random number is {randomNumber}")

    playAgain=input("\nPlay again(Yes/No) :")
    if playAgain != "Yes":
       print("Thanks for playing.")
       break
          
    
                 

   
           

