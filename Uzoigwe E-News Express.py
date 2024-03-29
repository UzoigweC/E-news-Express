# -*- coding: utf-8 -*-
"""ENews_Express_Learner_Notebook%5BFull_Code_Version%5D.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V3A4_UJVql_YD83A_mpvAUW9aJEzMMnH

# Project Business Statistics: E-news Express

**Marks: 60**

## Define Problem Statement and Objectives

**Problem Statement:**
E-news Express is focused on increasing its number of subscribers by developing a better and more engaging website. According to the company's executives, the current page design does not provide enough information and recommendations to keep customers engaged.
To determine which feature is more effective, a company often conducts an experiment that involves analyzing the responses of its users to two different products. This method, known as A-B testing, is designed to analyze the effectiveness of a new feature.

**Objective:**
For the experiment, the company will test the effectiveness of an updated landing page that has a more relevant and updated content compared to its old one. By sampling 100 users and dividing into two equal groups. The existing landing page was served to the first group (control group) and the new landing page to the second group (treatment group). Data about the interaction between the two groups was collected.  As a data scientist, the objective is to help the design team by providing the below data driven inputs.
1. Do the users spend more time on the new landing page than on the existing landing page?
2. Is the conversion rate (the proportion of users who visit the landing page and get converted) for the new page greater than the conversion rate for the old page?
3. Does the converted status depend on the preferred language?
4. Is the time spent on the new page the same for the different language users?

**Data Description**
The data contains the different data related to a E-News Portal. The detailed data dictionary is given below.

**Data Dictionary:**
The data contains information regarding the interaction of users in both groups with the two versions of the landing page.

1. user_id - Unique user ID of the person visiting the website

2. group - Whether the user belongs to the first group (control) or the second group (treatment)

3. landing_page - Whether the landing page is new or old

4. time_spent_on_the_page - Time (in minutes) spent by the user on the landing page

5. converted - Whether the user gets converted to a subscriber of the news portal or not

6. language_preferred - Language chosen by the user to view the landing page

## Import all the necessary libraries
"""

# Commented out IPython magic to ensure Python compatibility.
#import the important packages
import pandas as pd #library used for data manipulation and analysis
import numpy as np # library used for working with arrays.
import matplotlib.pyplot as plt # library for plots and visualisations
import seaborn as sns # library for visualisations
# %matplotlib inline


import scipy.stats as stats # this library contains a large number of probability distributions as well as a growing library of statistical functions.

# import the scipy and check the version to be sure that the version is above 1.6.1.
import scipy
scipy.__version__

"""####Observation
The version of Scipy is '1.10.1' which is above version 1.6.1 and also the latest version of Scipy.

## Reading the Data into a DataFrame
"""

#Connecting Google drive with Google colab
# Reading the data-set into Google colab
from google.colab import drive
drive.mount('/content/drive')

#Reading the abtest.csv dataset into a dataframe
path="/content/drive/My Drive/abtest.csv"
df=pd.read_csv(path)

"""## Explore the dataset and extract insights using Exploratory Data Analysis

- Data Overview
  - Viewing the first and last few rows of the dataset
  - Checking the shape of the dataset
  - Getting the statistical summary for the variables
- Check for missing values
- Check for duplicates
"""

# returning the first 5 rows head method
df.head()

# returning the last 5 rows using tail method
df.tail()

#checking shape of the dataframe to find out the number of rows and columns using shape command
print("There are", df.shape[0], 'rows and', df.shape[1], "columns.")

# Use info() to print a concise summary of the DataFrame
df.info()

"""#### Observations:
* There are a total of 100 non-null observations in each of the columns.

* The dataset contains 6 columns or series: 1 is of integer type ('user_id'), 1 is of floating point type ('time_spent_on_the_page') and 4 are of the general object type ('group', 'landing_page', 'converted', 'language_preferred').

* Total memory usage is approximately 4.8KB.
"""

# checking the statistical summary of the data using describe command and transposing.
df.describe().T

"""#### Observations:

* User ID are just identifiers for each order.

* The time spent on the page ranges from 0.19 to 10.71 minutes, with  average time spent on E-News portal which is around 5.3378 minutes and a standard deviation of 2.378166. 75% of the time spent on the E-News Portal for both old and new website is 7.0225 minutes.
"""

# Checking for missing values
df.isnull().sum()

"""#### Observations:

* There are no missing values in the data.
"""

duplicate = df[df.duplicated()]
duplicate

