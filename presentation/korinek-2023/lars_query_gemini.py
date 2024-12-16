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
    - Uses Gemini APIkey from environment variable
    - Reads prompt from external file
"""

import os
import google.generativeai as genai
from datetime import datetime
import sys

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
)


# Read prompt from external file, given as first argument
if len(sys.argv) < 2:
    print("Usage: python lars_query_gemini.py <prompt_file>")
    sys.exit(1)

prompt_file = sys.argv[1]

with open(prompt_file) as f:
    prompt = f.read()


# Generate completion




chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message(prompt)

print(response.text)

# Write the response to a file with the .out extension
datestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = os.path.splitext(prompt_file)[0] + "_gemini_" + datestamp + ".out"
with open(output_file, "w") as f:
    f.write(response.text)

