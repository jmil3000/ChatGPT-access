import os
import openai
import gradio as gr 

YOUR_API_KEY = "sk-x"  
openai.api_key = YOUR_API_KEY

start_sequence = "\AI:"
restart_sequence = "\Human:"

prompt = "The following is a conversation with an AI assistant: "

def openai_create(prompt):
    response = openai.Completion.create(
           model = "gpt-3.5-turbo",
           prompt = prompt,
           temperature = 0.9,
           max_tokens=150, 
           top_p=1,
           frequency_penalty=0, 
           presence_penalty=0.6, 
           stop=[" Human:", " AI:"]
       ) 
    return response.choices[0].text

def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history 

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>My chatGPT</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])
    
block.launch(debug = True)
