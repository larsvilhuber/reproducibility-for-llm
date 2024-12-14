"""
Replication code for "Chat 1" of the paper:

Generative AI for Economic Research: Use Cases and Implications for Economists
Journal of Economic Literature

Created by Anton Korinek in 2023 under the
Creative Commons Attribution 4.0 International License (CC BY 4.0)
"""

"""
OVERVIEW OF CODE:
    - Requires user to input their API key in line 19
    - Demonstrates simple use of the OpenAI API
"""

import openai
import os

# Set parameters

openai.api_key = os.environ.get('OPENAI_API_KEY')

# If the API key isn't found in the environment variable, prompt the user for it
if not openai.api_key:
    openai.api_key = input("Please enter your OPENAI API key: ")

prompt = "Can you brainstorm 20 channels through which AI may increase inequality? Limit your response to 10 words for each point."
model = "gpt-4-0613"
temperature = 0


# Generate completion

conversation = [{"role":"user", "content":prompt}]
        
completion = openai.ChatCompletion.create(
                model=model,
                temperature=temperature,
                messages=conversation)

response=completion["choices"][0]["message"]["content"]

print(response)
