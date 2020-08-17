# Medical Informatics, Telemedicine & eHealth Lab
# University of Udine, Italy
# V.Della Mea, D.La Barbera and K.Roitero
#
#Fastai based classification
#import fastai
from fastai import *
from fastai.vision import *
from zipfile import ZipFile
import pandas as pd
import numpy as np
import os 

print ("Identifying Cancer.")
#Setup: path should contain the test tiles, and an export.pkl from Fastai
#e.g., mv pre-classification-densenet201-6+6.pkl preclass/export.pkl
path = os.getcwd()
path = path.replace("\\", "/")
if len(path) > 1 and path[-1] != '/':
    path += '/'
    path = path.replace('code','')

#load model associated to test images
herohe = ImageList.from_folder(path + 'tilestrain/A0')
iciar_model = load_learner(path + "models", "cancer_identify.pkl", test = herohe)

#prediction
preds, y = iciar_model.get_preds(ds_type = DatasetType.Test)


print(iciar_model.model)
print("___________________________________________________")
print(iciar_model.summary())

assert False

#Initially set at 0.501, better to increase to 0.75
thresh = 0.75
labelled_preds = [' '.join([iciar_model.data.classes[i] for i,p in enumerate(pred) if p > thresh]) for pred in preds]
fnames = [f.name[:-4] for f in iciar_model.data.test_ds.items]
df = pd.DataFrame({'image_name':fnames, 'tags':labelled_preds, 'cancer':preds.numpy()[:, 0], 'no':preds.numpy()[:, 1]}, 
                  columns=['image_name', 'tags','cancer','no'])
df.to_csv('preclassified.csv', index=False)
# the preclassified.csv file contains file names, class with pred>0.75, and soft predictions. 
#This should be used to move away/delete image files not belonging to the cancer class
print("Cancer Identified.\n")