import json

#Create the output file to write the subreddit frequency counts to, in order
out = open("vaccine_frequency_by_sub_ALL.txt", 'w', encoding='utf-8')

total_vaccine_count = {}
sub_list = []

#Open each subreddit frequency counter (one per month) 
f1  = open("vaccine_frequency_by_sub_01.txt", 'r', encoding='utf-8')
f2  = open("vaccine_frequency_by_sub_02.txt", 'r', encoding='utf-8')
f3  = open("vaccine_frequency_by_sub_03.txt", 'r', encoding='utf-8')
f4  = open("vaccine_frequency_by_sub_04.txt", 'r', encoding='utf-8')
f5  = open("vaccine_frequency_by_sub_05.txt", 'r', encoding='utf-8')
f6  = open("vaccine_frequency_by_sub_06.txt", 'r', encoding='utf-8')
f7  = open("vaccine_frequency_by_sub_07.txt", 'r', encoding='utf-8')
f8  = open("vaccine_frequency_by_sub_08.txt", 'r', encoding='utf-8')
f9  = open("vaccine_frequency_by_sub_09.txt", 'r', encoding='utf-8')
f10 = open("vaccine_frequency_by_sub_10.txt", 'r', encoding='utf-8')
f11 = open("vaccine_frequency_by_sub_11.txt", 'r', encoding='utf-8')
f12 = open("vaccine_frequency_by_sub_12.txt", 'r', encoding='utf-8')

subs = open("all_subs.txt", 'r', encoding='utf-8')

input_files = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]

#Add the subs to list from input file
for row in subs:

    row = row[:-2]
    #Add all subreddits to one common list
    sub_list.append(row)

#Add each item in the sub_list to the counter dictionary
count = 0
total_vaccine_count = dict.fromkeys(sub_list, count)

#Iterate through each input file
for file in input_files:
    
    #Iterate through each subreddit
    for row in file:

        #Separate row into subreddit and count
        row = row.split(' ')
        #Remove the : from the end of subreddit
        row[0] = row[0][:-1]

        #Iterate through dictionary and search for current subreddit
        for sub, count in total_vaccine_count.items():
            if sub == row[0]:
                #When you find a match, add the current count to running total count for that sub
                total_vaccine_count[sub] += int(row[1])

#Write the results to output file
for w in sorted(total_vaccine_count, key=total_vaccine_count.get, reverse=True):
    line = str(w) + ': ' + str(total_vaccine_count[w])
    out.write(line)
    out.write('\n')
