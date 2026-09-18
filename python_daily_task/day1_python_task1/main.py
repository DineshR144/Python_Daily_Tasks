current=int(input("Enter your current battery percentage:"))
if(current<=20):
    print("critical-fast charging recommended")
elif(current<=50):
    print("low-normal charging")
elif(current<=80):
    print("moderate-partial charging")
else:
    print("invalid")
des=current-100
print("battery capacity 60kwh")
print("current:",current,"%")
print("desired:",des,"%")
    
