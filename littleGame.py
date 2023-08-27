
def intANDfloat(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                print('This is not valid number. ')


def get_yes_or_no(prompt):
    
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['y', 'yes']:
            return 'yes'
        elif answer in ['n', 'no']:
            return 'no'
        else:
            print("I don't understand what you mean.")

key = 33


name = input('Hi, what is your Name ? : ')
print("Hi,", name + '.',)

initializing = get_yes_or_no("Let's find treasures! (y/n) : ")



if initializing == 'no':
    
    print('Ok. bye !')
    
    
        
elif initializing == 'yes':
    
    gameStart = get_yes_or_no("We should find the key first to open the door! \nThe key is hidden between 0 and 100. Are you ready? (y /n): ")
        
    if gameStart == 'no':
        
        print('Ok. then I should find someone else. Bye. ')
        
    elif gameStart == 'yes':
        
        guessedNum = intANDfloat("What should be the key ? (between 0 and 100) : ")
            
        while guessedNum != key:
            
            if guessedNum > key:

                guessedNum = intANDfloat('It seems to be too big. : ')

            elif guessedNum < key:
                    
                guessedNum = intANDfloat('It seems to be too small. : ')
                    
        if guessedNum == key:

            intoBeyond = get_yes_or_no("You got it! now, we can get into the beyond through the door. Let's go! (y /n):  ")
            
            if intoBeyond == 'no':
                
                print('Ok. then I should find someone else. thanks for your help. Bye. ')
                
            
            elif intoBeyond == 'yes':
                
                print("Hm... it's too dark here. Next, we should brighten up this space.")
                
                
        

                print("This is my staff, but I've lost the last piece. ")
                print('However, this is a magical staff. So, even if you could just imagine the last peace.')
                print('we can reassemble the staff with your imagination. And then, by using the staff, we can brighten up this space. ' )
                print("But please remember ! You can only imagine 3 times.")
                print('If you imagine the piece more than 3 times, it will break.')
    
    
                secondGame = get_yes_or_no('Would you help me? (y /n): ')
                    
                if secondGame == 'no':
                    
                    print('Ok. Bye.')
                        
                elif secondGame == 'yes':
                    
                    a = 0
                    b = 1
                    
                    for i in range(10):
                        print(a)
                        a, b = b , a + b
                    print("   <= It's the last piece")
                    

                    lastPiece = intANDfloat("Look at this staff here. What should be the last piece? : ")

                    
                    count = 3
                    should_continue = True

                    while count >= 1:

                        
                        if lastPiece == 55:
                            
                            print('Thank you! You have repaired the staff. Now, we can brighten up here.')
                            break
                        
                        elif lastPiece != 55:
                            count -= 1
                            if count == 0:
                                print("I'm sorry but you failed.")
                                should_continue = False
                                break
                            else:
                                print("Hm... this shouldn't be the last piece. Now, you have only", count, 'more chances. ' )
                                lastPiece = intANDfloat("What should be the last piece ? : ")
                        
                            
                    if should_continue:           
                        lastQuest = get_yes_or_no("Look! There is a treasure chest over there. Let's go over there! (y /n)")
                        
                        
                        if lastQuest == 'yes':
                            
                            print('The chest is hardly locked, and there is a small note on it.')
                            print("The note has a riddle: 'I speak without a mouth and hear without ears.\nI have no body, but I come alive with the wind. What am I?'")
                            print('I believe that, if you speak out the answer, we can open the chest.\nBe aware! Here, there is another message. You can say the answer only one time')
                            
                            riddle = input('What should be the answer ?: ')
                            
                            if riddle == 'echo'.strip().lower():
                                
                                
                                print("You've done it. Here,a parchment Scroll, jeweled Dagger,")
                                print("golden Coins, mystic Gemstone ,aged Wine, an old Book,")      
                                print("a Small Box, magic Lantern, pocket watch, and mariner's compass all belong to you.")
                                print("Good bye,", name)
                            
                            else:
                                print("I'm sorry, but you failed. This treasure should belong to me now. Bye !")
                        
                        if lastQuest == 'no':
                            
                            print('Ok, thanks for your help. Bye.')        