"""#### Observations:

* There are no duplicate values in the dataset.

### Univariate Analysis

**Observations on Numerical columns by checking the distribution for numerical columns.**

Observations on User ID

#### User ID
"""

# check unique user ID
df['user_id'].nunique()

"""#### Observations:

* There are 100 unique user IDs. However, 'user_id' is just an identifier for the website visitors.
"""

ax = sns.histplot(df['user_id'], color='#9d94ba', kde=False)
ax.set(title='Distribution of User_id ')
ax.set_xlabel("User ID", fontsize=14)
# label each bar in histogram
for p in ax.patches:
 height = p.get_height() # get the height of each bar
 # adding text to each bar
 ax.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
 y = height+0.2, # y-coordinate position of data label, padded 0.2 above bar
 s = '{:.0f}'.format(height), # data label, formatted to ignore decimals
 ha = 'center') # sets horizontal alignment (ha) to center
 ax.patches[0].set_facecolor('salmon')
 ax.patches[1].set_facecolor('yellow')
 ax.patches[2].set_facecolor('blue')
 ax.patches[3].set_facecolor('red')
 ax.patches[4].set_facecolor('green')
 ax.patches[5].set_facecolor('purple')
 ax.patches[6].set_facecolor('brown')
 ax.patches[7].set_facecolor('orange')

"""#### Observations:

* There are 100 unique user IDs. As mentioned earlier, 'user_id' is just an identifier for the website visitors.

**Observation of time spent on landing page**
"""

ax = sns.histplot(df['time_spent_on_the_page'], color='#9d94ba', kde=False)
ax.set(title='Distribution of time spent on landing page')
ax.set_xlabel("Time spent on landing page", fontsize=14)
# label each bar in histogram
for p in ax.patches:
 height = p.get_height() # get the height of each bar
 # adding text to each bar
 ax.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
 y = height+0.2, # y-coordinate position of data label, padded 0.2 above bar
 s = '{:.0f}'.format(height), # data label, formatted to ignore decimals
 ha = 'center') # sets horizontal alignment (ha) to center
 ax.patches[0].set_facecolor('salmon')
 ax.patches[1].set_facecolor('yellow')
 ax.patches[2].set_facecolor('blue')
 ax.patches[3].set_facecolor('red')
 ax.patches[4].set_facecolor('green')
 ax.patches[5].set_facecolor('purple')
 ax.patches[6].set_facecolor('brown')
 ax.patches[7].set_facecolor('orange')

bxp=sns.boxplot(data=df,x='time_spent_on_the_page')
bxp.set_xlabel("Time spent on landing page", fontsize=14)
bxp.axes.set_title("Distribution of time spent on landing page", fontsize=16)
plt.show()

"""#### Observations:

* Majority of the website visitors spent around 5 to 7 minutes on the E-News Portal.
* Only about 4 of the website visitors spent upto 10 minutes on the portal.
* The data is normally distibuted
* There are no outliers in this coloumn
* 75% of the times visitors spent on the portal are below 7 minutes.

#### Group

**Observation of the group column**
"""

# check unique group
df['group'].nunique()

"""#### Observations:

* There are 2 unique groups in the group series.
"""

# check the unique values
df['group'].value_counts()

"""#### Observations:

* The group series is made up of two groups, the control (50 samples) and the treatment group (50 samples)
"""

ax=sns.countplot(data = df, x = 'group')
plt.xticks(rotation=90)
ax.set(title='Distribution of Group')
ax.set_xlabel("Group", fontsize=14)
# label each bar in the countplot
for p in ax.patches:
 height = p.get_height() # get the height of each bar
 # adding text to each bar
 ax.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
 y = height+0.2, # y-coordinate position of data label, padded 0.2 above bar
 s = '{:.0f}'.format(height), # data label, formatted to ignore decimals
 ha = 'center') # sets horizontal alignment (ha) to center

"""#### Observations:

* The 'group' columns consists of 2 unique values - control and treatment
* The distribution shows that number of website visitors selected for each group is 50. The number of visitors that uses the old landing  (50) is same with the number of visitors that used the new landing page (50), therefore the group is balanced.

####Landing Page

****Observation for Landing Page****
"""

# check unique group
df['landing_page'].nunique()

"""#### Observations:

* There are 2 unique groups in the landing page series.
"""

# check the unique values
df['landing_page'].value_counts()

"""#### Observations:

* The landing page series is made up of two groups, the old (50 samples) and the new landing page (50 samples)
"""

