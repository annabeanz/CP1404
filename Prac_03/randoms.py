import random

dir(str)
dir(random)
help(random.randint)
help(random.randrange)

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?"""
# Produces an integer between 5 and 20 (both inclusive), 5, 20

"""
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?"""
# Produces a random number between 3 and 10 (inclusive 3, excludes 10), with a step value of 2
# so numbers 3 + 2n can be generated, every 2n'd number from 3
# 3, 9

"""
What did you see on line 3?
What was the smallest number you could have seen, what was the largest?"""
# Produces a random float between 2.5 and 5.5 (both inclusive)

print(random.randint(0, 100))
