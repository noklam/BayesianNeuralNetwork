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
import fire

header = ['Competition Name', 'Type', 'Date', 'Model', 'Rank', 'Model Link',
       'Metrics', 'Metrics Link', 'Public Score', 'Private Score', 'Remark']
results = pd.read_csv('data/competition_results.csv')
results['Date'] = pd.to_datetime(results["Date"], format="%m/%d/%Y")

class MarkdownTableGenerator():    
    
     def generate_table(self, top_n_rank=5):
        table = results.sort_values(['Competition Name', 'Rank'])
        table = table.fillna('')
        table = table.to_html(index=False)
        
        with open('table.md', 'w', encoding='utf-8') as f:
            f.write(table)
