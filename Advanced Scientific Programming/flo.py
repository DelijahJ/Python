# Author:         Delijah Joseph
# Major:          Information Technology
# Creation Date:  February 12, 2022
# Due Date:       February 18, 2022
# Course:         CSC223
# Professor Name: Professor Earl 
# Assignment:     #2
# Filename:       main.py
# Purpose:        Python File Input/Output, Using Python Data Structures

def get_data(filename):
    """
Description: Takes a filename and returns standard sales and a list of lists of floats
Parameters: str filename: name of file to be opened -input
Return Values: list standard - list of standard sales, list lines - list of lists of floats
    """
    f = open(filename)

    lines = list()
    standard = f.readline()
    standard = standard.split()
    
    for i in range(len(standard)):
        standard[i] = float(standard[i])

    for line in f:
        line = line.strip().split()
        for i in range(len(line)):
            line[i] = float(line[i])
        lines.append(line)

    return standard,lines

def process_data(data):
    """
Description: Take list of floats and list of standard sales and returns a list of dictionaries.
Parameters: list data: list of standard sales, list of floats 
Return Values: list of dictionaries
    """
    final = []
    Department = []
    Average = []
    Above = []
    Below = []
    Performance = []
    dicts = {}
    
    for n in range(0,len(data[1])):
        Department.append(n+1) 
        tot = 0
        above = 0
        below = 0
        for i in range(0,len(data[1][0])):
            tot = tot + data[1][n][i]
            avg = tot/12
            if data[0][i] <= data[1][n][i]:
                above += 1
                
            if data[0][i] > data[1][n][i]:
                below += 1
        
        Average.append("%.1f" % avg)
        Above.append(above)
        Below.append(below)
        if below > 5:
            Performance.append('unsatisfied')
        else:
          Performance.append('satisfied')  

    for i in range(0,len(data[1])):
    
        dicts['Department'] = (Department[i])
        dicts['Average'] = (Average[i])
        dicts['Above'] = (Above[i])
        dicts['Below'] = (Below[i])
        dicts['Performance'] = (Performance[i])
        final.append(dicts.copy())
    
    return(final)
        
def write_to_file(processed):
    """
Description: Writes list of dictionaries to out.dat file
Parameters: list of dictionaries
Return Values: none
    """
    
    f = open('out.dat', 'w')
    f.write("Department, Average, Above, Below, Performance\n")
    for n in range(0,len(processed)):
       
        f.write(str(processed[n]['Department']))
        f.write(", ")
        f.write(str(processed[n]['Average']))
        f.write(", ")
        f.write(str(processed[n]['Above']))
        f.write(", ")
        f.write(str(processed[n]['Below']))
        f.write(", ")
        f.write(str(processed[n]['Performance']))
        f.write("{0}".format('\n'))
    f.close()

def main():
    """
    Description: Prompts user for a filename and calls the other functions with appropriate arguments
    Parameters: none
    Return Values: none
    """
    filename = input("Enter the file imput name: ")
    data = get_data(filename)
    processed = process_data(data)
    write_to_file(processed)
   
main()