from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    huggingfacehub_api_token="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"
)

model = ChatHuggingFace(llm=llm)

response = model.invoke(ask)

print(response.content)