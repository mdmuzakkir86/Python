# Exception handling
def add(number):
    total = 0

    for i in number:
        total += i
    print("Sum of:", end="")
    print(*number, sep="+", end="=")
    return total


try:
    inputs = input("Enter values to add:")
    inputs = list(map(int, inputs.split()))  # Used to read multiple values at a time from user

    # if input is greater than 10000000
    for i in inputs:
        if i > 100000000:
            raise IOError

    print(add(inputs))

except ValueError:
    print("Enter numbers only")
except IOError:
    print("Number should be less than 1 Million")
finally:
    print("----------------------------")


# User-define Exception
class ValueIsTooLarge(Exception):
    pass


class Age:
    def customeException(self, age):
        self.age = age
        print("Age is:", self.age)


try:
    age = int(input("Enter age:"))
    if age > 110:
        raise ValueIsTooLarge
    else:
        a = Age()
        a.customeException(age)
except ValueIsTooLarge:
    print("Enter age below 110")

try:
    f = open("Practice.txt")
    try:
        f.write("/nHello Good Morning")  # Exception is here because we need permission to write
    except:
        print("Something went wrong 1")
    finally:
        f.close()
except:
    print("Something went wrong")
