# LAB 2 - Tahimik, Allysa

##### Part 1 (30 pt) #####
# Take the following list and multiply all list items together.
# part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
answer1 = 1

for i in part1:
    answer1 = answer1 * i

print("The result of the list multiplied is: ", answer1)

##### Part 2 (30 pt) #####
# Take the following list and add all list items together
# part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
answer2 = 0

for i in part2:
    answer2 = answer2 + i

print("The result of the list added all together is: ", answer2)

##### Part 3 (40 pt) #####
# Take the following list and only add together those list items which are even. 
# part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
# isEven = num1 % 2 == 0

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
answer3 = 0

for i in part3:
    if i % 2 ==0:
        answer3 = answer3 + i

print("The result of all even numbers in the list added all together is: ", answer3)