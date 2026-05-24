from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.9
)

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert."),
    ("human", "Explain in simple terms, the concept of {topic}")
])

prompt = chat_template.invoke({
    "domain": "quantum physics",
    "topic": "wormhole"
})

response = model.invoke(prompt)

print(response.content)