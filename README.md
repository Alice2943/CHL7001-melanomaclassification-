# Melanoma Classification by Using EfficientNets
## Introduction
This is the repository for our work on melanoma classification for CHL7001 Deep Learning. 

A benign tumour is a lump of cells that does not invade its surrounding tissue or spread around the body. A malignant tumour is a lump of cells that may invade its surrounding tissue or spread around the body. Malignant tumours cause cancer. Skin cancer is the most common of all cancers. Melanoma causes 75% of skin cancer deaths, despite the fact that it only accounts for 1% of skin cancers. The American Cancer Society estimates that there will be 100,350 new melanoma cases in the United States in 2020. Among them, 6850 people are expected to die of melanoma. 

In this project, we would like to use Deep Learning methods to predict whether images of skin lesions are of benign or malignant status

## Datasets

We used the International Skin Imaging Collaboration (ISIC) 2020 Challenge Dataset from the Kaggle website https://www.kaggle.com/c/siim-isic-melanoma-classification/overview. There are metadata and image datasets.
The metadata contains: 
- image_name - unique identifier, points to filename of related DICOM image
- patient_id - unique patient identifier
- sex - the sex of the patient (when unknown, will be blank)
- age_approx - approximate patient age at time of imaging
- anatom_site_general_challenge - location of imaged site
- diagnosis - detailed diagnosis information (train only)
- benign_malignant - indicator of malignancy of imaged lesion
- target - binarized version of the target variable

The image dataset was collected from multiple hospitals and organizations such as Hospital Clínic de Barcelona, Medical University of Vienna, and Memorial Sloan Kettering Cancer Centre. The dataset contains 33,126 dermoscopic images of 32,542 benign and 584 malignant skin lesions from 2056 patients. The images are provided in the JPEG format and were converted into pixels later. There are various image sizes ranging from 640 × 480 to 6000 × 4000.

## Data Augmentation

![](/image/preprocessing.png)
