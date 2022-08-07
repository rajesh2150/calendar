
import calendar
choice=int(input("1.For Year and Month 2.For Year"))
if choice==1:
    
    year = int(input("Enter year:"))
    month=int(input("Enter month:"))
    mycal=calendar.month(year,month)
    print(mycal)
elif choice==2:
    year=int(input("Enter The Year:"))
    mycal=calendar.calendar(year)
    print(mycal)
else:
    print("Wrong input ")
print("Made By Rajesh Korlapati")
