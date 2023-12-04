from openai import OpenAI
import os 

openai_api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key=openai_api_key)

print(client.fine_tuning.jobs.list())