# Import the OpenAI library
from openai import OpenAI
import json


# Try to read the conversation history from the file; if the file doesn't exist, create an empty conversation history
def load_conversation_history(file_path):
    """
    Load conversation history from a file if it exists; otherwise, create an empty history.

    Parameters:
    - file_path (str): The path to the conversation history file.

    Returns:
    - list: The conversation history.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            context = json.load(file)
    except FileNotFoundError:
        context = []

    return context


def get_user_input():
    """
    Get user input with a predefined greeting.

    Returns:
    - str: User input.
    """
    # Predefined greeting
    greeting = "你好，我想了解三星堆的知识。"

    # Get additional input from the user
    user_input = input(greeting)

    # Combine the greeting with user input
    full_input = greeting + user_input

    return full_input


# Define the file path to save and read the conversation history
file_path = "conversation_history.json"

# Call the function to load or create the conversation history
conversation_history = load_conversation_history(file_path)

# Create an instance of the OpenAI class with your API key
client = OpenAI(
    api_key="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",
)


# Get user input and add it to the conversation history
user_input = get_user_input()

# Add the user input to the conversation history
conversation_history.append({'role': 'user', 'content': user_input})

# Make a request to the OpenAI API for chat completions
response = client.chat.completions.create(
    messages=conversation_history,
    model="gpt-3.5-turbo",
)

# Extract the content from the response
content = response.choices[0].message.content

# Print the model's response content
print(content)

# Add the model's response to the conversation history
conversation_history.append({'role': 'user', 'content': content})
