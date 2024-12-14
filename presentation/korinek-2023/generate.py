"""
Replication code for the paper:

Generative AI for Economic Research: Use Cases and Implications for Economists
Journal of Economic Literature

Created by Anton Korinek and Davis Taliaferro 2023 under the
Creative Commons Attribution 4.0 International License (CC BY 4.0)
"""

"""
OVERVIEW OF CODE:
    -Reads OpenAI API Key from system variable OPENAI_API_KEY or prompts user for it
    -Takes in prompts data from file specified under "filename_prompts"
    -Outputs results into files specified under "filename_results_txt" and "filename_results_csv"
"""

import openai
import pandas as pd
import numpy as np
import os

filename_prompts = 'prompts.xlsx'
filename_results_txt = 'results.txt'
filename_results_csv = 'results.csv'

temperature = 0     # determines the variability of output

# Attempt to obtain the OpenAI API key from the environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')

# If the API key isn't found in the environment variable, prompt the user for it
if not openai.api_key:
    openai.api_key = input("Please enter your OPENAI API key: ")

#Read in prompts
prompts = pd.read_excel(filename_prompts)


#Change this to only create outputs for a specific set of prompts.
#If you want to run the entire set, set the range to [0,len(prompts)]
range_of_prompts=[0,len(prompts)]

"""
---------------------------
looping through the prompts
---------------------------
"""

#Conversation fed to the language model
conversation=[]

for index in range(range_of_prompts[0],range_of_prompts[1]):
    print("Prompt "+str(index))
    
    #Read in the model used for this prompt
    model=prompts.loc[index,"Model"]
   
    #Only carry out these tasks if the model is either of the following 
    if model=="gpt-4-0613" or model=="text-davinci-003":
        
        if(index>0):
            #Check if this is a continuation of the same conversation.
            #Otherwise, if it is a new conversation, clear conversation array.
            if(prompts.loc[index,"Chat"]!=prompts.loc[index-1,"Chat"]):
                conversation=[]
    
        #Update the conversation with the prompt, read from the prompts file
        prompt=prompts.loc[index,"Prompt"]
        conversation.append({"role":"user", "content":prompt})
        
        #Generate the completion. The syntax differs for GPT-4 and GPT-3
        if model=="gpt-4-0613":
            #Create GPT-4 completion
            x = openai.ChatCompletion.create(
                model=model,
                temperature=temperature,
                messages=conversation
                )
            completion=x["choices"][0]["message"]["content"]

        elif model=="text-davinci-003":
            #Create GPT-3 completion
            x = openai.Completion.create(
              model=model,
              prompt=conversation[0]["content"],
              max_tokens=7,
              temperature=0
            )
            completion=x["choices"][0]["text"]

        #Update the dataframe
        prompts.loc[index,["Completion", "Prompt_Tokens", "Completion_Tokens", "Total_Tokens"]]=[completion, 
            x["usage"]["prompt_tokens"], 
            x["usage"]["completion_tokens"], 
            x["usage"]["total_tokens"]]        
        #Update the conversation with the completion
        conversation.append({"role": "assistant", "content":completion})

    else:
        completion="[This completion is not implemented via API access and requires manual interaction.]"
        prompts.loc[index,["Completion"]]=[completion]        
        #Update the conversation with the completion


    index+=1



#Output 1: save model outputs to a csv file
prompts.to_csv(filename_results_csv)


#Output 2: save model outputs to a txt file

#Delimiter will go between each conversation
delimiter="---\n\n"

#Construct output by appending all conversations
output_text=""
for index in range(range_of_prompts[0],range_of_prompts[1]):
    if index>0 and not(prompts.loc[index,"Chat"]==prompts.loc[index-1,"Chat"]):
        output_text+=delimiter
    output_text+="## PROMPT: " + prompts.loc[index,"Prompt"]+"\n\n"
    output_text+="### COMPLETION (" + str(prompts.loc[index,"Model"]) + "):\n\n" + str(prompts.loc[index,"Completion"])+"\n\n"      
    
#Save all conversations to the file
with open(filename_results_txt, "w", encoding="utf-8") as text_file:
    text_file.write(output_text)
