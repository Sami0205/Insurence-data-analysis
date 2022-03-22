# Lodaing the necessary Libraries.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('insurance (1).csv')
data.head()

data.head()

data.describe().transpose()

print(f'Shape of data : {data.shape}')
print(f'Total {data.shape[0]} rows in the data.')

data.info()

data.dtypes.unique()
data.columns
data.index
data.dtypes

data.age.value_counts()
data.sex.value_counts()
data.bmi.value_counts()
data.children.value_counts()
data.smoker.value_counts()

plt.figure(figsize= (4,2))
plt.subplot(3,3,1)
plt.hist(data.bmi, color='lightblue', edgecolor = 'black', alpha = 0.7)
plt.xlabel('bmi')

plt.subplot(3,3,2)
plt.hist(data.age, color='lightblue', edgecolor = 'black', alpha = 0.7)
plt.xlabel('age')

plt.subplot(3,3,3)
plt.hist(data.charges, color='lightblue', edgecolor = 'black', alpha = 0.7)
plt.xlabel('charges')

plt.show()


plt.figure(figsize= (4,2))
plt.subplot(3,1,1)
sns.boxplot(x= data.bmi, color='lightblue')

plt.subplot(3,1,2)
sns.boxplot(x= data.age, color='lightblue')

plt.subplot(3,1,3)
sns.boxplot(x= data.charges, color='lightblue')

plt.show()


plt.figure(figsize= (4,2))
sns.countplot(x = 'smoker',hue = 'sex',data = data) 
# It is showing the difference between smokers and non smokers

plt.figure(figsize= (4,2))
sns.lineplot(x = 'age',y = 'charges',data = data,hue = 'smoker')
# According to this graph smokers has paid more charges than non smokers

plt.figure(figsize= (4,2))
plt.title('Number of Male or Female')
plt.xlabel('Sex')
plt.ylabel("Count")
plt.hist(data['sex'])
plt.show

# According to this graph male and female are almost the same on this data but number of male is higher than number of female

plt.figure(figsize=(4,2))
sns.scatterplot(data.age, data.charges,hue=data.smoker,palette= ['red','green'] ,alpha=0.6)
plt.show()

# Visually the difference between charges of smokers and charges of non-smokers is apparent


plt.figure(figsize=(4,2))
sns.scatterplot(data.age, data.charges,hue=data.sex,palette= ['pink','lightblue'] )
plt.show()

# Visually, there is no apparent relation between gender and charges

plt.figure(figsize= (4,2))
sns.heatmap(data.corr(),annot = True)
plt.show()

