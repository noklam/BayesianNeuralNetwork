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

header = ['Competition names', 'Date', 'Rank', 'Model', 'Model Link', 'Metrics',
       'Metrics Link', 'Score']
results = pd.read_csv('data/competition_results.csv')
results['Date'] = pd.to_datetime(results["Date"], format="%m/%d/%Y")

# +
class MarkdownTableGenerator():    
        
    def generate_table(self, top_n_rank=5):
        "docc"
        table = results.to_html()
        with open('table.md', 'w', encoding='utf-8') as f:
            f.write(table)
        
if __name__ == '__main__':
    fire.Fire(MarkdownTableGenerator)
