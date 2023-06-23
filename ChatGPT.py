import tkinter as tk
from tkinter import ttk
import openai

openai.api_key = ''

root = tk.Tk()
root.title("ChatGPT")

prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack()


response_text = tk.Text(root, width=50, height=10)
response_text.pack()

def submit_prompt():
    prompt = prompt_entry.get()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    response_text.insert(tk.END, response['choices'][0]['message']['content'])


submit_button = ttk.Button(root, text="Submit", command=submit_prompt)
submit_button.pack()

root.mainloop()