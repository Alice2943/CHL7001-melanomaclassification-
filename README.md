# Melanoma Classification by Using EfficientNets
## Our objective

This is the repository for our work on melanoma classification for CHL7001 Deep Learning. 

A benign tumor is a lump of cells that does not invade its surrounding tissue or spread around the body. A malignant tumor, on the other hand, is a lump of cells that may invade its surrounding tissue or spread around the body. The presence of malignant tumors have the potential to cause cancer. In this project, we would like to use Deep Learning methods to predict whether images of skin lesions are of benign or malignant status

## Introduction

A benign tumour is a lump of cells that does not invade its surrounding tissue or spread around the body. A malignant tumour is a lump of cells that may invade its surrounding tissue or spread around the body. Malignant tumours cause cancer. Skin cancer is the most common of all cancers [1]. Melanoma causes 75% of skin cancer deaths, despite the fact that it only accounts for 1% of skin cancers. The American Cancer Society estimates that there will be 100,350 new melanoma cases in the United States in 2020. Among them, 6850 people are expected to die of melanoma. 

## Datasets
We used the International Skin Imaging Collaboration (ISIC) 2020 Challenge Dataset from the Kaggle website. There are metadata and image datasets.
The metadata contains: 
- image_name - unique identifier, points to filename of related DICOM image
- patient_id - unique patient identifier
- sex - the sex of the patient (when unknown, will be blank)
- age_approx - approximate patient age at time of imaging
- anatom_site_general_challenge - location of imaged site
- diagnosis - detailed diagnosis information (train only)
- benign_malignant - indicator of malignancy of imaged lesion
- target - binarized version of the target variable

