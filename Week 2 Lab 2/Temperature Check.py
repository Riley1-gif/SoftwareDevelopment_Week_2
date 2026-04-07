temperatureC = float(input("Enter temperature in Celsius: "))

temperatureF = (temperatureC * 9/5)

if temperatureF >= 30:
    print("It's a hot day.")
elif temperatureF >= 20:
    print("It's a warm day. ")
elif temperatureF >  50:
    print("Its a very hot day. ")
elif temperatureF < -30:
    print("Its a very cold day. ")
else: 
    print("It's a cold day. ")

