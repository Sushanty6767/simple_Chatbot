from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2603",temperature=0.9,max_tokens=60
)
print("-----------welcome type 0 to exit---")
while True:
    prompt=input("You :")
    if prompt=="0":
        break
    response = model.invoke(prompt)

    print("Bot :",response.content)