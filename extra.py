



# a = 0 
# b = 1

# for i in range(11):
    
    
#     print(a)
#     a, b = b , a + b


# a = 0
# b = 1
    
# for i in range(10):
#     print(a)
#     a, b = b , a + b
# print("   <= It's the last piece")
    
    
    
# lastPiece = input("This is the staff. what should be the last piece ? : ")

# for i in range(3, 0,-1):

# count = 3
    
# while count > 0:
            
#     count -= 1
        
#     print(count)



# def yORn(prompt):
    
#     while True:
        
#         if value == input(prompt in ['n', 'N', 'no', 'NO', 'No' ]):
            
#             value = False
        
#         elif value == input(prompt in['y', 'Y', 'Yes', 'yes', 'Yes', 'YES']):
            
#             value = True
            
#         else:
            
#             print("I don't understand what you mean" )
            


# def intANDfloat(prompt):
#     while True:
#         value = input(prompt)
#         try:
#             return int(value)
#         except ValueError:
#             try:
#                 return float(value)
#             except ValueError:
#                 print('This is not valid number. ')
        


# def yORn(prompt):
    
#     while True:
        
#         answer = input(prompt).strip().lower()
    
#         if answer in ['y', 'yes',]:
#             return 'yes'
            
        
#         elif answer in ['n', 'no']:
#             return 'no'
            
#         else:
            
#             print("I don't understand what you mean" )
            



# key = 53

# name = input('Hi, what is your Name ? : ')
# print("Hi,", name + '.',)

# initializing = yORn("Let's find treasures! (y/n) : ")


    
    

# key = 33


# name = input('Hi, what is your Name ? : ')
# print("Hi,", name + '.',)

# initializing = input("Let's find treasures! (y/n) : ")

# while True:
    
#     if not initializing in ['n', 'N', 'no', 'NO', 'No', 'y', 'Y', 'Yes', 'yes', 'Yes', 'YES']:
        
#         print("I don't understand what you mean. ")
#         initializing = input("Will you find the tresure ? (y/n) : ")
#         if initializing in ['n', 'N', 'no', 'NO', 'No']:
#             print('Ok. bye !')
#             break
#         gameStart = input("We should find the key first to open the door! \nThe key is hidden between 0 and 100. Let's find out the key! (y /n): ")
        
    
#     elif initializing in ['n', 'N', 'no', 'NO', 'No']:
        
#         print('Ok. bye !')
#         break
    
        
#     elif initializing in ['y', 'Y', 'Yes', 'yes', 'Yes', 'YES']:
        
#         gameStart = input("We should find the key first to open the door! \nThe key is hidden between 0 and 100. Let's find out the key! (y /n): ")
            
#     if not gameStart in ['y', 'Y', 'Yes', 'yes', 'YES']:
#         print('Ok. then I should find someone else. Bye. ')
#         break
#     elif gameStart in ['y', 'Y', 'Yes', 'yes', 'YES']:
            

#             guessedNum = intANDfloat("What should be the key ? (between 0 and 100) : ")
            
#             while guessedNum != key:


#                 if guessedNum > key:

#                     guessedNum = intANDfloat('It seems to be too big. : ')

#                 elif guessedNum < key:
                    
#                     guessedNum = intANDfloat('It seems to be too small. : ')
                    
#             if guessedNum == key:

#                 intoBeyond = input("You got it! now, we can get into the beyond through the door. Let's go! (y /n):  ")
                
                

def counter(prompt):
    count = 3
    
    insert = input(prompt)
    
    while count > 1:
        
        if count == 2:
            
            print("Hm... this shouldn't be the last piece. Now, you have only", count, 'more chances. ' )
        
        elif count == 1:
            
            print("It's wrong. You have only", count, "more chance. ")
            
        elif count == 0:
            
            print("I'm sorry but you failed. ")
            break