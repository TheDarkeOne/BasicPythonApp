import itertools, random, calendar

def display_cards():
    deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

    random.shuffle(deck)

    print("You got:")
    for i in range(5):
        print(deck[i][0], "of", deck[i][1])

def display_calender(year, month):
    yy = year  
    mm = month

    print(calendar.month(yy, mm))

def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, int(smaller)+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

def add_two_numbers(x, y):
    return x + y

def subtract_two_numbers(x, y):
    return x - y

def multiply_two_numbers(x, y):
    return x * y

def divide_two_numbers(x, y):
    if y == 0:
        print("Invalid denominator.")
        return x / 1
    else:
        return x / y

def main():
    print("Select an option.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.LCM\n6.GCD\n7.Factor Calculator\n8.Draw Cards\n9.Display Calender")

    while True:
        choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")
        if choice in ('1', '2', '3', '4', '5', '6', '7','8','9'):
            if choice == '1':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(num1, "+", num2, "=", add_two_numbers(num1, num2))
            elif choice == '2':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(num1, "-", num2, "=", subtract_two_numbers(num1, num2))
            elif choice == '3':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(num1, "*", num2, "=", multiply_two_numbers(num1, num2))
            elif choice == '4':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(num1, "/", num2, "=", divide_two_numbers(num1, num2))
            elif choice == '5':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("The L.C.M. of", num1, "and ", num2, "is", compute_lcm(num1, num2))
            elif choice == '6':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("The G.C.D. of", num1, "and ", num2, "is", compute_hcf(num1, num2))
            elif choice == '7':
                num = int(input("Enter a number to find the factors of: "))
                print_factors(num)
            elif choice == '8':
                display_cards()
            elif choice == '9':
                year = int(input("Enter the year: "))
                month = int(input("Enter the month: "))
                display_calender(year,month)
            break
        else:
            print("Invalid Input")

main()