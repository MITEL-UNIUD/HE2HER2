# Medical Informatics, Telemedicine & eHealth Lab
# University of Udine, Italy
# V.Della Mea, D.La Barbera and K.Roitero
#
import pandas as pd
import numpy as np
import os 

print("Generating final results.")

# Get absolute path
path = os.getcwd()
path = path.replace("\\", "/")
if len(path) > 1 and path[-1] != '/':
    path += '/'
    path = path.replace('code','')

# Working with data
data = pd.read_csv("her2_classification.csv")
# Getting image number foreach slide
aux = data["image_name"].str.split("_", n = 1, expand = True)
data["slide"] = aux[0]

# Rimuovo l'indecisione per i campi dove la rete non era in grado di decidere
data['tags'] = np.where(data['positive'] > data['negative'], '1-positive', '0-negative')

# Retrieving all slides list | Ho 150 slides di test
all_slides = set(np.unique(data["slide"]))

# Total number of tiles for each slide
df = data.groupby(by = ["slide"]).count()
df = df.drop(columns=['tags', 'negative', 'positive'])
df = df.rename(columns={"image_name": "tiles_count"})

# Counting for each slide number of pos and neg
tag_count = data.groupby(by = ["slide", "tags"]).count()
tag_count = tag_count.unstack()
tag_count = tag_count.fillna(0)
tag_count.columns = ['0-negative', '1-positive', 'a', 'b', 'c', 'd']
tag_count = tag_count.drop(columns=['a', 'b', 'c', 'd'])
df = df.merge(tag_count, left_index=True, right_index=True)

#df = df.merge(data_pos_0_35, left_index=True, right_index=True)
df["positive_ratio"] = round(df["1-positive"] / df["tiles_count"], 3)

# Relative 0.35 ratio
df['pred1'] = df.apply(lambda row: (0 if row.positive_ratio < .35 else 1), axis=1)


# Mean Pos
avg_pos = data
avg_pos = avg_pos[data["tags"] == "1-positive"]
avg_pos = avg_pos.drop(columns=[ 'image_name', 'tags', 'negative'])
avg_pos = avg_pos.groupby(["slide"]).mean()[["positive"]]
avg_pos.columns = ["mean_pos"]
avg_pos['mean_pos'] = avg_pos.apply(lambda row: round(row.mean_pos, 3), axis=1)

df = df.merge(avg_pos, how = "left", left_index=True, right_index=True)
# Fill per le slides che non hanno tiles positive 
df["mean_pos"] = df["mean_pos"].fillna(0)
df['pred2'] = df.apply(lambda row: (0 if row.mean_pos <= .66 else 1), axis=1)


# All mean
all_mean = data
all_mean = all_mean.groupby(["slide"]).mean()[["positive"]]
all_mean.columns = ["all_pos_mean"]

all_mean['all_pos_mean'] = all_mean.apply(lambda row: round(row.all_pos_mean, 3), axis=1)
df = df.merge(all_mean, left_index=True, right_index=True)
df['pred3'] = df.apply(lambda row: (0 if row.all_pos_mean < .5 else 1), axis=1)

df["pred_count"] = df['pred1'] + df['pred2'] + df['pred3']
df["her2"] = df.apply(lambda row: (0 if row.pred_count < 2 else 1), axis=1)
df = df.reset_index()

df.to_csv("log_corretto.csv", index = None, header=True)

#df.to_csv('prova.csv', index=False)
final_csv = df[["slide", "all_pos_mean", "her2"]]
final_csv.columns = ["caseID", "soft_prediction", "hard_prediction"]
final_csv.caseID = final_csv.caseID.astype(int)
final_csv = final_csv.sort_values(by = ["caseID"])
final_csv.to_csv ('mitel-uniud_corretto.csv', index = None, header=True)

# Removing temporary csv files
#if(os.path.exists("preclassified.csv")):
#    os.remove("preclassified.csv")
#if(os.path.exists("her2_classification.csv")):
#    os.remove("her2_classification.csv")

print("\nFile mitel-uniud.csv correctly generated.")