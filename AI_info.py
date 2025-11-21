from openai import OpenAI
from dotenv import load_dotenv
import os

#connect OpenAI client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#AI answer function
def ai_info(data):
    response = client.responses.create(
        model="gpt-5-nano",
        instructions="talking friendly, you are a weather assistant",
        input=data+'(one or two sentence to answer)',
    )

    return response.output_text
