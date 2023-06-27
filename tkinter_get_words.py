#!/usr/bin/python3
import tkinter as tk

def add_word():
    word = entry_word.get()
    if word:
        word_list.insert(tk.END, word)
        entry_word.delete(0, tk.END)

def clear_list():
    word_list.delete(0, tk.END)

def create_word_list():
    num_words = int(entry_num_words.get())
    words = []
    for _ in range(num_words):
        if word_list.size() > 0:
            words.append(word_list.get(0))
            word_list.delete(0)
    return words

root = tk.Tk()
root.title("Word List")

label_num_words = tk.Label(root, text="How many words do you want?")
label_num_words.pack()

entry_num_words = tk.Entry(root)
entry_num_words.pack()

label_word = tk.Label(root, text="Input Words:")
label_word.pack()


entry_word = tk.Entry(root)
entry_word.pack()

button_add = tk.Button(root, text="Add", command=add_word)
button_add.pack()

word_list = tk.Listbox(root)
word_list.pack()

button_clear = tk.Button(root, text="Clear List", command=clear_list)
button_clear.pack()

button_create = tk.Button(root, text="Create Word List", command=root.quit)
button_create.pack()

root.mainloop()

# Access the word list after Tkinter window is closed
words = create_word_list()
print(words)  # Do something with the words list

def get_words_2():
    return words
