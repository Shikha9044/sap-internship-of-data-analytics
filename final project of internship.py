import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import plotly.express as px
shop = pd.read_csv('shopping_trends_updated.csv')
shop.shape
shop.to_excel('shopping_trends_updated.xlsx')
shop.head()
shop.dtypes
shop.columns
shop.info()
shop.shape
shop.isnull().sum()
#question 1
shop['Age'].value_counts()
shop['Age'].mean()
shop['Gender'].unique()
shop['Age_category']=pd.cut(shop['Age'],bins=[0,15, 18 , 30 , 50 , 70],labels=['child','teen','Young Adults','Middle-Aged Adults','old'] )
fig = px.histogram(shop , y = 'Age' , x = 'Age_category')
fig.show()
#question 2
shop['Category'].unique()
shop.groupby('Category')['Purchase Amount (USD)'].mean()
#question 3
sns.barplot(shop , x = 'Gender' , y = 'Purchase Amount (USD)')
#question 4
shop.groupby('Category')['Item Purchased'].value_counts()
fig = px.histogram(shop , x = 'Item Purchased' , color = 'Category')
fig.show()
#question 5
shop['Season'].unique()
shop[shop['Season'] == 'Summer'].value_counts().sum()
shop[shop['Season'] == 'Winter'].value_counts().sum()
shop[shop['Season'] == 'Spring'].value_counts().sum()
shop[shop['Season'] == 'Fall'].value_counts().sum()
fig = px.histogram(shop , x = 'Season' , range_y= [200 , 1500] )
fig.show()
#question 6
shop_groupby = shop.groupby('Category')['Review Rating'].mean().reset_index()
fig = px.bar(shop_groupby ,x= 'Category' , y = 'Review Rating' )
fig.show()
#question 7
shop['Subscription Status'].unique()
sns.barplot(shop  , x = 'Subscription Status' , y = 'Purchase Amount (USD)')
shop['Purchase Amount (USD)'].sum()
shop.groupby('Subscription Status')['Purchase Amount (USD)'].mean()
#question 8
shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().sort_values(ascending= False)
shop_groupby = shop.groupby('Payment Method')['Purchase Amount (USD)'].mean().reset_index()
fig = px.bar(shop_groupby , x = 'Payment Method' , y = 'Purchase Amount (USD)')
fig.show()
sns.barplot(shop ,x='Payment Method' , y = 'Purchase Amount (USD)')
#question 9
shop_groupby  = shop.groupby('Promo Code Used')['Purchase Amount (USD)'].sum().reset_index()
fig = px.sunburst(shop , path=['Gender' , 'Promo Code Used'] , values='Purchase Amount (USD)')
fig.show()
fig  =  px.bar(shop_groupby , x= 'Promo Code Used' , y = 'Purchase Amount (USD)')
fig.show()
#question 10
shop[['Age' , 'Age_category']]
shop['Age_category'].unique()
shop_group = shop.groupby('Frequency of Purchases')['Age'].sum()
px.sunburst(shop , path=['Frequency of Purchases','Age_category'] , values='Age')
#11
shop_group = shop.groupby('Size')['Purchase Amount (USD)'].sum().reset_index()
fig  = px.bar(shop_group , x = 'Size' , y ='Purchase Amount (USD)'  )
fig.show()
#12
shop.groupby('Category')['Shipping Type'].value_counts().sort_values(ascending= False)
shop['Shipping_Category'] =shop['Shipping Type'].map({'Express': 0, 'Free Shipping': 1, 'Next Day Air': 2,  'Standard': 3, '2-Day Shipping': 4, 'Store Pickup': 5})
shop['Category'].unique()
shop['Category_num'] =shop['Category'].map({'Clothing':1, 'Footwear':2, 'Outerwear':3, 'Accessories':4})
#13
shop_group = shop.groupby('Discount Applied')['Purchase Amount (USD)'].sum().reset_index()
px.histogram(shop_group , x = 'Discount Applied' , y = 'Purchase Amount (USD)')
fig = px.sunburst(shop , path = ['Gender' , 'Discount Applied'], values='Purchase Amount (USD)' , color= 'Gender')
fig.show()
#14
px.histogram(shop , x = 'Color')
shop['Color'].value_counts().nlargest(5)
#15
shop['Color'].value_counts().nlargest(5)
#16
shop.groupby('Location')['Purchase Amount (USD)'].mean().sort_values(ascending = False)
shop_group = shop.groupby('Location')['Purchase Amount (USD)'].mean().reset_index()
fig = px.bar(shop_group, x = 'Location' , y = 'Purchase Amount (USD)')
fig.show()
#17
shop_group = shop.groupby('Category')['Age'].mean().reset_index()
fig = px.bar(shop_group ,y = 'Age' , x= 'Category')
fig.show()
#18
shop_group = shop.groupby('Gender')['Purchase Amount (USD)'].sum().reset_index()
fig = px.bar(shop_group , x = 'Gender' , y = 'Purchase Amount (USD)')
fig.show()
px.sunburst(data_frame= shop , path = ['Gender' ,'Age_category'] , values='Purchase Amount (USD)')
