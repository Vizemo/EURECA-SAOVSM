#Create counter variable to store number of subreddits and file writer to rewrite sub names with 'r/' prefix
counter = 0
outfile = open("all_subreddits.txt", 'w', encoding='utf-8')

#Open the input file and read through each subreddit
with open('all_subreddits_raw.txt','r', encoding='utf-8') as f:

    for line in f:

        #Increment the counter
        counter += 1

        #Write the subreddit names to the output file with 'r/' appended to the front
        final_name = 'r/' + line
        outfile.write(final_name)

print("Total number of subreddits: ", counter)
