import numpy as np

from course import *

test = Course("ECE345")

name = ["quiz1", "assignment1", "assignment2", "midterm"]
weight = [12, 10, 10, 10]
score = [86, 70, 90, 80]


print "Total" + str(sum(weight))


test.load_score(name, weight, score)

test.print_course()

for i in range(0, len(name)):
    print name[i]