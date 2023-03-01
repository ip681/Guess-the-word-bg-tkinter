import random
import tkinter as tk

# Определяме константи
MAX_TURNS = 12

# Създаваме графичното приложение
root = tk.Tk()
root.title("Познай думата")
root.geometry("400x300")

# Определяме променливи за думата, познатите букви и грешните опити
word = random.choice(["куче", "котка", "мечка", "лисица", "лимон", "банан"])
guesses = set()
wrong_guesses = set()

# Дефинираме функцията, която ще бъде извиквана при натискане на буква
def guess_letter(letter):
    if letter in word:
        guesses.add(letter)
        update_display()
        if all(letter in guesses for letter in word):
            show_message("Поздравления! Познахте думата!")
            root.quit()
    else:
        wrong_guesses.add(letter)
        update_display()
        if len(wrong_guesses) >= MAX_TURNS:
            show_message(f"Загубихте! Думата беше '{word}'.")
            root.quit()

# Дефинираме функцията, която ще обновява дисплея на играта
def update_display():
    display_word = "".join([letter if letter in guesses else "_" for letter in word])
    display_word_label.config(text=display_word)
    wrong_guesses_label.config(text="Грешни опити: " + ", ".join(sorted(wrong_guesses)))

# Дефинираме функцията, която показва съобщение на екрана
def show_message(message):
    message_label.config(text=message)

# Добавяме елементи към графичното приложение
display_word_label = tk.Label(root, text="".join(["_" for letter in word]))
display_word_label.pack()

letters_frame = tk.Frame(root)
for letter in "абвгдежзийклмнопрстуфхцчшщъьюя":
    letter_button = tk.Button(letters_frame, text=letter, command=lambda letter=letter: guess_letter(letter))
    letter_button.pack(side=tk.LEFT)
letters_frame.pack()

wrong_guesses_label = tk.Label(root, text="Грешни опити:")
wrong_guesses_label.pack()

message_label = tk.Label(root, text="")
message_label.pack()

# Стартираме графичното приложение
root.mainloop()