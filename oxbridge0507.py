import time
#prints numbers from 1-10
#while True:
##i=15
##for i in range (1,11):
##    print (i)
##    i+=1
##    time.sleep(0.15)
##  
##name = 'adam'
##num = 4
##k= name *num
##print(k)
##name = input("$ENTER YOUR NAME")
##rate = input("$ENTER HOURLY RATE")
##hours = input("$ENTER HOURS WORKED")
##salary= int(rate) * int(hours)
##print (name,"Your salary is", "£", salary,"per month")
celc = int(input("enter in celcius"))
fahr = (celc*(9/5))+32
print("That's",fahr,"Fahrenheit.")
fahr= int(input("enter in fahrenheit"))
celc = (fahr-32)*(5/9)
print("That's",celc,"Celcius")
