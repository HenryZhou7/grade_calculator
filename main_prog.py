from course import *

test = Course("ECE345")

name = ["quiz1", "assignment1", "assignment2", "midterm"]
weight = [12, 10, 10, 10]
score = [86, 70, 90, 80]

test.load_score(name, weight, score)

test.print_course()

print "Target grade:"
test.target_grade(20)

print "Adding an entry:"
test.add_grade("assignment4", 5, 90)
test.print_course()

print "Deleting an entry:"
test.delete_entry("quiz1")
test.print_course()