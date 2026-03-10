import random
import smtplib
from datetime import date
import time

def total(a):
    total=0
    for key in a:
        if key=='Burger':
            total+=a[key]*70
        elif key=='French Fries':
            total+=a[key]*50
        elif key=='Coffee':
            total+=a[key]*60
        elif key=='Soft Drink':
            total+=a[key]*40
        elif key=='Ice Cream':
            total+=a[key]*60
        else:
            total+=a[key]*100
    return total

def mail(a,b):
    b=str(b)
    msg="Here's the OTP to confirm your order: "+b
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('bakerypython@gmail.com','hofi iiof yrek widn')
    server.sendmail('bakerypython@gmail.com',a,b)
    

def order():
    l=["Burger-₹70","French Fries-₹50","Coffee-₹60","Soft Drink-MRP","Ice-Cream-₹60","Pizza-₹100"]
    order={}
    
    while True:
        print("1.Add item")
        print("2.Delete item")
        print("3.Checkout")
        print("4.Exit")
        choice1=int(input("Enter the number of the action you want to perform: "))
        
        if choice1==1:
            for i in range(len(l)):
                print(i,".",l[i])
            choice2=int(input("Enter the number of your choice: "))
            
            if choice2==0:
                if 'Burger' in order:
                    order['Burger']+=1
                else:
                    order['Burger']=1
                    
            elif choice2==1:
                if 'French Fries' in order:
                    order['French Fries']+=1
                else:
                    order['French Fries']=1
                    
            elif choice2==2:
                if 'Coffee' in order:
                    order['Coffee']+=1
                else:
                    order['Coffee']=1
                    
            elif choice2==3:
                if 'Soft Drink' in order:
                    order['Soft Drink']+=1
                else:
                    order['Soft Drink']=1
                    
            elif choice2==4:
                if 'Ice Cream' in order:
                    order['Ice Cream']+=1
                else:
                    order['Ice Cream']=1
                    
            elif choice2==5:
                if 'Pizza' in order:
                    order['Pizza']+=1
                else:
                    order['Pizza']=1
                    
            else:
                print("Please choose a valid option! ")
                
        elif choice1==2:
            print("Your order is: ")
            print(order)
            choice3=input("Enter the name of the item you want to delete: ")
            
            if choice3.lower()=='burger':
                del order['Burger']
                
            elif choice3.lower()=='french fries':
                del order['French Fries']
                
            elif choice3.lower()=='ice cream'or choice3.lower()=='ice-cream':
                del order['Ice Cream']
                
            elif choice3.lower()=='coffee':
                del order['Coffee']
                
            elif choice3.lower()=='soft drink':
                del order['Soft Drink']
                
            elif choice3.lower()=='pizza':
                del order['Pizza']
                
            else:
                print("Please enter a valid option! ")
                
        elif choice1==3:
            name=input("Please enter your name: ")
            email=input("Please enter your email id: ")
            today=date.today()
            today=date.isoformat(today)
            digits='0123456789'
            otp=''
            for i in range(4):
                otp+=random.choice(digits)
            mail(email,otp)
            
            print("Here's your order: ")
            print(order)
            print("Your total is: ","₹",total(order))
            print("Please check the spam mails")
            code=input("Please enter the 4-digit OTP send to your email: ")
            
            if code==otp:
                print("Your order was confirmed")
                return [name,email,today,total(order)]
                
            else:
                print("Wrong OTP,please try again")
                tries=1
                
                while tries<4:
                    code1=input("Please re-enter your OTP: ")
                    
                    if code1==otp:
                        print("Order Confirmed!!")
                        break
                
                    
                    else:
                        tries+=1
                        
                if tries==4:
                    print("Order failed")
            break
        
        elif choice1==4:
            break
        
        else:
            print("Please select a valid option!!")
        

                    
                                      
print("1.Order")

choice=int(input("Enter your choice number: "))

if choice==1:
    print("You have chosen 'Order' ")
    x = order()
