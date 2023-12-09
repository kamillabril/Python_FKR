# FKR Bryl KB-22

# TASK 1
s = input('Enter string: ')
val = input('Enter number: ')
val = int(val)
print(s * val)

# TASK 2
s_10 = input('Enter decimal numbers: ')
s_10 = int(s_10)
s_16 = hex(s_10)

print('Hexadecimal is:', s_16[2:])


# TASK 3
def checking_keyword(dict1, word):
    if dict1.get(word) is None:
        return False
    else:
        return True


mydog = {
    "name": "Keeper",
    "age": 10,
    "breed": "maltese dog",
    "color": "white"
}
print(checking_keyword(mydog, "name"))
print(checking_keyword(mydog, "dog"))

# output:
# True
# False

# TASK 4
s = input("Enter the sides of polygon: ")
side_length = s.split(" ")
if len(set(side_length)) == 1:
    print("YES")
else:
    print("NO")

time = input("Enter the time ")
time_list = time.split(':')
if int(time_list[0]) > 23:
    print("Not valid number of hours")
elif int(time_list[1]) > 59:
    print("Not valid number of minutes")

# TASK 5
time = input("Enter the time ")

def count_seconds(hours='0', minutes='0', *args):
    try:
        h = int(hours)
        m = int(minutes)
        s = int(args[0][:2]) if len(args) != 0 else 0

        if h > 23 or h < 0 or m > 60 or m < 0 or s < 0 or s > 60:
            raise ValueError

        return h * 3600 + m * 60 + s
    except:
        return "The value is not a time"


print(count_seconds(*time.split(':')))


# TASK 6

def multiplicity(value=1):
    def decorator(fun):
        def wrapper(*args, **kwargs):
            for arg in args:
                if arg % value != 0:
                    raise ValueError("A number is not multiple of " + str(value))
            return fun(*args, **kwargs)
        return wrapper
    return decorator


@multiplicity(3)
def sum_by_3(a, b):
    return a + b


try:
    print(sum_by_3(3, 3))
    print(sum_by_3(2, 3))
except ValueError as e:
    print(e)

# TASK 7
from math import inf


def odd_ex_7(start=0, end=inf):
    if start % 2 == 0:
        start += 1
    while start < end:
        if start % 7 == 0:
            start += 2
        yield start
        start += 2


for i in odd_ex_7(end=50):
    print(i)


# TASK 8

def find(substr, string):
    if len(substr) > len(string):
        return False
    if substr == string[:len(substr)]:
        return True
    else:
        return (find(substr, string[1:]))


substr = input("Enter the subsring: ")
string = input("Enter the string: ")
if find(substr, string) == True:
    print(f"The substing '\033[1m{substr}\033[0m' is in string '\033[1m{string}\033[0m'")
else:
    print(f"The substing '\033[1m{substr}\033[0m' is not in string '\033[1m{string}\033[0m'")

# TASK 9
from math import inf


def FizzBuzz(start=0, end=inf):
    while start < end:

        if start % 15 == 0:
            yield "FizzBuzz"
        else:
            if start % 3 == 0:
                yield "Fizz"
            elif start % 5 == 0:
                yield "Buzz"
            else:
                yield start

        start += 1


for i in FizzBuzz(end=50):
    print(i)


# TASK 10

def draw(start=0, n=15):
    for i in range(n):
        yield '\n'
        for j in range(n):
            if i == n // 2 and j == n // 2:
                yield '*'
            else:
                if i == j or i + j == n - 1:
                    yield ' '
                else:
                    yield '*'


size = int(input("Enter size: "))
for i in draw(n=size):
    print(i, end=' ')
