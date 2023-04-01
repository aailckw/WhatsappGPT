import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


def chat_complition(prompt: str, message_history: list) -> dict:
    try:
        last_three_conversations = message_history[-6:]  # Each conversation has a user and an assistant message, so -6
        messages = last_three_conversations.copy()
        messages.append({'role': 'user', 'content': prompt})

        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages,
            max_tokens=1024
        )


        return {
            'status': 1,
            'response': response['choices'][0]['message']['content']
        }
    except:
        return {
            'status': 0,
            'response': ''
        }


def generate_image(prompt: str) -> str:
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )

        return response['data'][0]['url']
    except:
        return ''
