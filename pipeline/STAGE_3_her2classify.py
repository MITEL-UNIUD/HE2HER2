# Medical Informatics, Telemedicine & eHealth Lab
# University of Udine, Italy
# V.Della Mea, D.La Barbera and K.Roitero
#
#Fastai based classification
# 
from fastai import *
from fastai.vision import *
import numpy as np
import pandas as pd
import os

from zipfile import ZipFile

print ("Identifying HER2 Status.")
#Setup: path should contain the test tiles, and an export.pkl from Fastai
#e.g., cp resnet152-3.pkl export.pkl

path = os.getcwd()
path = path.replace("\\", "/")
if len(path) > 1 and path[-1] != '/':
    path += '/'
    path = path.replace('code','')

#load model associated to test images
#herohe=ImageList.from_folder('valid/1-positive/')
#herohe=ImageList.from_folder('valid/0-negative/')
herohe = ImageList.from_folder(path + 'tiles')
her2_model = load_learner(path + "models", "resnet152-prec-norm-3.pkl", test=herohe)

# prediction
preds, y = her2_model.get_preds(ds_type = DatasetType.Test)
#Initially set at 0.501 
thresh = 0.501
labelled_preds = [' '.join([her2_model.data.classes[i] for i,p in enumerate(pred) if p > thresh]) for pred in preds]
fnames = [f.name[:-4] for f in her2_model.data.test_ds.items]
df = pd.DataFrame({'image_name':fnames, 'tags':labelled_preds, 'negative':preds.numpy()[:, 0], 'positive':preds.numpy()[:, 1]}, 
                  columns=['image_name', 'tags','negative','positive'])
df.to_csv('her2_classification.csv', index=False)
