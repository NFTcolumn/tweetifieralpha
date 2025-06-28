import tkinter as tk
from tkinter import scrolledtext, messagebox


def tweetify_text(text: str) -> str:
    """Return tweetified version of `text`."""
    new = text.replace('\n', '')
    result = new.replace('. ', '. #hashtag1 #hashtag2 #hashtag3 yourwebsite.com \n')
    result = result.replace('! ', '! #hashtag1 #hashtag2 #hashtag3 yourwebsite.com \n')
    return result


def tweetify():
    text = input_text.get('1.0', 'end-1c')
    result = tweetify_text(text)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, result)
    with open('tweets.txt', 'w') as f:
        f.write(result)
    messagebox.showinfo('Success', 'Your content has been tweetified')


def load_content():
    try:
        with open('content.txt', 'r') as f:
            input_text.delete('1.0', tk.END)
            input_text.insert(tk.END, f.read())
    except FileNotFoundError:
        pass


root = tk.Tk()
root.title('Tweetifier GUI')

input_text = scrolledtext.ScrolledText(root, width=80, height=15)
input_text.pack(padx=10, pady=10)

btn = tk.Button(root, text='Tweetify', command=tweetify)
btn.pack(pady=(0, 10))

output_label = tk.Label(root, text='Tweetified Content:')
output_label.pack()

output_text = scrolledtext.ScrolledText(root, width=80, height=15)
output_text.pack(padx=10, pady=(0, 10))

load_content()
root.mainloop()
