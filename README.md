# HE2HER2
This repository contains software developed to participate to the HEROHE Challenge (recognition of HER2 status from HE slides). 

The data set and the challenge are described in: 
Conde-Sousa E, Vale J, Feng M, Xu K, Wang Y, Mea VD, Barbera DL, Montahaei E, Baghshah M, Turzynski A, Gildenblat J, Klaiman E, Hong Y, Aresta G, Araújo T, Aguiar P, Eloy C, Polónia A. HEROHE Challenge: Predicting HER2 Status in Breast Cancer from Hematoxylin–Eosin Whole-Slide Imaging. *Journal of Imaging.* 2022; 8(8):213. https://doi.org/10.3390/jimaging8080213

If you use it, please cite the paper.


If you use this software, please cite it as:
La Barbera D, Polónia A, Roitero K, Conde-Sousa E, Della Mea V. Detection of HER2 from Haematoxylin-Eosin Slides Through a Cascade of Deep Learning Classifiers via Multi-Instance Learning. *Journal of Imaging.* 2020; 6(9):82. https://doi.org/10.3390/jimaging6090082 

## Content Description

In this section we detail the content of the repository.

### Code

The only folder *pipeline* contains the devoloped code. We used the format **STAGE_number** to match each script with the corresponding stage in the developed pipeline. The folder contains the following scripts:

- **STAGE_1_patch_extraction.py**: details the code developed to extract the patches of the given size from the slides;
- **STAGE_2B_PART1_preclassify.py**: details the code developed to identify cancer in the extracted patches;
- **STAGE_2B_PART2_move_notcancer.py**: details the code developed to remove patches for which no cancer has been identified;
- **STAGE_3_her2classify.py**: details the code developed to identify her2 in the extracted patches;
- **STAGE_4_5A_generate_output.py**: details the code developed to compute the output using the majority vote method;
- **STAGE_4_5B_tabular_model_generation.ipynb**: details the code developed to compute the output using the tabular classifier method.

### Models

Due to too large file dimensions, we share the developed models via [Google Drive](https://drive.google.com/drive/folders/1xzcfgugSd3wDUq1FxrYIUFO-LZOwgDxY?usp=sharing). Inside that folder you can find:

- **cancer_identify.pkl**: the developed network used to identify cancer on patches;
- **resnet152-prec-norm-3.pkl**: the developed network used to identify her2 on patches.

