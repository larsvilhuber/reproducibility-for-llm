"""
Replication code for "Chat 1" of the paper:

Generative AI for Economic Research: Use Cases and Implications for Economists
Journal of Economic Literature

Created by Anton Korinek in 2023 under the
Creative Commons Attribution 4.0 International License (CC BY 4.0)

Adapted by Lars Vilhuber 2024-12-14
"""

"""
OVERVIEW OF CODE:
    - Uses OPEN AI APIkey from environment variable
    - Reads prompt from external file
"""

import openai
import os
import sys

# Set parameters

openai.api_key = os.environ.get('OPENAI_API_KEY')

# If the API key isn't found in the environment variable, prompt the user for it
if not openai.api_key:
    openai.api_key = input("Please enter your OPENAI API key: ")

# Read prompt from external file, given as first argument
if len(sys.argv) < 2:
    print("Usage: python lars_query.py <prompt_file>")
    sys.exit(1)

prompt_file = sys.argv[1]

with open(prompt_file) as f:
    prompt = f.read()

model = "gpt-4o"
temperature = 0

# Generate completion

conversation = [{"role":"user", "content":prompt}]
        
completion = openai.ChatCompletion.create(
                model=model,
                temperature=temperature,
                messages=conversation)

response = completion["choices"][0]["message"]["content"]

# Print the response to the terminal
print(response)

# Write the response to a file with the .out extension
output_file = os.path.splitext(prompt_file)[0] + ".out"
with open(output_file, "w") as f:
    f.write(response)
