balance=10000
pin=int(input("enter your pin:"))
if(pin==4086):
    print("welcome!The menue is shown")

    while True:
      print("welcome!The menue is shown")
      print("1.check balance")
      print("2.deposit")
      print("3.withdraw")
      print("4.Exit")
      choice=int(input ("enter your choice:"))
      if(choice==1):
       print("balance is",balance)
      elif(choice==2):
       deposit=int(input("enter your deposit amount:"))
       balance=deposit+balance
       print("total balance:",balance)
      elif(choice==3):
        withdraw=int(input("enter your withdraw amount:"))
        if(balance>=withdraw):
         balance=balance-withdraw
         print("remaining amount:",balance)
        else:
          print("insufficient balance:") 
      elif(choice==4):
        break
      else:
        print("incorrect choice:")
else:
    print("pin is incorrect")        