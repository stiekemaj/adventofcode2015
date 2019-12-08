input = open('day1.in').read()

# question 1
print('Question 1: ' + str(input.count('(') - input.count(')')))

# question 2
current_floor = 0
for i in range(len(input)):
    if input[i] == '(':
        current_floor += 1
    else:
        current_floor -= 1

    if current_floor == -1:
        print('Question 2: ' + str(i + 1))
        break
