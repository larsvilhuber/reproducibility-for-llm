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

# Set parameters

openai.api_key = "your_api_key_here" # change this to set API key for access to OpenAI API

if openai.api_key == "your_api_key_here":
    openai.api_key = input("Please enter your OpenAI API key: ")

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
