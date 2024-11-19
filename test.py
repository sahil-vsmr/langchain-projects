from langchain.llms import openai
import os 

print(os.environment(["OPENAI_API_KEY"]))
# llm = openai(open_api_key = temperature=1)