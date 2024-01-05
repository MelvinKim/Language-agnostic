temp = -45
forecast = "rainy"

# if, elif and else
if temp > 80:
    print("It's too hot")
    print("Stay inside!")
elif temp < 60:
    print("It's too cold")
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")
 
#  logical or
if temp > 80 or temp < 60:
    print("Stay outside")
else:
    print("Enjoy the outdoors!")
   
# logical and 
if temp > 80 and temp < 60:
    print("Stay Inside")
else:
    print("Enjoy the outdoors!")
    
# not
if not forecast == "rainy":
    print("Go outside!!")
else:
    print("Enjoy the outdoors!")