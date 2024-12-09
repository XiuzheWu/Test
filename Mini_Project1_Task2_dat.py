import matplotlib.pyplot as plt

wavelengths = []
intensities = []

file_path = r"C:\Users\13822\Desktop\CHEM0062\Project 1\proj_3.dat"

with open(file_path,'r') as file:
    for lines in file:
        parts = lines.split()
        wavelength = float(parts[0])
        intensity = float(parts[3])-float(parts[1])
        wavelengths.append(wavelength)
        intensities.append(intensity)
        
plt.figure(figsize=(10,6))
plt.plot(wavelengths,intensities,color='black',linewidth=1)

plt.title("Iodine Spectrum")
plt.xlabel("Wavelength(nm)")
plt.ylabel("Intensity(a.u.)")

plt.show()