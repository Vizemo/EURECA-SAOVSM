import pandas



f = open("comment_count_01-2020.txt", 'w', encoding='utf-8') # opens outfile
count = 0
monthYear = '01 2020'

#open json file
while pandas.read_json("2020-01.txt", lines=True, chunksize=10000):
    
    
    
    
    
    
    count += 1


#find the comment section count and go on to the next one




f.write(f'{monthYear} had {count} comments.')