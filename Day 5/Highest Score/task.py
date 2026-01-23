student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

sum = 0
# The variable score has been assigned to each of the values in the student_scores list
for score in student_scores:
    # in the code, the += is assigning a new added value to sum with every loop
    sum += score
    # This print statement is indented into the for loop code block hence the printing is part of the look
    # The code executes vertically downwards in the block and once it finishes
    # looping is when it will move on to the next independent line or code block.
print(sum)
max_score = 0
for number in student_scores:
    if number > max_score:
        max_score = number

print(max_score)
