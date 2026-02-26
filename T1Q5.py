from math import pi

radius = float(input('Radius: '))
height = float(input('Height: '))

volume = pi * radius**2 * height 

print(f"The volume of a cylinder with radius {radius:.2f} metres and height {height:.2f} metres is {volume:.2f} cubic metres.")