import pandas as pd

def get_word(key,source_language,dest_language):
    words_table_df = pd.read_excel(
        'words.xlsx', sheet_name='Sheet1')

    words_table_df = words_table_df.set_axis(list(words_table_df.iloc[0]), axis=1)
    words_table_df = words_table_df.set_axis(list(words_table_df[source_language.capitalize()]), axis=0)

    # return words_table_df.loc[]
    return{
        source_language: key,
        dest_language: words_table_df.loc[key][dest_language.capitalize()]
    }

# get_word('able','english','russian')