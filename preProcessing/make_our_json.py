import json
import zstd
import zstandard
from zstandard import ZstdDecompressor

with open("RC_2020-03.zst", 'rb') as fh:
    dctx = zstandard.ZstdDecompressor(max_window_size=2147483648)
    f = open("sub_count_input.txt", 'w', encoding='utf-8')
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

                #Write our JSON to the output file
                f.write(json_data)

            previous_line = lines[-1]