import json
import zstandard
from zstandard import ZstdDecompressor

with open("RC_2020-01.zst", 'rb') as fh:
    dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)
    
    #Create the output file to write the comments, scores, and subreddits to
    f1 = open("vaccine_output.txt", 'w', encoding='utf-8')
    f2 = open("vax_output.txt", 'w', encoding='utf-8')
    f3 = open("jab_output.txt", 'w', encoding='utf-8')
    data = {}

    with dctx.stream_reader(fh) as reader:
        previous_line = ""
        
        while True:
            chunk = reader.read(2**24)  # 16mb chunks
            if not chunk:
                break

            string_data = chunk.decode('utf-8')
            lines = string_data.split("\n")

            for i, line in enumerate(lines[:-1]):
                if i == 0:
                   line = previous_line + line
                object = json.loads(line)

                #Store the relevant information in our JSON
                data['comment'] = object['body']
                data['score'] = object['score']
                data['subreddit'] = object['subreddit']
                
                #Load our JSON data in a writable format
                json_data = json.dumps(data)

                #Write our JSON to the appropriate output file if a key term is found
                
                # read through each word of the comments only (don't count instances of "vaccine" in subreddit names)
                for word in data['comment']:

                    # make all words lowercase so we don't miss terms due to capitalization
                    word = word.lower()

                    # check for the relevant terms  
                    # use contains() method so we don't miss terms due to punctuation          
                    if word.__contains__("vaccine") or word.__contains__("vacine") or word.__contains__("vaccines"):
                        f1.write(json_data)
                    elif word.__contains__("vaccination") or word.__contains__("vaccinations"):
                        f1.write(json_data)
                    elif word.__contains__("vax") or word.__contains__("vaxx"):
                        f2.write(json_data)
                    elif word.__contains__("jab"):
                        f3.write(json_data)
                
            previous_line = lines[-1]