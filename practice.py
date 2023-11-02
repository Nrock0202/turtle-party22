#Data Project Practice
# Norris Knight

#import csv
import statistics

def output_stats(list):
    print("Spring 2016:                               ",
          "Fall 2016")
    print("Mean     ",   statistics.mean(spring),"               ",
                         statistics.mean(fall)   )
    print("Median   ",   statistics.median(spring),"             ",
                         "              ",
                         statistics.median(fall) )
    print("Std Dev  ",   statistics.stdev(spring),
                         "              ",
                         statistics.stdev(fall)  )

    print()




# Data variables
spring = []
fall = []
#read in the file
csv = "sample_grade.csv"
file = open(csv)
for line in file:
    # print(line())
    list = line.rstrip().split(",")

    #print the(list)
    if list[1] == 'Spring 2016':
       spring.append(eval(list[2]))
    else:
       fall.append(eval(list[2]))

file.close()

#print("Spring 2016:")
output_stats(spring)

#print("Fall 2016:")
output_stats(fall)
