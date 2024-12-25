'''
15. Sphere Volume Calculator

Write a Python program to get the volume of a sphere with radius six.
'''

from math import pi

# radius of sphere
r = 6

# formula for volume of sphere
volume_sphere = (4/3) * pi * (r**3)

print(f"Volume of sphere is:", volume_sphere)
# Volume of sphere is: 904.7786842338603

print(f"Volume of sphere is:", round(volume_sphere, 2))
# Volume of sphere is: 904.78