# Add python code in this file
#triangle area from three points 

import os.path
import csv
def calculateArea (x1, y1, x2, y2, x3, y3):
    return abs ((x1*(y2-y3) + x2 *(y3 -y1) + x3 *(y1-y2))/2.0 )


def check (x1,y1, x4, y4, x,y):
    x2 = x4
    y2 = y1
    x3 = x1
    y3 = y4
    
    rectangleArea = 2 * calculateArea(x1, y1, x2, y2, x3, y3)
    
    A1 = calculateArea(x1, y1, x2, y2, x, y)
    A2 = calculateArea(x1, y1, x, y, x3, y3)
    A3 = calculateArea(x, y, x2, y2, x4, y4)
    A4 = calculateArea(x, y, x3, y3, x4, y4)
    
    return (A1+A2+A3+A4) == rectangleArea






def isInCity(x,y):
    with open('cities.csv') as cities_file:
        cities_reader = csv.reader(cities_file, delimiter=',')
        line_count = 0
        for row in cities_reader:
            if line_count == 0: 
                line_count += 1
                continue
            city = row[0]
            x1 = int (row[1])
            y1 = int (row[2])
            x4 = int (row[3])
            y4 = int (row[4])
            line_count += 1
            isExist = check(x1, y1, x4, y4, x, y)
            if isExist :
                return city
            
    return "None"


def writeToOutput (row):
    file_exists = os.path.isfile('output_points.csv')
    
    with open('output_points.csv','a') as output_file:
        headers = ['ID', 'X', 'Y', 'City']
        writer = csv.writer(output_file, delimiter=',', lineterminator='\n')
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(row)
    
    
def main ():
    with open('points.csv') as points_file:
        points_reader = csv.reader(points_file, delimiter=',')
        line_count = 0
        for row in points_reader:
            if line_count == 0: 
                line_count += 1
                continue
            iD = row[0]
            x = int (row[1])
            y= int (row[2])
            
            city = isInCity(x,y)
            newRow = [iD, x, y, city]
            writeToOutput(newRow)
            
    
if __name__ == '__main__':
    main()
    