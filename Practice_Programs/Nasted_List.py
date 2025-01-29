if __name__ == '__main__':
    # records = [['Rachel', -50],['Mawer', -50], ['Sheen', -50], ['Shaheen', 51]]
    records = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    # records = [['Harsh', 20],['Beria', 20], ['Varun', 10], ['Kakumari', 19], ['Vikas', 21]]
    # records = [['Test1', 52], ['Test2', 53], ['Test3', 53]]

    # for _ in range(int(input())):
    #     name = input()
    #     score = input()

    #     records.append([name, score])

    # Sorting records list based on score
    records.sort(key=lambda x: x[1])
    print('records = ', records)

    # Storing first sub-list score in 'k' to compare with other variables
    lowestScore = records[0][1]
    print("lowestScore=", lowestScore)

    # Storing Second lowest score in 'second_lowest_score'
    second_lowest_score = None

    # iterating records
    for i in records:

        # if first sublist score (i,e k) is not equal to current sublist score then it is a second_lowest_score
        # if second_lowest_score is equal to current sublist score then loop will be break to avoid second_lowest_score to be modify
        if lowestScore != i[1]:
            print('i[i]= ', i[1])
            second_lowest_score = i[1]
            if second_lowest_score == i[1]:
                break

    # result_set list to store second_lowest_score records (i,e list)
    result_set = []
    print('second_lowest_score=', second_lowest_score)

    # Iterating records and checking second_lowest_score records(list) in it
    # if available append it to result_set
    for i in records:
        if i[1] == second_lowest_score:
            result_set.append(i)

    # Sort the result based on alphabets
    result_set.sort(key=lambda x: x[0])
    print('result_set = ', result_set)

    # Iterating result set and printing names of second_lowest_score guys
    for name, score in result_set:
        print(name)
