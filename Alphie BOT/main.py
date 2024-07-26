import tkinter as tk
from tkinter import scrolledtext
from query import queries
from nltk.chat.util import Chat, reflections


class ChatbotApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Alphie ChatBot")
        self.root.geometry('500x470')
        self.root.configure(bg='#00A0FF')
        self.root.resizable(False, False)

        self.brand_label = tk.Label(root, text="Hello, I'm Alphie", font=("Impact", 22, "bold"), bg='#00A0FF', fg='#FFF', highlightthickness=2)
        self.brand_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=51, height=18, font=("Arial", 12))
        self.chat_history.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.user_input = tk.Entry(root, width=40, font=("Georgia", 12))
        self.user_input.grid(row=2, column=0, padx=10, pady=10)
        self.user_input.bind("<Return>", lambda event: self.send_message())

        self.send_button = tk.Button(root, text="Send", command=self.send_message, font=("Impact", 12), bg="#FFFFFF")
        self.send_button.grid(row=2, column=1, padx=10, pady=10)

        # Initialize the chatbot
        self.chatbot = Chat(queries, reflections)

    def send_message(self):
        user_msg = self.user_input.get()
        self.chat_history.insert(tk.END, f"YOU : {user_msg}\n", "blue")

        response = self.chatbot.respond(user_msg)
        self.chat_history.insert(tk.END, f"ALPHIE : {response}\n", "green")

        self.user_input.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()
