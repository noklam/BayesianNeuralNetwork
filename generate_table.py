# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 0.8.6
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd

from IPython.display import display, Markdown

results = pd.read_csv('data/competition_results.csv')

# # Cleaning

results['Date'] = pd.to_datetime(results["Date"], format="%m/%d/%Y")

results

# # Header

header = ['Competition names', 'Date', 'Rank', 'Model', 'Model Link', 'Metrics',
       'Metrics Link', 'Score']

def generate_header(ls):
    table = '<tr>'
    for column in header:
        table = table + f"<th><b>{column}</b></th>"
    table = table + '</tr>'        
    
    return table

# # Row

def generate_rows(ls):
    rows = ""
    
    for row in results.iterrows():
        rows = rows + '<tr>'
        for element in row[1].values:            
            rows = rows + f"<td><p>{element}</p></td>"
        rows = rows + '</tr>'        
    
    return rows

def generate_table(df):
    table = "<table>"
    table = table + generate_header(header)
    table = table + generate_rows(results) 
    table = table + "</table>"
    return table

Markdown(generate_table(results[header]))

table = generate_table(results[header])

print(table)

with open('table.md', 'w') as f:
    f.write(table)


