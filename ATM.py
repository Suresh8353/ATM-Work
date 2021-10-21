amount=500
def ATM():
          print("========================================================================")
          print("\t\t  A T M   O P E R A T I O N")
          print("========================================================================")
          print()
          print("\t\t\t 1. Deposite ")
          print("\t\t\t 2. Withdrawal")
          print("\t\t\t 3. Balence Enqury ")
          print("\t\t\t 4. Generate Pin  ")
          print("\t\t\t 5. Exit")
          print()
          print("======================================================================")
          ch=input("Enter your choice:")
          if ch in ('1','2','3','4','5'):
                    if ch=='1':
                              Deposite()
                    if ch=='2':
                              Withdrawal()
                    if ch=='3':
                              BalenceEnqury()
                    if ch=='4':
                              GeneratePin()

                    if ch=='5':
                              Exit()
                    #else:
                              #print("Sorry your choice is wrong please try again:")
                              #ATM()
          else:
                    print("Sorry String/Special Symbols/negative numbers are not allowed here:")
                    print("------------>Try Again")
                    print(end="\n\n")
                    ATM()
def Deposite():
          global amount
          dp=int(input("Enter your ammount for Deposite:"))
          ac=int(input("Enter your pin code of ATM:"))
          if ac<1000 or ac>10000:
                    print("\n========================================================================")
                    print("Invalid Pin please try again. ATM Pin code must be 4 Digit:")
                    print("\n========================================================================")
                    Deposite()
          else:
                    amount=amount+dp
                    print("Deposite Succesfully your Deposite balance is:",dp)
                    print("Total balence is in your account:",amount)
                    print()
                    ATM()
def Withdrawal():
          global amount
          wd=int(input("Enter your ammount for Withdrawal:"))
          ac=int(input("Enter your pin code of ATM:"))
          if ac<1000 or ac>10000:
                    print("\n=========================================================================")
                    print("Invalid Pin please try again. ATM Pin code must be 4 Digit:")
                    print("\n=========================================================================")
                    Withdrawal()
          if wd>=amount:
                    print("\n========================================================================")
                    print("Sorry you have not sufficient balence in your account:")
                    print("--------------->Try again")
                    print("\n")
                    print("==========================================================================")
                    Withdrawal()
                    
          else:
                    amount=amount-wd
                    print("Withdrawal Succesfully your Withdrawal balance is:",wd)
                    print("Total balence is in your account:",amount)
                    ATM()
def BalenceEnqury():
          global amount
          ac=int(input("Enter your pin code of ATM:"))
          if ac<1000 or ac>10000:
                    print("\n=========================================================================")
                    print("Invalid Pin please try again. ATM Pin code must be 4 Digit:")
                    print("\n=========================================================================")
                    BalenceEnqury()
          else:
                    print("Total balence is in your account:",amount)
                    print()
                    ATM()
def GeneratePin():
          global amount
          an=int(input("Enter your Account Number:"))
          if an<1000000000000000 or an>10000000000000000:
                    print("\n=========================================================================")
                    print("Invalid Account Number please try again. A/C number must be 16 Digit:")
                    print("\n=========================================================================")
                    GeneratePin()
          ac=int(input("Enter  pin code for  generate ATM pin :"))
          if ac<1000 or ac>10000:
                    print("\n========================================================================")
                    print("Invalid Pin please try again. ATM Pin code must be 4 Digit:")
                    print("\n========================================================================")
                    GeneratePin()
          else:
                    print("===========================================================================")
                    print("Your ATM pin has Successfully generate")
                    Exit()
                    
def Exit():
          print("===================================================================================")
          print("Thanku for using ATM machine:")
          
                    
ATM()


















