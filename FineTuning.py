from openai import OpenAI
import os

openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=openai_api_key)

# Upload the dataset file
train_file_response = client.files.create(
    file=open("trevor_noah_train_data_chat.jsonl", "rb"),
    purpose="fine-tune"
)


val_file_response = client.files.create(
    file=open("trevor_noah_val_data_chat.jsonl", "rb"),
    purpose="fine-tune"
)

# Extract the file ID from the response
train_file_id = train_file_response.id
val_file_id = val_file_response.id

# Assuming the file ID is retrieved successfully, create a fine-tuning job
if train_file_id and val_file_id:
    fine_tune_response = client.fine_tuning.jobs.create(
        training_file=train_file_id,
        model="gpt-3.5-turbo",
        validation_file=val_file_id,
        hyperparameters={
            "n_epochs": 5,
        }
    )
    fine_tune_response_id = fine_tune_response.id
    print("fine_tune_response")
    print(fine_tune_response)
    print(fine_tune_response_id)
    print()


