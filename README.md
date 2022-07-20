# HE2HER2
This repository contains software developed to participate to the HEROHE Challenge (recognition of HER2 status from HE slides). 

The data set is described in: 
*Eduardo Conde-Sousa, João Vale, Ming Feng, Kele Xu, Yin Wang, Vincenzo Della Mea, David La Barbera, Ehsan Montahaei, Mahdieh Soleymani Baghshah, Andreas Turzynski, Jacob Gildenblat, Eldad Klaiman, Yiyu Hong, Guilherme Aresta, Teresa Araújo, Paulo Aguiar, Catarina Eloy, António Polónia. HEROHE Challenge: assessing HER2 status in breast cancer without immunohistochemistry or in situ hybridization.* https://arxiv.org/abs/2111.04738 .
If you use it, please cite the paper.


If you use this software, please cite it as:
*La Barbera, D.; Polónia, A.; Roitero, K.; Conde-Sousa, E.; Della Mea, V. Detection of HER2 from Haematoxylin-Eosin Slides Through a Cascade of Deep Learning Classifiers via Multi-Instance Learning. J. Imaging 2020, 6, 82.* https://doi.org/10.3390/jimaging6090082 

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

