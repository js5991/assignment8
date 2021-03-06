'''
Created on Nov 28, 2016
This is the main module of assignment 8. 
@author: Jingyi Su
@description: This program asks user for inputs of a list of numbers of shares to buy as positions for investment and then asks user for the number of times to repeat the investment simulation trials

'''
from Investment import Investment
import sys

if __name__ == '__main__':
    while True:
        try:
            inputstr=input('Please enter a list of numbers of shares to buy in parallel, such as [1,10,100,1000]')
            if (inputstr=='quit'):
                print("User Directed Quit.")
                sys.exit()
            inputstr=inputstr.replace(' ','')#Remove extra blank
            if inputstr=='':
                raise ValueError('Invalid Input: Need a list of numbers of shares to buy in parallel')
            if inputstr[0]!='[' or inputstr[-1]!=']':
                raise ValueError('Invalid Input: Need a list of number in [ and ], such as [1,10,100,1000]')
            positions=list(map(int,inputstr[1:-1].split(",")))
            if any(x<=0 for x in positions):
                raise ValueError('Invalid Input: all numbers of shares need to be positive')
            break
        except ValueError as msg:
            print(msg)
        except KeyboardInterrupt:
            print('Keyboard Interruption')
            sys.exit()
        except EOFError:
            print('EOFError')
            sys.exit()
        
    while True:
        try:
            inputstr2=input('Please enter the number of times you want to repeat the simulation')
            if (inputstr2=='quit'):
                print("User Directed Quit.")
                sys.exit()            
            num_trials=int(inputstr2)
            Investment.investment(positions,num_trials).simulation()
            break
        except ValueError as msg:
            print(msg)
        except KeyboardInterrupt:
            print('Keyboard Interruption')
            sys.exit()
        except EOFError:
            print('EOFError')
            sys.exit()
           