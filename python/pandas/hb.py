from networkx import dfs_predecessors
import pandas as pd


marks = {'Chemistry': [67,90,66,32], 
        'Physics': [45,92,72,40],  
        'Mathematics': [50,87,81,12],  
        'English': [19,90,72,68]}
marks_df = pd.DataFrame(marks, index = ['Subodh', 'Ram', 'Abdul', 'John'])
print(marks_df)
#2
marks_df['Total'] = marks_df['Chemistry'] + marks_df['Physics'] + marks_df['Mathematics'] + marks_df['English']
print(marks_df)
#3To drop a feature:
marks_df.drop(columns = 'Total', inplace = True)
#4
dfs_predecessors.loc[df['model_year'] == 72 ].head()


