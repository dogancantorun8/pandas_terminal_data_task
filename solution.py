#python solution.py --min-date 2020-01-22 --max-date 2020-05-08 --top 2

###parser block 
import pandas as pd
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-s', "--min-date", help="The Start Date - format YYYY-MM-DD ", required=True)
parser.add_argument('-e', "--max-date", help="The End Date format YYYY-MM-DD (Inclusive)", required=True)
parser.add_argument('-i', "--top",help="Top arguments", type=int )
start_date=sys.argv[2] 
end_date=sys.argv[4]  
top_var=int(sys.argv[6])


####Data Analysis block#############
df1 = pd.read_csv(r'product.csv')
df2 = pd.read_csv(r'store.csv')
df3 = pd.read_csv(r'sales.csv')
    #id_x = product_id and id_y=store_id 
df4=pd.merge(df3, df1, left_on = 'product', right_on = 'id', how = 'inner').drop('product', axis = 1) 
df5=pd.merge(df4, df2, left_on = 'store', right_on = 'id', how = 'inner').drop('store', axis = 1)  
df5.rename(columns={ 'name_x': 'product_name' ,'name_y' : 'store_name','id_x ': 'product_id'},inplace=True)

#Datas between two dates pandas  
df5['date'] = pd.to_datetime(df5['date']) 
mask = (df5['date'] > start_date) & (df5['date'] <= end_date) #mask operation ile aralığıma eriştim 
df_main = df5.loc[mask]
    #1)get product_name & quantitity in target range   
df_product=df_main[["product_name", "quantity"]]
print()
df_product=df_product.groupby(['product_name']).sum() 
df_product=df_product.sort_values(by='quantity', ascending=False)
print("-- top seller product --")
print(df_product.head(top_var)) 

    #2)store name & quantity in target range 
df_store=df_main[["store_name", "quantity"]]
print()
df_store=df_store.groupby(['store_name']).sum()  
df_store=df_store.sort_values(by='quantity', ascending=False) 
print("-- top seller store --")
print(df_store.head(top_var)) 

    #3)brand & quantity in target range 
df_brand=df_main[["brand", "quantity"]]
print()
df_brand=df_brand.groupby(['brand']).sum()  
df_brand=df_brand.sort_values(by='quantity', ascending=False)
print("-- top seller brand --")
print(df_brand.head(top_var)) 

    #4)city & quantity in target range  
df_city=df_main[["city", "quantity"]]
print()
df_city=df_city.groupby(['city']).sum()  
df_city=df_city.sort_values(by='quantity', ascending=False)
print("-- top seller city --")
print(df_city.head(top_var))




