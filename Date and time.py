from datetime import datetime
current_time=datetime.now()
print(current_time)
format1=current_time.strftime("%Y-%m-%d_%H:%M:%S")
print(format1)
#Display the format[MM/DD/YYYY]
format2=current_time.strftime("%m/%d/%Y")
print(format2)
#Display the format[Day,Month,DD,YYYY]
format3=current_time.strftime("%A,%B,%d,%Y")
print(format3)
#Display the format[Day,Month,DD,YYYY,HH:MM:SS AM/PM]
format4=current_time.strftime("%A,%B,%d,%Y,%H:%M:%S %p")
print(format4)
#Display the date and time like "Thu-Jul-11 10:26:23 IST 2024"
format5=current_time.strftime("%a-%b-%d %H:%M:%S IST 2024")
print(format5)
#Display [Abbr Weekday Name-Abbr month name-DD HH:MM:SS IST YYYY]  Eg: Wed-Oct-02 12:41:18 IST 2024
format6=current_time.strftime("%a-%b,%d %H:%M:%M IST %Y")
print(format6)
#Display format- 8 [ISO format:]
format7=current_time.strftime("%Y,%m,%d")
print(format7)
#Display Date only
format8=current_time.strftime("%d")
print(format8)
#Display Time only
format9=current_time.strftime("%H:%M%S")
print(format9)
#Display month only
format10=current_time.strftime("%B")
print(format10)
#Display Year only
format11=current_time.strftime("%Y")
print(format11)


