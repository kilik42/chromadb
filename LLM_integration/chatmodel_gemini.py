from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.9)
prompt ="what is the capital of France?"
result  = model.invoke(prompt)

print(result.content)
#python LLM_integration/chatmodel_gemini.py