ax=sns.countplot(data = df, x = 'landing_page')
plt.xticks(rotation=90)
ax.set(title='Distribution of Landing Page')
ax.set_xlabel("Landing Page", fontsize=14)
# label each bar in the countplot
for p in ax.patches:
 height = p.get_height() # get the height of each bar
 # adding text to each bar
 ax.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
 y = height+0.2, # y-coordinate position of data label, padded 0.2 above bar
 s = '{:.0f}'.format(height), # data label, formatted to ignore decimals
 ha = 'center') # sets horizontal alignment (ha) to center

"""#### Observations:

* The 'landing page' columns consists of 2 unique values - old and new landing page
* The distribution shows that number of old landing page served to the website visitors is the same with the number of new landing page served, therefore it is balanced.

#### Converted
"""

# check unique group
df['converted'].nunique()

"""#### Observations:

* There are 2 unique groups in the converted series.
"""

# check the unique values
df['converted'].value_counts()

"""#### Observations:

* The converted series is made up of two groups, yes (54) and the new landing page (46)
"""

ax=sns.countplot(data = df, x = 'converted')
plt.xticks(rotation=90)
ax.set(title='Distribution of website conversion')
ax.set_xlabel("Conversion", fontsize=14)
# label each bar in the countplot
for p in ax.patches:
 height = p.get_height() # get the height of each bar
 # adding text to each bar
 ax.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
 y = height+0.2, # y-coordinate position of data label, padded 0.2 above bar
 s = '{:.0f}'.format(height), # data label, formatted to ignore decimals
 ha = 'center') # sets horizontal alignment (ha) to center

"""#### Observations:

* The 'converted' columns consists of 2 unique values - yes and no
* The distribution shows that number of website visitors that subscribed (54) and the number of website visitors that did not subscribe (48), therefore there are more visitors that subscribed than those that didn't subscribe.

####Language Prefered
"""

# check unique group
df['language_preferred'].nunique()

"""#### Observations:

* There are 3 unique groups in the language prefered series.
"""

# check the unique values
df['language_preferred'].value_counts()

"""#### Observations:

* The three groups of the language series are the Spanish (34), French (34) and the English (32) Language.
"""

plt.figure(figsize = (8,5))
sns.countplot(data = df, x = 'language_preferred');

#--Sort the plot
plt.figure(figsize = (8,5))
ax=sns.countplot(data = df, x = 'language_preferred', order = df['language_preferred'].value_counts().index);
plt.xticks(rotation=90)
ax.set(title='Distribution of Language Prefered')
ax.set_xlabel("language_preferred", fontsize=14)
# label each bar in the countplot
for p in ax.patches:
 height = p.get_height() # get the height of each bar
 # adding text to each bar
 ax.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
 y = height+0.2, # y-coordinate position of data label, padded 0.2 above bar
 s = '{:.0f}'.format(height), # data label, formatted to ignore decimals
 ha = 'center') # sets horizontal alignment (ha) to center

"""#### Observations:

* There are 3 unique languages in the dataset.

* The distribution of languages prefered show that Spanish (34) and French(34) languages are the most frequently prefered languages.

* English has the least frequency though not with a large margin from others.

### Bivariate Analysis

****Correlation analysis between the numeric variables****
"""

plt.figure(figsize=(10,5))
ax=sns.heatmap(df.corr(),annot=True,cmap='Spectral',vmin=-1,vmax=1)
ax.set(title='Correlation between variables')
plt.show()

"""####Observation
* The only two numeric variables which are the User_id and the time spent on landing page have negative correlation, however this is not useful in the analysis since the User_id is just an identifier.

****Relationship between group and landing page series****
"""

plt.figure(figsize=(10,5))
bxp=sns.countplot(data=df,x='group', hue='landing_page')
bxp.set_xlabel("Group", fontsize=14)
bxp.axes.set_title("Relationship between group and landing page", fontsize=16)
plt.xticks(rotation=90)
# label each bar in the countplot
for p in bxp.patches:
 height = p.get_height() # get the height of each bar
 # adding text to each bar
 bxp.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
 y = height+0.2, # y-coordinate position of data label, padded 0.2 above bar
 s = '{:.0f}'.format(height), # data label, formatted to ignore decimals
 ha = 'center') # sets horizontal alignment (ha) to center
plt.show()

