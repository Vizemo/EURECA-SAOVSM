from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
 
#Create output file
out = open("12_2020_vaccine_valence.txt", 'w', encoding='utf-8')
  
#Create a SentimentIntensityAnalyzer object
sid_obj = SentimentIntensityAnalyzer()

pos_count = 0
neu_count = 0
neg_count = 0
tot_count = 0
compound_total = 0

#Open the text file
print("Started reading JSON input file")
with pd.read_json("12_2020_vaccine_output.txt", lines=True, chunksize = 1, encoding='utf-8') as f:

    for chunk in f:

        #Iterate through each row in 1,000 row chunks
        for row in chunk.itertuples():
         
            # polarity_scores method of SentimentIntensityAnalyzer
            # object gives a sentiment dictionary.
            # which contains pos, neg, neu, and compound scores.
            sentiment_dict = sid_obj.polarity_scores(row.comment)
            
            #print("Overall sentiment dictionary is : ", sentiment_dict)
            #print("Sentence Overall Rated As", end = " ")
            out.write(str(sentiment_dict['compound']))
            compound_total += sentiment_dict['compound']
        
            # decide sentiment as positive, negative and neutral
            if sentiment_dict['compound'] >= 0.05 :
                pos_count += 1
        
            elif sentiment_dict['compound'] <= - 0.05 :
                neg_count += 1
        
            else :
                neu_count += 1
            
            out.write('\n')
            tot_count += 1

print("Positive: ", pos_count)
print("Neutral: " , neu_count)
print("Negative: ", neg_count)
print("Total: ",    tot_count)
print("Compound: ", compound_total)
