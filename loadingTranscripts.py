from PyPDF2 import PdfReader
import re
from pathToTitle import Titles
import csv
import json
from transformers import GPT2Tokenizer
import random
import tiktoken

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def num_tokens_from_string(string: str) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return num_tokens


titles = []
responses = []
for i in range(50):
    text = ''
    path = "./transcripts/transcript%d.txt" % (i+1)
    with open(path, 'r') as file:
        text = file.read()

    def cleaning(text):
        words = text.split()
        text = ' '.join(words)
        timestamp_pattern = r'\[\d{2}:\d{2}:\d{2}\]'
        return re.sub(timestamp_pattern, '', text)

    # Your transcript text would be passed to this function
    cleaned_text = cleaning(text)
    def split_into_chunks(text, chunk_size=3500):
        tokens = tokenizer.encode(text)
        chunks = []
    
        previous_end = 0
        
        while previous_end < len(tokens):
            # Calculate end index
            end_index = previous_end + chunk_size if previous_end + chunk_size < len(tokens) else len(tokens)
            
            # Check if we are in the middle of a sentence
            while end_index < len(tokens) and not tokenizer.decode([tokens[end_index]]).endswith(('.','?','!')):
                end_index += 1
            
            # Ensure we don't go past the end
            end_index = end_index + 1 if end_index < len(tokens) else len(tokens)
            
            # Decode the chunk to text
            chunk = tokenizer.decode(tokens[previous_end:end_index])
            
            # Add the chunk to the list
            chunks.append(chunk)
            
            # Update the start index for the next slice
            previous_end = end_index


            
        return chunks
    
    tokenized = split_into_chunks(cleaned_text)
    
    for j in range(len(tokenized)):
        titles.append(Titles[path])
        responses.append(tokenized[j])
prompts = []
for i in range(len(titles)):
    title = titles[i]
    first = True
    end = True
    prompt = ""
    if i > 0 and titles[i] == titles[i-1]:
        first = False
    
    if i < (len(titles)-1) and titles[i] == titles[i+1]:
        end = False

    if first and end:
        prompt = "Write me a Trevor Noah podcast about %s." % (titles[i])
    elif first:
        prompt = "Write me the beginning of a Trevor Noah podcast about %s." % (titles[i])
    elif end:
        prompt = "Write me the end of a Trevor Noah podcast about %s."  % (titles[i])
    else:
        prompt = "Write me a section of a Trevor Noah podcast about %s."  % (titles[i])
    
    prompts.append(prompt)




# Create a list of dictionaries, each containing a prompt-response pair
data_pairs = [{"prompt": prompt, "completion": response} for prompt, response in zip(prompts, responses)]

# Define the filename for your dataset
filename = "TrevorNoahTrainingData.jsonl"


with open(filename, 'w') as file:
    for pair in data_pairs:
        json_line = json.dumps(pair)
        file.write(json_line + "\n")

train_file_path = 'trevor_noah_train_data.jsonl'
val_file_path = 'trevor_noah_val_data.jsonl'

# Define your split ratio
split_ratio = 0.8  # 80% for training, 20% for testing

# Read the original file and collect all data
with open(filename, 'r') as original_file:
    lines = original_file.readlines()


# Shuffle the data
random.shuffle(lines)

# Calculate the split index
split_index = int(len(lines) * split_ratio)

# Split the data
train_data = lines[:split_index]
val_data = lines[split_index:]
# Write the split data to new files
with open(train_file_path, 'w') as train_file:
    train_file.writelines(train_data)

with open(val_file_path, 'w') as val_file:
    val_file.writelines(val_data)