"""####Observation
* The control and treatment group has same number of samples which is 50 each
* The old landing page was used as the control group and the new landing page as the treatment group.
* The groups are balanced
* Since the sample size is greater than 30, the ccentral limit theorem can be applied.

****Relationship between  group and time spent on the page****
"""

plt.figure(figsize=(8,5))
bxp=sns.boxplot(data=df,x='group', y='time_spent_on_the_page')
bxp.set_xlabel("group", fontsize=14)
bxp.axes.set_title("Relationship between  group and time spent on the page", fontsize=16)
plt.xticks(rotation=90)
plt.show()

"""####Observation
* 50% of the time spent by the control group which is on the old landing page is below 4.3 minutes whereas 50% of time spent by the treatment group is below 6 minutes
* 75% of  the time spent by the control group which is on the old landing page is below 6.3 minutes whereas 75% of time spent by the treatment group is below 7minutes.
* The average time spent on the new landing page is higher than the average time spent on the old landing page.
* There are outliers in the treatment group.

****Relationship between group and converted****
"""

plt.figure(figsize=(10,5))
bxp=sns.countplot(data=df,x='group', hue='converted')
bxp.set_xlabel("Group", fontsize=14)
bxp.axes.set_title("Relationship between group and converted", fontsize=16)
plt.xticks(rotation=90)
# label each bar in the countplot
for p in bxp.patches:
 height = p.get_height() # get the height of each bar
 # adding text to each bar
 bxp.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
 y = height+0.2, # y-coordinate position of data label, padded 0.2 above bar
 s = '{:.0f}'.format(height), # data label, formatted to ignore decimals
 ha = 'center') # sets horizontal alignment (ha) to center
plt.show()

"""#### Observation
* Out of the 50 visitors sampled for the control group, 21 of them subscribed to the E-News Portal whereas 29 didn't, this gives a conversion rate of 42%.
* Out of the 50 visitors sampled for the treatment group, 33 of them subscribed to the E-News Portal whereas only 17 didn't, this gives a conversion rate of 66%.
* Therefore, more of those in the treatment group converted (subscribed) than those in the control group.

****Relationship between  converted and time spent on the page****
"""

plt.figure(figsize=(10,5))
bxp=sns.boxplot(data=df,x='converted', y='time_spent_on_the_page')
bxp.set_xlabel("Converted", fontsize=14)
bxp.axes.set_title("Relationship between converted and time spent on the page", fontsize=16)
plt.xticks(rotation=90)
plt.show()

"""####Observation
* 75% of those who did not subscribe(not converted) to the E-News Portal spent below 5 minutes.
* 75% of those who did  subscribed(converted) to the E-News Portal spent below 7 minutes.
* The average time spent by those who got converted on the website is higher than the average time spent on those who did not convert.
* There are outliers in but conversion groups

****Relationship between time spent and prefered language****
"""

plt.figure(figsize=(10,5))
bxp=sns.boxplot(data=df,x='language_preferred', y='time_spent_on_the_page')
bxp.set_xlabel("Language prefered", fontsize=14)
bxp.axes.set_title("Relationship between time spent and prefered language", fontsize=16)
plt.xticks(rotation=90)
plt.show()

"""####Observation
* 75% of those who prefered Spanish language spent below 6.3 minutes on the portal.
* No much different between the time spent by 75% of those who prefered English and French
* There exist an outlier in the spanish group.

**Multivariate Analysis**

****Relationship between landing page, time spent on the page, based on conversion****
"""

plt.figure(figsize=(10,5))
bxp=sns.boxplot(data=df,x='landing_page', y='time_spent_on_the_page', hue='converted')
bxp.set_xlabel("landing page", fontsize=14)
bxp.axes.set_title("Relationship between landing page, time spent on the page, based on conversion", fontsize=16)
plt.xticks(rotation=90)
plt.show()

"""####Observation
* Those who did not get converted on the new landing page spent more time than those who did not get converted on the old landing page.
* There seem to be no much diffrence in the time spent by those who got converted on the old landing page and those who got converted on the new landing page.
* There exist an outlier in the groups

****Relationship between language prefered, time spent on the page, based on conversion****
"""

plt.figure(figsize=(10,5))
bxp=sns.boxplot(data=df,x='language_preferred', y='time_spent_on_the_page', hue='converted')
bxp.set_xlabel("language prefered", fontsize=14)
bxp.axes.set_title("Relationship between language prefered, time spent on the page, based on conversion", fontsize=16)
plt.xticks(rotation=90)
plt.show()

