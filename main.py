""" Preparation """

import os
import uvicorn
from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_TOKEN')
client = OpenAI(api_key=OPENAI_API_KEY)


app = FastAPI()

class UserData(BaseModel):
  """
  Insert Name and Age
  """
  name: str
  age: int

@app.post("/greet")
async def create_hello_message(user_data: UserData):
  """
  Create a welcoming message
  """
  promptSystemWithDataInjection= f"""
  Create a welcome message to engage with the user according to their age
  Use their name and their age and comment something about their place
  Use spanish argentinian language for responses

  be asertive and concise

  USER_DATA
  Name: {user_data.name}
  Age: {user_data.age}

  Respond with a JSON using this structure
  (
    message: your message
    score: give a score to the user according to the probability of buying a motorcicle but do not mention the topic (1 to 100) 
  )
  """

  chat_completionCustom = client.chat.completions.create(
      messages=[
        { 
            "role": "system", 
            "content": promptSystemWithDataInjection
        }
        ],
      model="gpt-3.5-turbo-0125",
      response_format={"type":"json_object"}
    )

  return chat_completionCustom.choices[0].message.content

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)