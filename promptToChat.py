import json

def transform_to_chat_completion(input_file_path, output_file_path):
    """
    Transforms a .jsonl file with prompt and completion pairs into a chat-completion formatted .jsonl file.
    
    Parameters:
    input_file_path (str): Path to the input .jsonl file with prompt-completion pairs.
    output_file_path (str): Path to write the output .jsonl file with chat-completion format.
    """
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            # Parse the JSON object from the .jsonl file
            data = json.loads(line.strip())

            # Create the chat-completion structure
            chat_completion = {
                "messages": [
                    {"role": "user", "content": data["prompt"]},
                    {"role": "assistant", "content": data["completion"].strip()}
                ]
            }

            # Write the transformed object to the output .jsonl file
            output_file.write(json.dumps(chat_completion) + '\n')

    print("Transformation complete. Output written to:", output_file_path)

# Replace 'input.jsonl' and 'output.jsonl' with the actual file paths on your system
transform_to_chat_completion('trevor_noah_val_data.jsonl', 'trevor_noah_val_data_chat.jsonl')
