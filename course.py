# A file that defines the class Course
# it contains the course information and the current grade

import os
import numpy

#function that calculates the weighted summation
#vectorization can be applied
def weight_sum(list1, list2):
    sum = numpy.dot(list1, list2)
    return sum


class Course:

    #constructor
    def __init__(self, _cname):
        self.name = _cname;
        self.grade_name = [];
        self.grade_weight = [];
        self.grade_score = [];

    #load the score
    #_gname is a list of strings indicating the content
    #_gwght is a list of doubles for score weight in hundred percentage
    #_gscro is a list of doubles for actual score in hundred percentage
    def load_score(self, _gname, _gwght, _gscro):
        self.grade_name = _gname
        self.grade_weight = _gwght
        self.grade_score = _gscro
    
    
    #adding a grade entry to the Course
    def add_grade(self, entry, weight, score):
        self.grade_name.append(entry)
        self.grade_weight.append(weight)
        self.grade_score.append(score)


    #delete a grade from the course
    #given an entry name, delete the entry from the course
    def delete_entry(self, entry_name):
        size = len(self.grade_name)
        for i in range(0, size):
            if self.grade_name[i] == entry_name:
                self.grade_name = self.grade_name[: i] + self.grade_name[i + 1:]
                self.grade_weight = self.grade_weight[: i] + self.grade_weight[i + 1:]
                self.grade_score = self.grade_score[: i] + self.grade_score[i + 1:]
                print "The entry of the name: " + entry_name + " is successfully removed"
                return

        print "There is no such entry name in this course"
        print "Please double check your input"
        return


    #input a target score, return an expectation of mean percentage
    #of the following score entry
    def target_grade(self, target):
        grade = weight_sum(self.grade_weight, self.grade_score) / 100.0
        difference = target - grade

        if difference <= 0:
            print "You have already reached your expected grade. Congrats"
            return
        else:
            must_achieve = difference / (100 - sum(self.grade_weight)) * 100
            print "You need to score at least " + str(must_achieve) + "% in the future to score you expected score"
            return 


    #print all the grades currently have in a nice fashion
    def print_course(self):
        print "\n"
        print "           " + "Course Name: " + self.name
        print "__________________________________________________"
        print "|         Entry        |    Weight  |    Score   |"
        print "--------------------------------------------------"
        
        i = 0
        size = len(self.grade_name)
        while (i < size):
            width = 20
            print "|" + self.grade_name[i].rjust(width) + "  |",
            width = 9
            str_number = str(self.grade_weight[i])
            print str_number.rjust(width) + "  |",
            str_number = str(self.grade_score[i])
            print str_number.rjust(width) + "  |"
            i = i + 1
        print "--------------------------------------------------"
        width = 20
        print "|" + "Sum all the Grade".rjust(width) + "  |",
        width = 10
        str_number = str(sum(self.grade_weight)) + " / 100"
        print str_number.rjust(width) + " |",
        #Needs to calculate the latest weighted sum
        width = 4
        str_number2 = str(weight_sum(self.grade_weight, self.grade_score) / 100.0)
        print str_number2.rjust(width) + " / 100" + " |"
        print "\n\n"
