#Task2 ask us to read data from a txt file

#As usual, we need to import packages we need
import matplotlib.pyplot as plt 
#This is not a csv file so we don't import csv package

#Then we need two empty lists to store our data
wavelengths=[]
intensities = []

#Tell the program where is the file
file_path = r"C:\Users\13822\Desktop\CHEM0062\Project 1\proj_2.txt" #Don't forget r at front, otherwise it will recognize \ as a meaningful function

#Now we can open up the file using with and open function 
with open(file_path,'r')as file:
    for lines in file:#Read all data in the file    
        try:
            parts=lines.split()
            wavelength = float(parts[0])
            intensity = float(parts[3])-float(parts[1])
            #using two variables to store data
            wavelengths.append(wavelength)
            intensities.append(intensity)
            #Adding data to the empty list
        except:
            print(f"Skipping values:{lines.strip()}")#Tell us what's being skipped
#Then we can use our lists to plot the graph
plt.figure(figsize=(10,6))#Tell the program how large we want the graph to be
plt.plot(wavelengths,intensities,color='blue',linewidth=1)#Enter the information of x-values and y-values

#Don't title,x-label and y-label
plt.title("Iodine Spectrum")
plt.xlabel("Wavelength(nm)")
plt.ylabel("Intensity(a.u.)")

#In the end, we need to show the graph
plt.show()            