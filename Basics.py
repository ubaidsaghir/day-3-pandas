def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        return sum / len(numbers)
    
c = average(5,6,7,1)
print(c)    
# try catch method
try:
    age = int(input("Enter age: "))
    print("Passed")
except ValueError:
    print("Please enter a number")
    
    
    def safe_input():
        while True:
        try:
            number = int(input("Enter number greater than 5: "))
            if number > 5:
                return number
            else:
                print("Number must be > 5")
        except ValueError:
            print("Please enter a valid integer.")


def get_even(numbers):
    evens =[]
    for num in numbers:
        if num %2==0:
            evens.append(num)
            
        return evens


def average(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total / len(numbers)
