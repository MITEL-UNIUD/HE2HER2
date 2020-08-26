# HE2HER2
This repository contains software developed to participate to the HEROHE Challenge (recognition of HER2 status from HE slides). 

If you use the software, please cite it as:
*Della Mea V, Polonia A, La Barbera D, Conde-Sousa E, Roitero K. Detection of HER2 from Haematoxylin-Eosin Slides Through a Cascade of Deep Learning Classifiers via Multi-Instance Learning. J. of Imaging, 2020, in press*.

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

