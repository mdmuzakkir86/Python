# python code which takes string as input and returns each character appended with its repetition count.
# Ex : Input – aabbbcca   Output – a2b3c2a1


# Creating a function
def count_string(any_string):

    previous = any_string[0]   # Adding 1st char of string to 'previous' variable
    count = 0                  # 'count' is set to 0
    index = 1                  # 'index' is set to 1 because 0 is already stored in 'previous'
    output = ''                # 'output' is empty, in this character and count are appending

    while index < len(any_string):

        if any_string[index] == previous:              # if any_String[index] char matches previous char
            count += 1                                 # count is increased by 1
        else:                                          # in case any_String[index] != previous
            output = output + previous + str(count)   # char and count are appended
            previous = any_string[index]               # 'previous' set to current string 'index'
            count = 1                                  # count is set to 1 again

        if index == len(any_string) - 1:               # To print the last character and count
            output = output + previous + str(count)

        index += 1  # increasing index value by 1
    print(output)


text = input("Enter a String to count: ")
count_string(text)
