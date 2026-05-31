from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2603",temperature=0.9,max_tokens=60
)
response = model.invoke(" Write a poem of ML")

print(response.content)

