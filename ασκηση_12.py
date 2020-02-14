from datetime import date
End = date(int(input("give a year")),int(input("give month")),int(input("give day")))    #θεωρω οτι δινονται ορθα στοιχεια δεν κανω ελεγχο εγκυροτητας αφου δεν ζητειται απο την εκφωνηση
from datetime import datetime
date_2 = datetime.today().strftime('%d/%m/%Y')
d_2 = date_2[0]+date_2[1]
m_2 = date_2[3]+date_2[4]
y_2 = date_2[6]+date_2[7]+date_2[8]+date_2[9]
Start=date(int(y_2),int(m_2),int(d_2))
Gap = (End-Start).days
if int(Gap) < 0  :
    Gap = int(Gap) * -1 #an h difora einai arnhtikh thn kano thetikh
print("The distance is:",Gap,'day/s',",",Gap*1440,"minute/s",",",Gap*86400,"second/s")
from calendar import monthrange
num_days = monthrange(int(End.year),int(End.month))
import calendar
print("The month",calendar.month_name[End.month],"has",num_days[1],"days")




