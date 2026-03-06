import os

from dotenv import load_dotenv
from openai import OpenAI

import tools as tool_functions
from tool_schemas import tools

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
You are a financial analytics assistant.
Use available tools to answer questions about Toyota stock prices.
"""


def run_agent(user_input):

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input},
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini", messages=messages, tools=tools, tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]

        name = tool_call.function.name
        args = eval(tool_call.function.arguments)

        tool_function = getattr(tool_functions, name)

        result = tool_function(**args)

        return result

    return message.content