"""####Observation
* 75% of those who prefered Spanish language that got converted spend below 7 minutes
* 75% of those who prefered English language that got converted spend below 7.5 minutes
* 75% of those who prefered French language that got converted spend below 7.7 minutes
* Therefore with spanish language conversion is made within lesser time when compared to other languages.

****Relationship between landing page, time spent on the page, based on language prefered****
"""

plt.figure(figsize=(10,5))
bxp=sns.boxplot(data=df,x='landing_page', y='time_spent_on_the_page', hue='language_preferred')
bxp.set_xlabel("landing page", fontsize=14)
bxp.axes.set_title("Relationship between landing page, time spent on the page, based on language prefered", fontsize=16)
plt.xticks(rotation=90)
plt.show()

"""####Observation
* The average time spent on the new landing page is higher for all prefered langauges than on the old landing page.
* Those who prefered English language spend higher time than those others in other prefered languages.

## 1. Do the users spend more time on the new landing page than the existing landing page?

### Perform Visual Analysis
"""

plt.figure(figsize=(8,5))
bxp=sns.boxplot(data=df,x='landing_page', y='time_spent_on_the_page')
bxp.set_xlabel("Landing Page", fontsize=14)
bxp.axes.set_title("Relationship between  Landing page and time spent on the page", fontsize=16)
plt.xticks(rotation=90)
plt.show()

"""####Observation

* 50% of the time spent on the old landing page is below 4.3 minutes whereas 50% of time spent on the new landing page is below 6 minutes
* 75% of  the time spent on the old landing page is below 6.3 minutes whereas 75% of time spent on the new landing page is below 7minutes.
* The average time spent on the new landing page is higher than the average time spent on the old landing page.
* There are outliers in the new landing page group.
"""

df.groupby('landing_page')["time_spent_on_the_page"].mean().sort_values(ascending=False).reset_index()

"""### Step 1: Define the null and alternate hypotheses

Let $\mu_1, \mu_2$ be the  mean time spent on new landing page and mean time spent on old landing page respectively.

We will test the null hypothesis

>$H_0:\mu_1=\mu_2$

against the alternate hypothesis

>$H_a:\mu_1>\mu_2$

### Step 2: Select Appropriate test
"""

newtime=df.loc[df['landing_page']=='new']
newdf=newtime['time_spent_on_the_page'].reset_index(name='New landing page time',drop="True")
newdf2= pd.DataFrame(newdf)
newdf2.columns = ['Time spent on new page']
newdf2.head()

oldtime=df.loc[df['landing_page']=='old']
olddf=oldtime['time_spent_on_the_page'].reset_index(name='Old landing page time',drop="True")
olddf2= pd.DataFrame(olddf)
olddf2.columns = ['Time spent on old page']
olddf2.head()

# find the sample means and sample standard deviations for the two samples
print('The mean time spent on the old landing page is ' + str(olddf2['Time spent on old page'].mean()))
print('The mean time spent on the new landing page is ' + str(newdf2['Time spent on new page'].mean()))
print('The standard deviation of the time spent on the old landing page is ' + str(round(olddf2['Time spent on old page'].std(), 2)))
print('The standard deviation of the time spent on the new landing page is  ' + str(round(newdf2['Time spent on new page'].std(), 2)))

"""### Let's check the nature of the data to ascertain which statistical test assumption it satisfies.

* Continuous data - Yes, the time is measured on a continuous scale.
* Normally distributed populations - Yes, the sample size in each group is >30, so it satifies the assumption of central limit theorem.
* Independent populations - As we are taking random samples for two different groups, the two samples are from two independent populations.
* Unequal population standard deviations - As the sample standard deviations are different, the population standard deviations may be assumed to be different.
* Random sampling from the population - Yes, we are informed that the collected sample a simple random sample.
This satisfies the conditions for using ****Two independent sample T-test****

### Step 3: Decide the significance level

We were asked to explore the data and perform a statistical analysis (at a significance level of 5%) therefore the level of significance will be 0.05 at 95% confidence interval. The significant level will be one-tailed since we are looking at one direction (greather than)

### Step 4: Collect and prepare data
"""

frames = [olddf2, newdf2]
result = pd.concat(frames,axis=1)
result.reset_index(drop="True").head()

result.reset_index(drop="True").tail()

"""### Step 5: Calculate the p-value

The ttest_ind() function of Scipy will be used to compute the test statistic and p-value.
"""

#import the required functions
from scipy.stats import ttest_ind

