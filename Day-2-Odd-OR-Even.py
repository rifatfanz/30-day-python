import random 
print("=== Even OR Odd Game ===") 
print("Exit, if you write exit the game will be stopped...") 
score = 0 

while True: 
    number = random.randint(1, 100) 
    print("The number: " + str(number)) 
    
    ans = input("Is It Odd OR Even? ").lower() 
    
    if ans == "exit": 
        print(f"Game over.! Your Final Score..: {score} ") 
        break 
    
    if number % 2 == 0: 
        ch = "even" 
        
    else: 
        ch = "odd" 
        
    if ans == ch: 
        score = score + 1 
        
        
        print("Correct..! You are a genius 🎉") 
        
        
    else: 
        print("Wrong.. Better luck next time.. Shotik: " + ch) 
        
    print(f"Your Score: {score}")