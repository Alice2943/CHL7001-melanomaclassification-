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

## Exploratory data analysis

We performe EDA on the metadata, trying to understand the data structure.
There are 424 duplicated images that are removed from the subsequent exploratory data analysis (EDA)and modelling.  Most patients have under 20 images.
![](/image/Picture1.png)

The maximum number ofimages for one patient is 115.There are 1000 more male patients compared to female patients. 
![](/image/Picture2.png)

The mean ageis roughly around 50 years old (See figure 3 in appendix A). 
![](/image/Picture3.png)

The highest number of images is taken for torsoand least number of images is taken for oral/genital (i.e.  52% for torso and 0.386% for oral/gentital). 
![](/image/Picture4.png)
![](/image/Picture5.png)

There are around 30,000 more benign images compared to malignant images(See figure 6 in appendix A). 
![](/image/Picture6.png)

Lastly, most images have unknown diagnosis whereas 584 images are diagnosedwith melanoma.
![](/image/Picture17.png)

The distributions of age for both genders are similar.
![](/image/Picture8.png)

For every anatomy size,the  mean  age  is  around  50  years  old  with  a  range  of  15  to  90  years  old.  
![](/image/Picture9.png)

Thedistribution of age for melanoma diagnosis ranges from 17 to 90 years old.
![](/image/Picture10.png)

2.2%of male patients and 1.4% of female patients have malignant tumors.
![](/image/Picture11.png)

For  female  patients,  the  distribution  of  age  is  roughly  the  same  for  patients  with  benign  and  malignanttumors with mean age of 50 years old.For male patients, the mean age for gettingmalignant tumors is around 70 years old and for getting benign tumors is around 45 years old.
![](/image/Picture12.png)

Three variables have missing values among five variables.  Anatomy site has the highest number of missingvalues of 526,  which accounts for 1.6% of total values. Age has 3 more missingvalues than sex and both variables account for 0.1% of total values.

\begin{table}
\centering
\caption{Missing values with its percentage of total values.}
\begin{tabular}{l|ll}
              & Missing Values & \% of Total values  \\ 
\hline
Anatomy sites & 526            & 1.6                 \\ 
\hline
Age           & 44             & 0.1                 \\ 
\hline
Sex           & 41             & 0.1                
\end{tabular}
\end{table}


## Data Preprocessing

![](/image/preprocessing.jpg)
