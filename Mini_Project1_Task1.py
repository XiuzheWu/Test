#If we are going to read data from a csv file and plot graph, we need two packages
import csv
import matplotlib.pyplot as plt

#We first need to create two lists to store data
wavelengths = []
intensities =[]

#We need to tell the system where is the file, I will create a variable that stores where is the file
file_path = r"C:\Users\13822\Desktop\CHEM0062\Project 1\proj_1.csv"
'''
Be aware that there is '\' in the string, this symbol has certain function
so I add a r at the front to make '\' a word
'''
#For headers in the csv file, we need to a dictionary to store each name 

header_info = {}

#Now we read the file using 'with' function
with open(file_path,'r')as file:
    #'r' means we are only reading the file, using 'as' so that we don't need to type file_path every time
    reader = csv.reader(file) #use reader function in the csv package to read the file and create a variable to store all data in the file
    
    for row in reader:
        try:#There are words in the file refering to what are the data
            wavelength = float(row[0])#Open the file with txt, we found that all data have decimal place which means they are float type
            intensity = float(row[3])-float(row[1])#row[1] is baseline, to get real intensity we need to 
            
            wavelengths.append(wavelength)
            intensities.append(intensity) #Then we add the values into the lists we prepared
           
        except ValueError:#We need to tell the program how to deal with those words
            if len(row)>1:
                key=row[0].strip()
                value=row[1].strip()
                header_info[key]=value

print("Header Information")
print(header_info)
for key,value in header_info.items():#items function put key and value into a tuple
    print(f"{key}:{value}")
    
plt.figure(figsize=(10,6))
plt.plot(wavelengths,intensities,color='blue',linewidth=1)

plt.title('Iodine Spectrum')
plt.xlabel('Wavelength(nm)')
plt.ylabel('Intensity(a.u.)')

plt.show()    