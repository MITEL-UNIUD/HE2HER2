# Medical Informatics, Telemedicine & eHealth Lab
# University of Udine, Italy
# V.Della Mea, D.La Barbera and K.Roitero
#
import os
import sys
import glob
import shutil

print("Removing not cancer tiles.")
# Retrieving absolute path
path = os.getcwd()
path = path.replace("\\", "/")
if len(path) > 1 and path[-1] != '/':
    path += '/'
print(path)

# Creating directory structure if not exists
if not os.path.exists(path  + "noncancer"):
    os.makedirs(path  + "noncancer")
    print("Dirs created.")

# Retrieving .csv files
csv = "preclassified.csv"
print("Currently working on {}".format(csv))
# Setting up urrent directories
noncancer_path = path + "noncancer/"
current_working_dir = path + "tiles/"
with open(csv) as fin:
    next(fin) # Skipping header line
    for line in fin:
        current_line = line.split(",")
        if(current_line[1] != "cancer"):
            if(os.path.exists(current_working_dir + current_line[0] + ".jpg")):
                shutil.move(current_working_dir + current_line[0] + ".jpg", noncancer_path + current_line[0] + ".jpg")
            else:
                shutil.move(current_working_dir + current_line[0] + ".png", noncancer_path + current_line[0] + ".png")

print("Done.")
print("Cancer tiles removed.")