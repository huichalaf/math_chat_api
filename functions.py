import openai
import os
from dotenv import load_dotenv
import json
import pandas as pd
import numpy as np

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def cosine_similarity(embedding1, embedding2):
    return np.dot(embedding1, embedding2)/(np.linalg.norm(embedding1)*np.linalg.norm(embedding2))

async def get_user(user):
    #dividimos por ;
    user = user.split(";")[0]
    #quitamos user=
    user = user.replace("user=", "")
    user = user.replace("%40", "@")
    return user

async def get_config():
    with open("config.json", "r") as json_file:
        data = json.load(json_file)
    return data

async def pre_process_math_prompt(prompt):
    
    prompt_lista = list(prompt)
    prompt_to_return = ''
    for i in range(len(prompt_lista)):
        if prompt_lista[i].isdigit():
            prompt_to_return += prompt_lista[i]
            if i+1 < len(prompt_lista):
                if prompt_lista[i+1] in ['+', '-', '*', 'x', '/', '^', 'sqrt', '√']:
                    prompt_to_return += ' '
        elif prompt_lista[i] == '.':
            prompt_to_return += prompt_lista[i]
        elif prompt_lista[i] in ['+', '-', 'x', '/', '^', 'sqrt', '√']:
            prompt_to_return += ' ' + prompt_lista[i] + ' '
        elif prompt_lista[i] == '*' and prompt_lista[i+1] == '*':
            prompt_to_return += ' ' + prompt_lista[i] + prompt_lista[i+1] + ' '
        elif prompt_lista[i] == '*' and prompt_lista[i+1] != '*' and prompt_lista[i-1] != '*':
            prompt_to_return += ' ' + prompt_lista[i] + ' '
        else:
            if prompt_lista[i] != '*':
                prompt_to_return += prompt_lista[i]
            else:
                pass
    return prompt_to_return

async def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    result = await openai.Embedding.acreate(input=[text], model=model)
    result_data = result['data'][0]['embedding']
    return result_data

async def read_embeddings_from_csv(file_path):
    functions_embeddings = pd.read_csv(file_path)
    embeddings = functions_embeddings["embedding"].tolist()
    embeddings = [eval(embedding) for embedding in embeddings]
    names = functions_embeddings["name"].tolist()
    descriptions = functions_embeddings["description"].tolist()
    return names, descriptions, embeddings

async def get_functions(prompt):
    embedding_prompt = await get_embedding(prompt)
    with open("functions.json", "r") as json_file:
        data = json.load(json_file)
    functions = data
    names, descriptions, functions_embeddings = await read_embeddings_from_csv("embed_functions.csv")
    similarities = []
    for embedding in functions_embeddings:
        similarities.append(await cosine_similarity(embedding_prompt, embedding))
    #filtramos por todas las que tengan similarities menor a 0.7
    functions_past = functions
    functions = [function for function, similarity in zip(functions, similarities) if similarity > 0.725]
    similarities_past = similarities
    similarities = [similarity for similarity in similarities if similarity > 0.725]
    if len(functions) == 0:
        #retornamos la funcion mas similar    
        max_similarity = max(similarities_past)
        index = similarities_past.index(max_similarity)
        function = functions_past[index]
        return [function]
    try:
        max1 = max(similarities)
        index1 = similarities.index(max1)
        function1 = functions[index1]
        similarities.pop(index1)
        functions.pop(index1)
    except:
        return False
    try:
        max2 = max(similarities)
        index2 = similarities.index(max2)
        function2 = functions[index2]
        similarities.pop(index2)
        functions.pop(index2)
    except:
        return [function1]
    try:
        max3 = max(similarities)
        index3 = similarities.index(max3)
        function3 = functions[index3]
        similarities.pop(index3)
        functions.pop(index3)
    except:
        return function1, function2
    try:
        max4 = max(similarities)
        index4 = similarities.index(max4)
        function4 = functions[index4]
        similarities.pop(index4)
        functions.pop(index4)
    except:
        return function1, function2, function3
    try:
        max5 = max(similarities)
        index5 = similarities.index(max5)
        function5 = functions[index5]
        similarities.pop(index5)
        functions.pop(index5)
    except:
        return function1, function2, function3, function4
    
    return function1, function2, function3, function4, function5

async def identify_numbers(text):
    text_list = list(text)
    numbers = []
    number = ''
    for t in text_list:
        if t.isdigit():
            number += t
        elif t == '.':
            number += t
        elif number != '':
            numbers.append(float(number))
            number = ''
    if number != '':
        numbers.append(float(number))
    return numbers