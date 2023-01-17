import pandas as pd

words_table_df = pd.read_excel(
    'words.xlsx', sheet_name='Sheet1')

# print(words_table_df)
print(list(words_table_df.iloc[0]))

words_table_df.set_axis(list(words_table_df.iloc[0]), axis=1, inplace=1)
words_table_df.drop(0, axis=0, inplace=True)

print(words_table_df)
