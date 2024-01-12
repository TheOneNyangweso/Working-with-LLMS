from dotenv import dotenv_values
import cohere

api_key = dotenv_values(
    dotenv_path='/home/nyangweso/Desktop/Ds_1/Working-with-LLMS/.env')['COHERE_API_KEY']
co = cohere.Client(api_key=api_key)

response = co.generate(
    prompt='Tell me about openai in 100 words',
    max_tokens=200
)

print(response.generations[0].text)