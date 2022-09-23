total_vaccine_count = []

#Open the input file and read through each subreddit
with open('all_subreddits.txt','r', encoding='utf-8') as f:

    for line in f:
        temp = tuple(line, 0)
        total_vaccine_count.append(temp)

print(*total_vaccine_count, sep = "\n")
