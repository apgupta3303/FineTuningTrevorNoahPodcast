import tiktoken
from PyPDF2 import PdfReader
import re


path = "./test.txt"
print(path)
with open(path, 'r') as file:
    text = file.read()

def cleaning(text):
    words = text.split()
    text = ' '.join(words)
    timestamp_pattern = r'\[\d{2}:\d{2}:\d{2}\]'
    return re.sub(timestamp_pattern, '', text)


def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return num_tokens

# text = ""
# path = "./transcripts/transcript1.pdf"
# with open(path, 'rb') as file:
#     reader = PdfReader(file)
        
#     # Iterate through each page and extract text
#     for page in reader.pages:
#         text += page.extract_text()

print(num_tokens_from_string(text))