# find the p-value
test_stat, p_value = ttest_ind(newdf2['Time spent on new page'], olddf2['Time spent on old page'].dropna(), equal_var = False, alternative = 'greater')
print('The p-value is ', p_value)

"""### Step 6: Compare the p-value with $\alpha$"""

P_value=0.000139
levsig=0.05
p_value<levsig

"""### Step 7:  Draw inference

### Inference
As the p-value (~0.00014) is less than the level of significance, we can reject the null hypothesis. Hence, we do have enough evidence to support the claim that website visitors spend more time on the new landing page than on the old landing page.

**A similar approach can be followed to answer the other questions.**

## 2. Is the conversion rate (the proportion of users who visit the landing page and get converted) for the new page greater than the conversion rate for the old page?

### Perform Visual Analysis
"""

plt.figure(figsize=(10,5))
bxp=sns.countplot(data=df,x='landing_page', hue='converted')
bxp.set_xlabel("Landing Page", fontsize=14)
bxp.axes.set_title("Relationship between landing page and converted", fontsize=16)
plt.xticks(rotation=90)
# label each bar in the countplot
for p in bxp.patches:
 height = p.get_height() # get the height of each bar
 # adding text to each bar
 bxp.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
 y = height+0.2, # y-coordinate position of data label, padded 0.2 above bar
 s = '{:.0f}'.format(height), # data label, formatted to ignore decimals
 ha = 'center') # sets horizontal alignment (ha) to center
plt.show()

"""#### Observation
* Out of the 50 visitors sampled for the old landing page group, 21 of them subscribed to the E-News Portal whereas 29 didn't, this gives a conversion rate of 42%.
* Out of the 50 visitors sampled for the new landing page group, 33 of them subscribed to the E-News Portal whereas only 17 didn't, this gives a conversion rate of 66%.
* Therefore, more of those served with the new landing page converted (subscribed) than those served with the old landing page.

### Step 1: Define the null and alternate hypotheses

### Let's write the null and alternative hypothesis
Let $p_1,p_2$ be the proportions of conversions in the new landing page and the old landing page respectively.

The E-news portal team  will test the null hypothesis

>$H_0:p_1 =p_2$

against the alternate hypothesis

>$H_a:p_1 > p_2$

### Step 2: Select Appropriate test
"""

df.groupby('converted')['landing_page'].apply(lambda x: (x=='new').sum()).reset_index(name='count')

df.groupby('converted')['landing_page'].apply(lambda x: (x=='old').sum()).reset_index(name='count')

"""### Let's check the nature of the data to ascertain which statistical test assumption it satisfies.

*   Binomally distributed population - Yes, a landing page is either converted or not converted.
*   Random sampling from the population - Yes, we are informed that the collected sample is a simple random sample.  
*   Can the binomial distribution approximated to normal distribution - Yes. For binary data, CLT works slower than usual. The standard thing is to check whether np and n(1-p) are greater than or equal to 10. Here, n and p refer to the sample size and sample proportion respectively.
>$np_1 = 50\cdot \frac{33}{50} =33 \geq 10\\
n(1-p_1) = 200 \cdot \frac{50-33}{50} =17 \geq 10 \\
np_2 = 400\cdot \frac{21}{50} =21 \geq 10\\
n(1-p_2) = 400 \cdot \frac{50-21}{50} =29 \geq 10 $

This satisfies the conditions for using ****Two Proportion Z-test****

### Step 3: Decide the significance level

We were asked to explore the data and perform a statistical analysis (at a significance level of 5%) therefore the level of significance will be 0.05 at 95% confidence interval. The significant level will be one-tailed since we are looking at one direction (greather than)

### Step 4: Collect and prepare data
"""

df.groupby('converted')['landing_page'].apply(lambda x: (x=='new').sum()).reset_index(name='count')

df.groupby('converted')['landing_page'].apply(lambda x: (x=='old').sum()).reset_index(name='count')

"""### Step 5: Calculate the p-value"""

#import the required fuction
from statsmodels.stats.proportion import proportions_ztest

# set the counts of defective items
converted = np.array([33,21])

# set the sample sizes
nobs = np.array([50, 50])

# find the p-value
test_stat, p_value = proportions_ztest(converted, nobs, alternative = 'larger')
print('The p-value is ' + str(p_value))

"""### Step 6: Compare the p-value with $\alpha$"""

P_value=0.008
levsig=0.05
p_value<levsig

