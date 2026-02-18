(1) 


 a=float(input (" enter value in fahrenheit so it converts to celsius :"))

 b=(5/9)*(a-32)

 print(a, "F =",b, "C")

------
(2) 

length =int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("Area =", area)
print("Perimeter =", perimeter)

---------
(3) 

angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = 180 - (angle1 + angle2)

print("Third angle =", angle3)
if angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("Triangle is Right-angled")
elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
    print("Triangle is Isosceles")
else:
    print("Triangle is neither Right-angled nor Isosceles")

----------
(4) 

days = int(input("Enter number of days: "))
years = days // 365
remaining_days = days % 365

months = remaining_days // 30
remaining_days = remaining_days % 30

weeks = remaining_days // 7

print("Years =", years)
print("Months =", months)
print("Weeks =", weeks)

-----------
(5) 

m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5

average = total / 5

# (Assuming each subject is out of 100)
percentage = (total / 500) * 100

print("Total Marks =", total)
print("Average Marks =", average)
print("Percentage =", percentage, "%")

