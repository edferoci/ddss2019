import pandas as pd
import urllib

DOWLOAD_URL   = 'https://docs.google.com/spreadsheets/d/1Clf6VpAwHRvTxeFft2TRCbSxLvMHO14zJiyA7fH1l5Y/export?format=xlsx&id=1Clf6VpAwHRvTxeFft2TRCbSxLvMHO14zJiyA7fH1l5Y'
LOCAL_FILE    = 'words.xlsx'
urllib.urlretrieve(DOWLOAD_URL, LOCAL_FILE)

# Read imput file
df = pd.read_excel(LOCAL_FILE, header=None, names=['word'])

# Sort the dataframe and re-index according to the new order
df = df.sort_values('word')
df.reset_index(drop=True)

# Generate the output file
df['word'].to_csv('output.csv', index=False)

# Count rows
print("Words count: " + str(df.count()[0]))

# Calculate mean length
df['length']  = df['word'].str.len()
mean_word_len = df['length'].mean()
print('Mean words length: ' + str(mean_word_len))
