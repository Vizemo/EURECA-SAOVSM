import json
import pandas as pd

#Create the output file to write the comments, scores, and subreddits to
f1 = open("vaccine_output.txt", 'w', encoding='utf-8')
f2 = open("vax_output.txt", 'w', encoding='utf-8')

temp_row = {}

#Open the text file
print("Started reading JSON input file")
with pd.read_json("2020-01.txt", lines=True, chunksize = 1000) as f:

    for chunk in f:

        #Iterate through each row in 1,000 row chunks
        for row in chunk.itertuples():

            #Split comments into words (delimite by white space)
            temp_comment = row.comment.split(' ')
            
            #Use a flag to only write each comment once, even if it says "vaccine" multiple times 
            flag = True
            
            #Iterate through each word in user comments
            for word in temp_comment:

                if flag:
                    
                    #Make all words lowercase so we don't miss terms due to capitalization
                    if(type(word) == str):
                        word = word.lower()
                    
                    #If we find a key term match, store the row into a JSON and write to output file
                    if word == "vaccine" or word == "vacine" or word == "vaccines":
                        temp_row['comment']   = row.comment
                        temp_row['score']     = row.score
                        temp_row['subreddit'] = row.subreddit
                        f1.write(json.dumps(temp_row))
                        f1.write('\n')
                        flag = False
                    
                    elif word == "vaccination" or word == "vaccinations" or word == "vaccinated":
                        temp_row['comment']   = row.comment
                        temp_row['score']     = row.score
                        temp_row['subreddit'] = row.subreddit
                        f1.write(json.dumps(temp_row))
                        f1.write('\n')
                        flag = False
                    
                    elif word == "vax" or word == "vaxx" or word == "vaxxed":
                        temp_row['comment']   = row.comment
                        temp_row['score']     = row.score
                        temp_row['subreddit'] = row.subreddit
                        f2.write(json.dumps(temp_row))
                        f2.write('\n')
                        flag = False

            print(row.Index)
