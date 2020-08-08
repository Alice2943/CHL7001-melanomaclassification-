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

The image dataset was collected from multiple hospitals and organizations such as Hospital Clínic de Barcelona, Medical University of Vienna, and Memorial Sloan Kettering Cancer Centre. The dataset contains 33,126 dermoscopic images of 32,542 benign and 584 malignant skin lesions from 2056 patients. The images are provided in the JPEG format and were converted into pixels later. There are various image sizes ranging from 640 × 480 to 6000 × 4000. The image sets were randomly divided into 80% training and 20% validating data. Therefore, there are 26500 images in the training set and 6626 images in the testing set.

The process of randomly splitting the datasets is in the split.R file. We randomly split the provided metadata and create two sepearate files named "train.csv" and "test.csv".

## Exploratory data analysis

We performe EDA on the metadata, trying to understand the data structure.
There are 424 duplicated images that are removed from the subsequent exploratory data analysis (EDA)and modelling.  Most patients have under 20 images.
![](/image/Picture1.png)

The maximum number ofimages for one patient is 115.There are 1000 more male patients compared to female patients. 
![](/image/Picture2.png)

The mean ageis roughly around 50 years old. 
![](/image/Picture3.png)

The highest number of images is taken for torsoand least number of images is taken for oral/genital (i.e.  52% for torso and 0.386% for oral/gentital). 
![](/image/Picture4.png)
![](/image/Picture5.png)

There are around 30,000 more benign images compared to malignant images. 
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

The codes are provided in EDA.py

## Data Preprocessing
Before we feed the images into the EfficientNets, we apply standard pre-processing procedures on the imagesets.

### Over-sampling
Instead of the imbalances of the classification outcomes in the training set, we have decided to implement the oversampling strategy to adjust the ratio of the benign and malignant cases. In general, we are increasing the proportion of malignant cases by adding replicates of the image into the training set to make different replicates.

In order to have a similar scale of all skin lesions in the training image sets, we resize the images from J x K to L x 480, maintaining the aspect ratio. 

The procedure of resizing are in the file data-preprocessing.py.

With the resized images, we applied cropping on to these images. The rationale for cropping included two purposes. First, we wish to remove the unwanted skin area from the image and leave only the area of tumor, to increase the accuracy of the area captured by the image. Second, we can implement over-sampling through random cropping 5 times on the minority class - malignant images to balance the training set. 

For benign cases, we applied cropping only once, based on the center of the image. For malignant cases, we apply random cropping five times on the image. Through this process, one malignant image would turn into 5 images. Eventually, we have 28,320 images in the training set. There are 2,275 malignant images vs 26,045 benign images, and the new ratio between malignant cases and benign cases is around 8.6\%. Figure 1 and 2 shows the procedure of the utilized oversampling strategy. The testing image sets are also resized and cropped for consistency.

In order to investigate the effect of image size on skin lesion classification performance, we also cropped the images with five different pre-defined scales, 224 x 224, 240 x 240, 260 x 260, 300 x and 380 x 380.

![](/image/flow.png)

![](/image/WX20200806-142813@2x.png)

## CNN model and EfficientNets
The EfficientNets.ipynb contains the training codes.

For each experiment, we would define the cropping size and batch size. The file would read from the folders containg the resized images and crop the images based on the pre-defined image scale. Then, the processed image would be put into a image data generator from Keras API, where we can define different data augmentation strategies. After that, we would send the image into the EfficientNet architecture.

![](/image/archi.png)

We selected three models from the EfficientNets family, EfficientNets-B0, EfficientNets-B1 and EfficientNets-B3 to experiment their performances. The EfficientNets are state-of-art algorithm for image classification. It uses a scaling method of uniformly scaling model parameters with a compound efficient. Among the common CNN models, EfficientNets have proven to be the model with highest accuracy \cite{6}. The EfficientNets architecture have different depth of network. The main difference between EfficientNets B0 to B7 is the number of parameters. We selected three shallower models to train the model. With fewer parameters and shallower network depth, we could prevent over-fitting of the model and reduce computation costs.

The network consists of a base layer from EfficientNet, a global maximum pooling layer, a batch normalization layer, a dropout layer and two fully connected layers. We adapt the global maximum pooling layer 2D to convert the 4D tensors to 2D tensors. The layer would have less number of features comparing to a flat layer and would effectively reduce the number of parameters. We used a dropout factor of 0.2 in the dropout layer. A batch normalization layer is also added after the dropout layer. The rationale of adding these layers to the base layer is to prevent the risk of overfitting, especially with imbalanced data.

We implemented the images into the EfficientNets models. We have selected a batch size of 32. We use the Adam optimization algorithm with an initial learning rate of 0.0001. The network is trained for 50 epochs and we calculate the evaluation metrics from each epoch.

Our models are implemented using the Keras API with version 2.2.4 and tensorflow version 2.3.0 as the backend. 

