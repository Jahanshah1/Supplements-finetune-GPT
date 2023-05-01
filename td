
I want to use this data to fine tune GPT-3.

Write me a python script to create prompt and completion pairs in this format:

{"prompt": "<prompt text>", "completion": "<ideal generated text>"}

{"prompt": "<prompt text>", "completion": "<ideal generated text>"}

{"prompt": "<prompt text>", "completion": "<ideal generated text>"}

I want each completion to contain a written summary of all data for a particular product using string interpolation.

When inserting the data remember to use the full name of the column from the csv,

eg 'Optimum nutrition flavours' instead of just 'Optimum Nutrition'. You must use all of the text for each column as written below (each column name is separated by a comma):

Product, Benefits of the product, Reviews of the product, difference in the product, flavours of the products, overall rating of the product, price per serving, product description, product name, and verified buyer ratings