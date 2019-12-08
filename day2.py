presents = open('day2.in').read().split()

wrapping_paper = 0
ribbon = 0
for present in presents:
    dimensions = [int(x) for x in present.split('x')]
    dimensions.sort()
    wrapping_paper += (dimensions[0] * dimensions[1] * 3 +
                       dimensions[1] * dimensions[2] * 2 +
                       dimensions[0] * dimensions[2] * 2)

    ribbon += (dimensions[0] * 2 +
               dimensions[1] * 2 +
               dimensions[0] * dimensions[1] * dimensions[2])

print('Answer 1: ' + str(wrapping_paper))
print('Answer 2: ' + str(ribbon))

