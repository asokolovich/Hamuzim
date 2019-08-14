import glob
import csv

#Locate all csv files in workspace and thier path
txtfiles = []
for file in glob.glob("$WORKSPACE/*.csv"):
    txtfiles.append(file)

#Create a new out put file to send in an Email

f= open("Final_output.txt","w+")

#Find all the relevent urls per site wuth higher than 70 score of fuzzyhash
for file in txtfiles:
    site = file[-8:-4]
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        flag = False
        for row in csv_reader:
            if row[9] > 70:
                if flag == False:
                    f.write("The site is: " + site + "\n" + row[0] + "," + row[1] + "," + row[2] + "," + row[9])
                    line_count += 1
                    flag = True
                else:
                    f.write(row[0] + "," + row[1] + "," + row[2] + "," + row[9] +"\n")
                    line_count += 1
            else:
                line_count += 1
f.close()
