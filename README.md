# pandas_terminal_data_task 

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)   
![code quality score ]https://www.code-inspector.com/project/21979/score/svg 
![code quality grade ]https://www.code-inspector.com/project/21979/status/svg

Question

Write a python script using pandas that finds and prints:

top seller n products in given date range (product name & quantity)
top seller n stores in given date range (store name & quantity)
top seller n brands in given date range (brand & quantity)
top seller n cities in given date range (city & quantity)
On equality, print all of the rows.

Input Data Format

product.csv

id: identifier of the product
name: name of the product
brand: brand of the product
store.csv

id: identifier of the store
name: name of the store
city: city that the store is located in
sales.csv

product: identifier of the product (id column in product.csv)
store: identifier of the product (id column in product.csv)
date: date of sale
quantity: sales quantity of the specified product in the specified store
Arguments

Your script should take following arguments from command line:

"--min-date": start of the date range. type:str, format:"YYYY-MM-DD", default:"2020-01-01"
"--max-date": end of the date range. type:str, format:"YYYY-MM-DD", default:"2020-06-30"
"--top": number of rows in the output. type:int, default:3
Expected command and output:

$ python3 solution.py --min-date 2020-02-01 --max-date 2020-06-30 --top 2

![pandas_terminal](https://user-images.githubusercontent.com/48547417/116120366-21764080-a6c8-11eb-8bd8-aea58ef76bce.PNG)

