import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('V3_API_KEY')
print(f"-- debug -- openai api key is {api_key[0:10]}******")

client = OpenAI(
    base_url="https://api.vveai.com/v1",
    api_key=api_key
)


response = client.chat.completions.create(
    model="o3-mini",
    messages=[
        {"role": "user", "content": "Hello world!"}
    ]
)

print(response.choices[0].message.content)


# 正常会输出结果：Hello! It's great to see you. How can I assist you today?