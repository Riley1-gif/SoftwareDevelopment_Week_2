score = int(input("Enter your score: "))

if score >= 90: 
    print("Excellent")
    print("Grade: A")
elif score >= 80:
    print("Good")
    print("Grade: B")
elif score >= 70:
    print("Average")
    print("Grade: C")
elif score > 100:
    print("Thats not a valid score")
elif score <= 0:
    print("Thats not a valid score")
else: 
    print("Poor")
    print("Grade: F")


    