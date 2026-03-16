import csv
import sys

def load_data():
    data = []
    with open('Data/testdata - Sheet1.csv') as csvfile: 
        # Return a reader object which will 
        # iterate over lines in the given csvfile. 
        readCSV = csv.reader(csvfile, delimiter=',') 
        for row in readCSV: 
            data.append(row)
    return data

def get_cell(data,row, column):
    '''
    Arguments:  data (list of lists)
                row (int)
                column (int)
    Returns: cell value
    Purpose: Returns the value at the specified row and column from the data'''
    return data[row][column]

def multiply(a, b):
    '''
    Arguments: a (int or float)
               b (int or float)
    Returns: product (int or float)
    Purpose: Multiplies two numbers'''
    return a * b

def get_email(data, username):
    '''
    Arguments:  data (list of lists)
                username (string)
    Returns: email (string)
    Purpose: Returns the email corresponding to a unique username'''
    for row in data[1:]:
        if row[0] == username:
            return row[1] 
            
    return ""

def get_all_usernames(data):
    '''
    Arguments: data (list of lists)
    Returns: list of usernames (list of strings)
    Purpose: Returns a list of all usernames from the data'''
    usernames = []
    for row in data[1:]:
        usernames.append(row[0])
    return usernames


def string_to_int(string):
    '''
    Arguments: s (string representing an integer e.g. '123')
    Returns: integer value of the string
    Purpose: Converts a numeric string to an integer'''
    return int(string)

def main():
    pass

if __name__ == "__main__":
    main()