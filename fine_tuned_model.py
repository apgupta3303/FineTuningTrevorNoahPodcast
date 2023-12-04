from openai import OpenAI
from openai import OpenAI

client = OpenAI()
import os
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=openai_api_key)


title = "Amy Coney Barrett Joins the Supreme Court | Chelsea Handler"



MODEL = "ft:gpt-3.5-turbo-0613:personal::8RtQOcXa"
start = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f'Write me the beginning of a Trevor Noah podcast about {title}'},
    ],
    temperature=0,
    max_tokens = 3000
)

end = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f'Write me the end of a Trevor Noah podcast about {title}'},
    ],
    temperature=0,
    max_tokens = 3000
)


print(start.choices[0].message.content)
print()
print()
print()
print(end.choices[0].message.content)


with open('final.txt', 'w') as file:
    file.write("start" + '\n')
    file.write(start.choices[0].message.content + '\n')
    # file.write("mid" + '\n')
    # file.write(mid.choices[0].text + '\n')
    file.write("end" + '\n')
    file.write(end.choices[0].message.content + '\n')


