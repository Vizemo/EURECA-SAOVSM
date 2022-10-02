import pandas as pd

#Create the output file to write the subreddit frequency counts to, in order
f1 = open("vaccine_frequency_by_sub_01.txt", 'w', encoding='utf-8')

total_vaccine_count = {}
sub_list = []

#Open the vaccination file and read through each subreddit
print("Started reading JSON input file")
with pd.read_json("vaccine_output_01.txt", lines = True, chunksize = 1000) as f:

    for chunk in f:

        #Iterate through each row in 1,000 row chunks
        for row in chunk.itertuples():

            #Add each subreddit to the list
            sub_list.append(row.subreddit)

sl_unique = [*set(sub_list)]

#Add each item in the sub_list to the counter dictionary
total_vaccine_count = dict.fromkeys(sl_unique, 0)

#Open the vaccination file and read through each comment
print("Started reading JSON input file")
with pd.read_json("vaccine_output_01.txt", lines = True, chunksize = 1000) as f:

    for chunk in f:

        #Iterate through each row in 1,000 row chunks
        for row in chunk.itertuples():

            #If the subreddit is found in all subreddit list, increment the counter
            if row.subreddit in total_vaccine_count:
               total_vaccine_count[row.subreddit] += 1
            else:
                print(row.subreddit)

#Write the results to output file
for w in sorted(total_vaccine_count, key=total_vaccine_count.get, reverse=True):
    line = str(w) +': ' + str(total_vaccine_count[w])
    f1.write(line)
    f1.write('\n')