"""### Step 7:  Draw inference

### Inference
As the p-value (~0.008) is less than the level of significance, we can reject the null hypothesis. Hence, we do have enough evidence to support the claim that the conversion rate for new page is larger than the conversion rate for old page.

## 3. Is the conversion and preferred language are independent or related?

### Perform Visual Analysis
"""

plt.figure(figsize=(10,5))
bxp=sns.countplot(data=df,x='language_preferred', hue='converted')
bxp.set_xlabel("Language preferred", fontsize=14)
bxp.axes.set_title("Relationship between language preferred and converted", fontsize=16)
plt.xticks(rotation=90)
# label each bar in the countplot
for p in bxp.patches:
 height = p.get_height() # get the height of each bar
 # adding text to each bar
 bxp.text(x = p.get_x()+(p.get_width()/2), # x-coordinate position of data label, padded to be in the middle of the bar
 y = height+0.2, # y-coordinate position of data label, padded 0.2 above bar
 s = '{:.0f}'.format(height), # data label, formatted to ignore decimals
 ha = 'center') # sets horizontal alignment (ha) to center
plt.show()

"""####Observation
*English has the highest number (21) of those who converted than any other language
*The number of people that converted in french language(15) is less than people that did not convert(19).

### Step 1: Define the null and alternate hypotheses

### Let's write the null and alternative hypothesis


We will test the null hypothesis

>$H_0:$ Conversion is independent of Language preference.

against the alternate hypothesis

>$H_a:$ Conversion is dependent of Language preference.

### Step 2: Select Appropriate test

### Let's check the nature of the data to ascertain which statistical test assumption it satisfies.
* Categorical variables for both independent and dependent - Yes
* Expected value of the number of sample observations in each level of the variable is at least 5 - Yes, the number of observations in each level is greater than 5.
* Random sampling from the population - Yes, we are informed that the collected sample is a simple random sample.

Therefore the right test to choose is the ****Chi-Square Test for Independence****

### Step 3: Decide the significance level

We were asked to explore the data and perform a statistical analysis (at a significance level of 5%) therefore the level of significance will be 0.05 at 95% confidence interval. The significant level will be Two-tailed since we are looking at relationship in both directions.

##Step 4: Collect and prepare data
"""

dfchiq=pd.crosstab(index=df['converted'], columns=df['language_preferred']) #Creating contingency table
dfchiq

"""### Step 5: Calculate the p-value

The [`chi2_contingency()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html) function of Scipy will be used to compute the test statistic and p-value
"""

# import the required function
from scipy.stats import chi2_contingency

# find the p-value
chi, p_value, dof, expected = chi2_contingency(dfchiq)
print('The p-value is', p_value)

"""### Step 6: Compare the p-value with $\alpha$"""

P_value=0.2129
levsig=0.05
p_value<levsig

"""### Step 7:  Draw inference

###Inference
The p-value is 21.30% which means that we do not reject the null hypothesis at 95% level of confidence. The null hypothesis was that conversion and language prefered are independent. The contingency table was 2×3.

## 4. Is the time spent on the new page same for the different language users?

### Perform Visual Analysis
"""

plt.figure(figsize=(10,5))
bxp=sns.boxplot(data=newtime,x='landing_page', y='time_spent_on_the_page', hue='language_preferred')
bxp.set_xlabel("landing page", fontsize=14)
bxp.axes.set_title("Relationship between new landing page, time spent on new page, based on language prefered", fontsize=16)
plt.xticks(rotation=90)
plt.show()

"""####Observation

* Of the 75% of time spent on the new landing page, English, Spanish and French was found to be around below 7.8,6.8, and 7.6 minutes respectively.
* The average time spent by those who prefered English on the new landing page is higher than other languages
* There are outliers in the Spanish language prefered group.

### Step 1: Define the null and alternate hypotheses

### Let's write the null and alternative hypothesis

Let $\mu_1, \mu_2, \mu_3$ be the means time spent on the new page for English, French and Spanish respectively.

We will test the null hypothesis

>$H_0: \mu_1 = \mu_2 = \mu_3$

against the alternative hypothesis

>$H_a: $ At least one prefered language group is different from the rest.

### Step 2: Select Appropriate test

### Shapiro-Wilk’s test

We will test the null hypothesis

>$H_0:$ Time spent on new page follows a normal distribution against

against the alternative hypothesis

>$H_a:$ Time spent on new page does not follow a normal distribution

The [`shapiro()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html) function of Scipy will be used to compute the test statistic and p-value.
"""

