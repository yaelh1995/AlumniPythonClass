string = "whats good?"
uppercase = str.upper(string)
print(uppercase)

def prime():
    num = input("choose a number that you think is prime")
    integer = input("choose a number, to see if prime number is divisible")
    if num > 1 and num % integer == float:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

prime()

def even_odd(num_1, num_2, num_3, num_4, num_5):
    num = [num_1, num_2, num_3, num_4, num_5]
    for i in num:
        if i % 2 == 0:
            print(i, " is an even number.")
        else:
            print(i, "is an odd number.")
