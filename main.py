import veryfi
import pprint
import tkinter as tk
from tkinter import filedialog
import os, sys, json

root = tk.Tk()
root.withdraw()

client_id = "vrfwrWACZRyYLPxNRO7TwnMbupfSHv9aJBk5duZ"
client_secret = "24asmDDbOS8WN3J5onV9FNCFYYkLtVVU4b4KtA0sx4JKVBmn48s9gxdxoDF1ZUr4SvKOn0NDEOckoswCGKzI1r2ZyFaKhOJctfFm01lf8LMy0oBRcrfw290NNcX3upoY"
username = "jacob.maxwell"
api_key = "4068312b429a6076c8ed5e9b130df234"

client = veryfi.Client(client_id, client_secret, username, api_key)

selectedFile = filedialog.askopenfilename()
print(selectedFile)

categories = ["Travel", "Freight", "Airfare", "Lodging", "Job Supplies and Materials", "Groceries"]
json_result = client.process_document(selectedFile, categories)

file = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')

if file:
    pprint.pprint(json_result, file)
    file.close()