print("Enter Date in the Format: DD/MM/YYYY")
d1=input("Enter the first date: ")                                             #to get input from the user
d2=input("Enter the second date: ")
if d1[2]!="/" or d1[5]!="/" or d2[2]!="/" or d2[5]!="/":                       #to make sure user inputs a valid date
    print("Enter a valid date")
    exit()
if int(d1[6:])>int(d2[6:]):
    print("Second date should be greater than the first one.")
    exit()
if int(d1[0:2])>31 or int(d1[3:5])>12 or int(d2[0:2])>31 or int (d2[3:5])>12:
    print("Please Enter a valid date.")
    exit()
y1=d1[6:]                                                                      #to extract the year from the date
y2=d2[6:]                                                                      #to extract the year from the date
y1=int(y1)                                                                     #converting the strint to integer
y2=int(y2)                                                                     #converting the strint to integer
ly=""                                                                          #variable to store all the leap years
nly=""                                                                         #variable to store all the non leap years
while y1<=y2:
    if y1%4==0:                                                                #condition to check leap year
        ly=ly+str(y1)+","                                                      #adding the year to the variable
    elif y1%4!=0:                                                              #condition to check non leap year
        nly=nly+str(y1)+","                                                    #adding the year to the variable
    if y1==y2:
        ly=ly[:-1]+"."                                                         #to get a well formatted output
        nly=nly[:-1]+"."
    y1+=1
print("Leap years are: "+ly)
print("Non Leap Years are: "+nly)