# Assumption 1: Normality
# import the required function
from scipy import stats

# find the p-value
w, p_value = stats.shapiro(newtime['time_spent_on_the_page'])
print('The p-value is', p_value)

"""Since p-value of the test is very large, we fail to reject the null hypothesis that the response follows the normal distribution.

### Levene’s test

We will test the null hypothesis

>$H_0$: All the population variances are equal

against the alternative hypothesis

>$H_a$: At least one variance is different from the rest

The [`levene()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html) function of Scipy will be used to compute the test statistic and p-value.
"""

#Assumption 2: Homogeneity of Variance
#import the required function
from scipy.stats import levene
statistic, p_value = levene(newtime['time_spent_on_the_page'][newtime['language_preferred']=="English"],
                                   newtime['time_spent_on_the_page'][newtime['language_preferred']=="French"],
                                   newtime['time_spent_on_the_page'][newtime['language_preferred']=="Spanish"])
# find the p-value
print('The p-value is', p_value)

"""Since the p-value is large, we fail to reject the null hypothesis of homogeneity of variances.

### Let's check the nature of the data to ascertain which statistical test assumption it satisfies.
* The populations are normally distributed - Yes, the normality assumption is verified using the Shapiro-Wilk’s test.
* Samples are independent simple random samples - Yes, we are informed that the collected sample is a simple random sample.
* Population variances are equal - Yes, the homogeneity of variance assumption is verified using the Levene's test.
Therefore this satisfies the assumption for using ****One-way ANOVA Test****

### Step 3: Decide the significance level

We were asked to explore the data and perform a statistical analysis (at a significance level of 5%) therefore the level of significance will be 0.05 at 95% confidence interval. The significant level will be Two-tailed since we are looking at difference in both directions (Either less or larger).

##Step 4: Collect and prepare data
"""

newtime=df.loc[df['landing_page']=='new'].reset_index(drop="True")
newtime.head()

"""### Step 5: Calculate the p-value

The [`f_oneway()`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html) function of Scipy will be used to compute the test statistic and p-value.
"""

#import the required function
from scipy.stats import f_oneway

# perform one-way anova test
test_stat, p_value = f_oneway(newtime.loc[newtime['language_preferred'] == 'English', 'time_spent_on_the_page'],
                              newtime.loc[newtime['language_preferred'] == 'French', 'time_spent_on_the_page'],
                              newtime.loc[newtime['language_preferred'] == 'Spanish', 'time_spent_on_the_page'])
print('The p-value is ' + str(p_value))

"""### Step 6: Compare the p-value with $\alpha$"""

P_value=0.4320
levsig=0.05
p_value<levsig

"""### Step 7:  Draw inference

###Inference
The p-value is 43.20% which means that we do not reject the null hypothesis at 95% level of confidence. The null hypothesis was that time spent on the new page is the same for the different languages. And also since the time spent on the new page by users of different languages is found to be the same there is no need to conduct a ****Multiple Comparison test (Tukey HSD)****

## Conclusion and Business Recommendations

####Conclusion
* There are no missing values in the data
*There are no duplicate values
* Majority of the website visitors spent around 5 to 7 minutes on the E-News Portal.
* The distribution shows that number of old landing page served to the website visitors is the same with the number of new landing page served, therefore it is balanced.
* The distribution shows that number of website visitors that subscribed (54) and the number of website visitors that did not subscribe (48), therefore there are more visitors that subscribed than those that didn't subscribe.
* The distribution of languages prefered show that Spanish (34) and French(34) languages are the most frequently prefered languages.
* 75% of the time spent by the control group which is on the old landing page is below 6.3 minutes whereas 75% of time spent by the treatment group is below 7minutes.
* The average time spent on the new landing page is higher than the average time spent on the old landing page.
* Therefore, more of those in the treatment group converted (subscribed) than those in the control group.
* The average time spent by those who got converted on the website is higher than the average time spent on those who did not convert.
* Website visitors spend more time on the new landing page than on the old landing page.
* The conversion rate for new page is larger than the conversion rate for old page.
* The conversion and language prefered are independent
* The time spent on the new page by users of different languages is found to be the same

####Recommendation

* More features should be added to the new lading page to encourage more conversion.
* The E-news portal should embrace the new landing page since it leads to more conversion rate.
* More features should be added to help increase the time spent on the page, since more time was found to increae conversion.

___
"""