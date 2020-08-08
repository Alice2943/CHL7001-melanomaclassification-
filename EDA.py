import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly as plotly


# Import dataset
# Have to change to the real train set later
train = pd.read_csv(r'C:\Users\di_ni\OneDrive\Documents\Desktop\CHL7001\train.csv')
print(train)

# Import duplicates
duplicates = pd.read_csv(r'C:\Users\di_ni\OneDrive\Documents\Desktop\CHL7001\train_duplicates.csv')
print(duplicates)

# Remove duplicates from original dataset
cond = train['image_name'].isin(duplicates['duplicates'])
print(cond)
train.drop(train[cond].index, inplace = True)
print(train)

# Check duplicated patient id: max is 115 images for one patient
train.patient_id.value_counts().max()

# Multiple images for one patient： distribution plot and box plot
patient_counts_train = train.patient_id.value_counts()
print(patient_counts_train)

patient_counts_train = pd.DataFrame(patient_counts_train)

patient_counts_train.columns = ['frequency']
print(patient_counts_train)

fig, ax = plt.subplots(2,1,figsize=(20,19))
sns.set(font_scale=2)
sns.distplot(patient_counts_train, ax=ax[0], color="green", kde=True);
ax[0].tick_params(axis="both", labelsize=23)
ax[0].set_xlabel("Number of images per patient", fontsize=23)
ax[0].set_ylabel("Frequency of patients", fontsize=23)
sns.boxplot(x=patient_counts_train['frequency'], ax=ax[1], color="green");
ax[1].tick_params(axis="both", labelsize=23)
ax[1].set_xlim(0,130)
ax[1].set_xlabel("Number of images per patient", fontsize=23)
ax[1].set_ylabel("Frequency of patients", fontsize=23)
plt.savefig('Frequency.png')
plt.show()

# Check frequency for individual variables
for i in ['sex', 'age_approx', 'anatom_site_general_challenge', 'benign_malignant']:
    fig = plt.figure(figsize=(15, 10))
    df = pd.DataFrame(train[i].value_counts())
    df['name'] = df.index
    plt.bar(df.name, df[i])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()

for i in ['diagnosis']:
    fig = plt.figure(figsize=(15, 10))
    df = pd.DataFrame(train[i].value_counts())
    df['name'] = df.index
    plt.bar(df.name, df[i])
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.show()

# Treemap for location
cntstr = train.anatom_site_general_challenge.value_counts().rename_axis('anatom_site_general_challenge').reset_index(
         name='count')
fig = px.treemap(cntstr,
                 path=['anatom_site_general_challenge'],
                 values='count',
                 color='count',
                 color_continuous_scale='PuBu',
                 title='Scans by Anatom Site General Challenge - Train Data')
fig.update_layout(font=dict(size=32))
fig.update_traces(textinfo='label+percent entry')
plotly.offline.plot(fig)

# Function to calculate missing values by column# Funct
def missing_values_table(df):
    # Total missing values
    mis_val = df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
        columns={0: 'Missing Values', 1: '% of Total Values'})

    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)

    # Print some summary information
    print("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"
           "There are " + str(mis_val_table_ren_columns.shape[0]) +
          " columns that have missing values.")

    # Return the dataframe with missing information
    return mis_val_table_ren_columns

# Missing values statistics: using imputations
missing_values = missing_values_table(train)
print(missing_values)

# Age, sex
# Similar trend for males and females
fig, ax = plt.subplots(2,1,figsize=(20,15))
sns.set(font_scale=2)
sns.boxplot(train.sex, train.age_approx, ax=ax[0], palette="Reds_r");
ax[0].tick_params(axis="both", labelsize=23)
ax[0].set_xlabel('Sex', fontsize=23)
ax[0].set_ylabel('Age', fontsize=23)
sns.countplot(train.age_approx, hue=train.sex, ax=ax[1], palette="Reds_r");
ax[1].tick_params(axis='both', labelsize=23)
ax[1].set_xlabel('Age', fontsize=23)
ax[1].set_ylabel('Frequency', fontsize=23)
plt.savefig('AgeSex.png')
plt.show()

# Age, location
# Evenly distributed
fig, ax = plt.subplots(2,1, figsize=(20,25))
sns.set(font_scale=2)
sns.boxplot(y=train.age_approx, x=train.anatom_site_general_challenge, ax=ax[0], palette='Reds_r',
            boxprops=dict(alpha=.7))
ax[0].set_xlabel("")
ax[0].set_ylabel('Age')
labels = ax[0].get_xticklabels();
ax[0].set_xticklabels(labels, rotation=45);
sns.countplot(train.age_approx, hue=train.anatom_site_general_challenge, ax=ax[1], palette="Reds_r");
ax[1].set_ylabel('Frequency')
ax[1].set_xlabel('Age')
plt.savefig('AgeLocation.png')
plt.show()

# Age, diagnosis
# Melanoma across all age groups but concentrated at the age 45 to 70
fig, ax = plt.subplots(figsize=(20,29))
sns.boxplot(y=train.age_approx, x=train.diagnosis, palette='Reds_r', boxprops=dict(alpha=.7))
ax.set_ylabel('Age')
ax.set_xlabel("");
labels = ax.get_xticklabels();
ax.set_xticklabels(labels, rotation=40);
plt.savefig('AgeDiagnosis1.png')
plt.show()

fig, ax = plt.subplots(figsize=(20,15))
sns.countplot(train.age_approx, hue=train.diagnosis, palette="Reds_r");
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
plt.savefig('AgeDiagnosis2.png')
plt.show()

# Age, sex, malignant/benign: boxplot, heatmap, histograms, tree leaf
# People diagnosed with malignant tumors are older compared to people diagnosed with benign tumors
# 62% of malignant cases belong to males
# 2.1% of males have malignant tumors
# A high gender imbalance for a wide range of ages for the malignant cases
sex_and_cancer_map = train.groupby( ["benign_malignant", "sex"]
                      ).size().unstack(level=0) / train.groupby("benign_malignant").size() * 100

cancer_sex_map = train.groupby(["benign_malignant", "sex"]
                  ).size().unstack(level=1) / train.groupby("sex").size() * 100

fig, ax = plt.subplots(1,3,figsize=(20,5))
sns.boxplot(train.benign_malignant, train.age_approx, ax=ax[0], palette="Reds_r");
ax[0].set_ylabel('Age')
ax[0].set_xlabel("");
sns.heatmap(sex_and_cancer_map, annot=True, cmap="Reds_r", cbar=False, ax=ax[1])
ax[1].set_xlabel("")
ax[1].set_ylabel("");
sns.heatmap(cancer_sex_map, annot=True, cmap="Reds_r", cbar=False, ax=ax[2])
ax[2].set_xlabel("")
ax[2].set_ylabel("");
plt.savefig('AgeMalignant.png')
plt.show()

fig, ax = plt.subplots(figsize=(18,12))
sns.violinplot(train.sex, train.age_approx, hue=train.benign_malignant, split=True, palette='Purples_r');
ax.set_ylabel('Age')
plt.savefig('AgeSexMalignant1.png')
plt.show()






































