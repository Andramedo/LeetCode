from random import randint
guess = randint(1, 100) #Загаданное число

def InputChoise(): #Обработка ввода пользователя

    while True: #Вечный цикл, пока польщователь не введет коректное значение
        try:
            choise = int(input("""Please select the difficulty level:
                               
            1. Easy (10 chances)
            2. Medium (5 chances)
            3. Hard (3 chances)
                               
Your choise: """))
            
            if choise >= 1 and choise <= 3:
                print("Success!")
                return choise
                
            
            else: #Обработка исключения №1
                print("Number may be between 1 and 3!!!")

        except ValueError: #Обработка исключения №2
            print("Enter the number between 1 and 3!")

print("""
Welcome to number guessing game

""")

def Game(level): #Код для игры
    print("I'm thinking your number between 1 and 100")

    if level == 1:
        n = 10
    elif level == 2:
        n = 5
    else:
        n = 3

    for i in range(n):
        userInput = int(input())

        if userInput == guess:
            print("Congratulations!")
            break
        elif userInput > guess:
            print("My number lesser than your's")
        else:
            print("My number bigger than your's")
        
    print(f"My number was {guess}")
        

level = InputChoise()
Game(level)