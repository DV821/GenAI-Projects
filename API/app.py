from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from langchain_community.llms import Ollama 
import uvicorn 
import os 
from dotenv import load_dotenv 

load_dotenv() 


os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title='Langchain Server',
    version='1.0',
    description='A Simple API Server'
)

add_routes(app, 
           ChatOpenAI(model='gpt-4.1-nano-2025-04-14'), 
           path='/openai')

model = ChatOpenAI()

llm = Ollama(model="gemma3:1b")

prompt1 = ChatPromptTemplate.from_template('Write me an essay about {topic} with 100 words')
prompt2 = ChatPromptTemplate.from_template('Write me a poem about {topic} for a 5 year old kid with 100 words') 

add_routes(app, 
           prompt1|model,
           path='/essay')

add_routes(app, 
           prompt2|llm,
           path='/poem')

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)