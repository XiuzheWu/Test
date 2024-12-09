'''
CSV file is an easy way to store data, data is separated by comma
'''
#First of all we need import package we need
import matplotlib.pyplot as plt #package used to plot graph
import numpy #package that can carry out maths calculation
import csv #import csv to read the csv file

#We need to read our file now, but we have to point out the location of the file
file_path = r"C:\Users\13822\Desktop\CHEM0062\Project 1\proj_1.csv"
#notice that I put an 'r' at the front, this is because the path contains '\' which has specific meaning in python
output_file = 'processed_proj_1.csv'
#if we are plotting a graph of intensity against wavelength, we need to lists to store the data
wavelengths = []
intensities = []

# Header 
header_info = {}

#now we can read our file
with open(file_path,'r') as file: #'r'means only read the file without editing it 
    reader = csv.reader(file)
    
    #once we have read the file,we can search our data now
    for row in reader:
        try:#we use try here because headers are not float
            wavelength = 1239.84/(float(row[0]))
            intensity = float(row[3])-float(row[1]) #row 3 is the measured intensity, we need to minus the baseline
            
            wavelengths.append(wavelength)
            intensities.append(intensity)
            
        except ValueError:
            if len(row)>1:
                key = row[0].strip()
                value = row[1].strip()
                header_info[key]=value

with open(output_file,'w',newline='') as file:
    writer = csv.writer(file)
    
    for key,value in header_info.items():
        writer.writerow([f'#{key}:{value}'])
        
    for w, i in zip(wavelengths,intensities):
        writer.writerow([w,i])

print("Header information:")
print(header_info)
for key,value in header_info.items():
    print(f"{key}:{value}")

plt.figure(figsize=(10,6))
plt.plot(wavelengths,intensities,color='blue',linewidth=1)

plt.title('Iodine spectrum')
plt.xlabel('Wavelength(eV)')
plt.ylabel("Intensities(a.u.)")

plt.show()