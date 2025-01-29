# Generator-Function :
# --------------------
#    A generator-function is defined like a normal function, but whenever it needs to generate a
#    value, it does so with the yield keyword rather than return. If the body of a def contains yield,
#    the function automatically becomes a generator function.


# 1. There is a lot of complexity in creating iteration in Python; we need to implement __iter__() and __next__() method
#    to keep track of internal states.
#
# 2. It is a lengthy process to create iterators. That's why the generator plays an essential role in simplifying this
#    process. If there is no value found in iteration, it raises StopIteration exception


def even():
    for index in range(1, 11):
        if index % 2 == 0:
            yield index


# Successive Function call using for loop
for index in even():
    print(index)

print("======== Multiple yield Statement =========")


# Using multiple yield Statement
def multiple_yield():
    str1 = "Hi"
    yield str1

    str2 = 'Hello'
    yield str2

    str3 = "Good morning"
    yield str3


# obj is generator object
obj = multiple_yield()
print(obj)
print(type(obj))

print(next(obj))
print(next(obj))
print(next(obj))

print("======= Generator Expression ========")

# Generator Expression
# 1. We can easily create a generator expression without using user-defined function. It is the
#    same as the lambda function which creates an anonymous function; the generator's expressions create an anonymous
#    generator function.
#
# 2. The representation of generator expression is similar to the Python list comprehension.
#    The only difference is that square bracket is replaced by round parentheses.
#    The list comprehension calculates the entire list, whereas the generator expression calculates one item at a time.

# List Comprehension
list1 = [1, 2, 3, 4, 4, 5, 6, 7, ]
z = [x ** 2 for x in list1]

# Generator expression
a = (x ** 3 for x in list1)

print(z)
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

