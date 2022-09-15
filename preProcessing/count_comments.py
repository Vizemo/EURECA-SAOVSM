import json
import pandas as pd

of = open("2020-01-comment-count.txt", 'w', encoding='utf-8') # opens outfile
count = 0
monthYear = '01 2020'

#with open("D:\\EURECA\\processed\\2020-02.txt", 'r', encoding='utf-8') as f:
#    for line in f:
#        data = json.loads(line)
#        print(data)

#with open("D:\\EURECA\\processed\\2020-01.txt", 'r', encoding='utf-8') as f:
#    lines = f.read().splitlines()
#    print(lines)
#    df_inter = pd.DataFrame(lines)
#    count += 1
#    df_inter.columns = ['comment']

#open json file
with pd.read_json("D:\\EURECA\\processed\\2020-02.txt", lines=True, chunksize=1) as reader:
    reader
    for chunk in reader:
        print(chunk)
#print(count)
    
    
    
#    count += 1


#find the comment section count and go on to the next one




#f.write(f'{monthYear} had {count} comments.')