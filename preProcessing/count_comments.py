import json
import pandas as pd

of = open("2020-01-comment-count.txt", 'w', encoding='utf-8') # opens outfile
count = 0
monthYear = '01 2020'

#with open("D:\\EURECA\\processed\\2020-01.txt", 'r', encoding='utf-8') as f:

#open json file
with pd.read_json("test_json.txt", lines=True, chunksize= 10) as reader:
    reader
    print("opened file")
    for chunk in reader:
        print(chunk)   
        break
    
#f.write(f'{monthYear} had {count} comments.')
