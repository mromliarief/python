import csv

with open("C:/Users/Vivo Design/Documents/Phyton/00-Template/water_potability.csv","r") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
       print(row)
    
   