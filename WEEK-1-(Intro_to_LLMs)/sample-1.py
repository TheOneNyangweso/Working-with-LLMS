import openai
from dotenv import load_dotenv, dotenv_values

config = dotenv_values('/home/nyangweso/Desktop/Ds_1/Working-with-LLMS/.env')

openai.api_key = config['OPENAI_API_KEY']

english_text = "Hi, I'm Sam. Nice to meet you"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f'Translate the following English text to French: "{english_text}"'}],
)

print(response['choices'][0]['message']['content'])
