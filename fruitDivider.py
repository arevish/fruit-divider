try:
    n = int(input("Enter number of apple harry got: "))
    mn = int(input("Enter the minimum number of students: "))
    mx = int(input("Enter the maximum number of students: "))
except ValueError:
    print("Enter integer values only")
if mn >= mx:
    print(f"It's not a range minimum {mn} should be less than maximum {mx}")
if n<mx:
    print("unable to divide properly number of apple is way less than number of students")
else:
    for i in range(mn ,mx+1):
        if n% i==0 :
            print(i," is the divisor of ",n)
        else:
            print(i," is not a divisor of ",n)
