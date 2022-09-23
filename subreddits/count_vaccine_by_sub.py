total_vaccine_count = []

#Open the input file and read through each subreddit
with open('all_subreddits.txt','r', encoding='utf-8') as f:

  for line in f:
    #Chop off the last character, to remove the new line character
    line2 = line[:-1]
    
    #Pair each subreddit name with a counter
    temp = (line2, 0)

    #Add each pairing to the list
    total_vaccine_count.append(temp)

print(*total_vaccine_count, sep = "\n")
