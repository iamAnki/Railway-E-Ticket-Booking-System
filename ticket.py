print("Welcome to Indian Railways Ticket Booking System\n")
dictcon={}
dictwait={}

x=1
left=input("Total Tickets")
print("Total Tickets availabe is "+str(left))

while True:
    
    print("For Ticket Booking Press 1\nFor PNR status press 2\nFor cancellation press 3\nTo Display Ticket press 4\nTo Exit press 5")

    ch=input("Enter Choice :")
    try:
        choice=int(ch)
    except:
        print("Wrong Input,Try Again\n")
        continue
    
    if(choice in range(1,4)):
        if(choice==1):

            while True:
                
                print("Book A ticket")

                print("Enter details for passenger "+str(x))
                name=input("Enter Name: ")
                age=input("Enter Age: ")
                sex=input("Enter Sex: ")

                if(x<=int(left)):
                    dictcon[str(x)]={'Name:':name,'Age:':age,'Sex:':sex}             
                    print("\nBooking Succesfull Your Reg number is "+str(x))
                else:
                    dictwait[str(x)]={'Name:':name,'Age:':age,'Sex:':sex}
                    print("\nBooking full.Put into Waiting list.Your Reg number is "+str(x))
                        
                x+=1

                q=input("book more [y/n]:")
                
                if q.lower()=='y':
                    continue
                elif q.lower()=='n':
                    break
                else:
                    print("Wrong Input\n")
                    break
                    
        
        elif choice==2:

            c=input("Enter your Reg number ")
            if (int(c)<=x):
                if(str(c) in dictcon.keys()):
                    print("Confirmed\n")
                    continue
                elif(str(c) in dictwait.keys()):
                    print("Waiting\n")
                    continue
                else:
                    print("Not found")
                    continue
            else:
                print("Not found")
                continue
            
        elif choice==3:
            
            r=input("Enter ticket reg number for cancellation")
            if(str(r) in dictcon.keys()):
                del dictcon[str(r)]
                for keys,values in dictwait.items():
                    dictcon[str(keys)]=dictwait[str(keys)]
                    del dictwait[str(keys)]
                    break
                print("Ticket with reg number "+str(r)+"deleted\n")
            elif(str(r) in dictwait.keys()):
                del dictwait[str(r)]
                print("Ticket with reg number "+str(r)+"deleted\n")
            else:
                print("Not Found")     

            
    elif(choice==4):
        s=input("Enter ticket Reg number to display")
        try:
            try:
                print(dictcon[str(s)])
                continue
            except:
                print(dictwait[str(s)])
                continue
        except:
            print("Not found")
            continue

    elif(choice==5):
        break
    
    else:
        print("Wrong Input,Try Again\n")
        continue