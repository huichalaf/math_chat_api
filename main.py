import openai
import json
import os
import sys
from functions import *
from mathGpt.algebra import *
from mathGpt.calculus import *
from mathGpt.probabilities_statistics import *
from mathGpt.linear_algebra import *
from mathGpt.geometry import *
from mathGpt.diferential_ecuations import *
from mathGpt.financial_math import *
from mathGpt.plot import create_graph
import time
import gradio as gr
import dotenv
import websockets
from retry import retry

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

@retry(tries=3, delay=1, backoff=2)
async def chat(user, user_message, temperature, max_tokens):
    state_chart = False
    user_message = await pre_process_math_prompt(user_message)
    prompt_template = user_message
    cantidad_numeros = len(await identify_numbers(user_message))
    messages = [{'role': 'user', 'content': prompt_template}, {'role': 'system', 'content': 'As a math teacher, provide a step-by-step explanation to the student in their language. Ensure that your solution is clear, concise, and easy to understand. Use examples and illustrations where necessary to aid comprehension. Avoid using technical jargon or complex terminology that may confuse the student. Remember to address the specific question asked by the student in your response. remember that you have math functions, use them'}]
    functions = await get_functions(prompt_template)
    if functions == False:
        functions = []
    start = time.time()
    data_config = await get_config()
    model = data_config["base_model"]
    #model = "gpt-3.5-turbo-0613"
    response = await openai.ChatCompletion.acreate(
        model = model,
        messages = messages,
        functions = functions,
        function_call="auto",
        max_tokens = max_tokens,
        temperature = temperature,
    )
    try:
        total_tokens = response["usage"]["total_tokens"]
        await add_daily_query_usage(user, total_tokens)
    except:
        pass
    response_message = response['choices'][0]['message']
    print(response_message)
    if response_message.get("function_call"):
        while response_message.get("function_call"):
            available_functions = {
                "evaluate_expressions": evaluate_expressions,
                "trigonometric_function": trigonometric_function,
                "integrate": calculate_integral,
                "limit": limit,
                "derivate": calculate_derivative,
                "statistics": statistics_function,
                "logarithm": logarithm_function,
                "plot": create_graph,
                "matrix_solve": matrix_solve,
                "matrix_operation": matrix_alone_operations,
                "matrix_multiplication": matrix_multiplication,
                "derivative_applications": derivative_applications,
                "integral_applications": integral_applications,
                "cartesian_transform": cartesian_transform
            }

            function_name = response_message["function_call"]["name"]
            function_to_call = available_functions[function_name]
            if function_to_call == evaluate_expressions:
                function_args = json.loads(response_message["function_call"]["arguments"])
                function_response = function_to_call(
                    function_args["expression"]
                )
            elif function_to_call == trigonometric_function:
                function_args = json.loads(response_message["function_call"]["arguments"])
                function_response = function_to_call(
                    function_args["function"],
                    function_args["number"],
                    function_args["tipo"]
                )
            elif function_to_call == calculate_integral:
                function_args = json.loads(response_message["function_call"]["arguments"])
                try:
                    a = function_args["upLimit"]
                    b = function_args["lowLimit"]
                except:
                    function_args["upLimit"] = 0
                    function_args["lowLimit"] = 0
                function_response = function_to_call(
                    function_args["function"],
                    function_args["upLimit"],
                    function_args["lowLimit"]
                )
            elif function_to_call == limit:
                function_args = json.loads(response_message["function_call"]["arguments"])
                function_response = function_to_call(
                    function_args["function"],
                    function_args["number"]
                )
            elif function_to_call == calculate_derivative:
                function_args = json.loads(response_message["function_call"]["arguments"])
                try:
                    a = function_args['number']
                except:
                    function_args['number'] = 0
                function_response = function_to_call(
                    function_args["function"],
                    function_args["number"]
                )
            elif function_to_call == statistics_function:
                function_args = json.loads(response_message["function_call"]["arguments"])
                function_response = function_to_call(
                    function_args["numbers"],
                    function_args["operation"]
                )
            elif function_to_call == logarithm_function:
                function_args = json.loads(response_message["function_call"]["arguments"])
                function_response = function_to_call(
                    function_args["base"],
                    function_args["number"]
                )
            elif function_to_call == create_graph:
                state_chart = True
                function_args = json.loads(response_message["function_call"]["arguments"])
                try:
                    a = function_args["upLimit"]
                    b = function_args["lowLimit"]
                except:
                    function_args["upLimit"] = 10
                    function_args["lowLimit"] = -10
                function_response = await function_to_call(
                    function_args["function"],
                    function_args["upLimit"],
                    function_args["lowLimit"],
                    user
                )
            elif function_to_call == matrix_solve:
                function_args = json.loads(response_message["function_call"]["arguments"])
                function_response = function_to_call(
                    function_args["matrix"],
                    function_args["vector"],
                )
            elif function_to_call == matrix_alone_operations:
                function_args = json.loads(response_message["function_call"]["arguments"])
                function_response = function_to_call(
                    function_args["matrix"],
                    function_args["operation"],
                )
            elif function_to_call == matrix_multiplication:
                function_args = json.loads(response_message["function_call"]["arguments"])
                function_response = function_to_call(
                    function_args["matrix1"],
                    function_args["matrix2"],
                )
            elif function_to_call == derivative_applications:
                function_args = json.loads(response_message["function_call"]["arguments"])
                try:
                    a = function_args["number"]
                except:
                    function_args["number"] = 0
                function_response = function_to_call(
                    function_args["operation_type"],
                    function_args["function"],
                    function_args["variable"],
                    function_args["number"],
                )
            elif function_to_call == integral_applications:
                function_args = json.loads(response_message["function_call"]["arguments"])
                try:
                    a = function_args["interval"]
                    b = function_args["axis"]
                except:
                    function_args["interval"] = "0,0"
                    function_args["axis"] = 0
                function_response = function_to_call(
                    function_args["operation_type"],
                    function_args["function"],
                    function_args["variable"],
                    function_args["interval"],
                    function_args["axis"]
                )
            elif function_to_call == cartesian_transform:
                function_args = json.loads(response_message["function_call"]["arguments"])
                function_response = function_to_call(
                    function_args["operation_type"],
                    function_args["coordinates"],
                )
            messages.append(response_message)
            messages.append({'role': 'function', 'name': function_name,'content': str(function_response)})
            second_response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo-0613",
                messages = messages,
                functions = functions,
            )
            try:
                total_tokens = second_response["usage"]["total_tokens"]
                await add_daily_query_usage(user, total_tokens)
            except:
                pass
            response_message = second_response['choices'][0]['message']
    return [response_message['content'], state_chart]

if __name__ == '__main__':
    temperature = gr.inputs.Slider(0, 1, label="Temperature")
    max_tokens = gr.inputs.Slider(1, 500, 1, label="Max Tokens")
    interface = gr.Interface(fn=chat, inputs=["text", "text", temperature, max_tokens], outputs="text")
    interface.launch()