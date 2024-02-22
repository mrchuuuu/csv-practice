import csv
import time

def csv_main():
    
    theLoop = True
    while theLoop:
        csv_add()
        
        choice = input("Do you still want to add more students? y/n ")
        
        if choice == 'y' or choice == 'Y' :
            
            theLoop = True

        else :
            theLoop = False
    
    time.sleep(2) 
    print("Data Entered!!")
    
def csv_add():
    
    with open('./data/studentData.csv', 'a') as studentFile:
        writeData = csv.writer(studentFile, delimiter = '\t')
        
        studentName = input('Enter Student Name: ')
        studentId = input('Enter Student ID# YYYY-MMMM: ')
        studentYear = input('Enter Student Year Level: ')
        studentGender = input('Enter Student Gender: ')
    
        studentData = [studentName, studentId, studentYear, studentGender]
        writeData.writerow(studentData)
        
        studentFile.close()    
        
if __name__ == "__main__":

    print("Program Executing..")
    time.sleep(2)
    
    csv_main()    
    
    
    
    
    
        
    
    
