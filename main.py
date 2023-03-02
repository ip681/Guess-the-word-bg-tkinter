import random
import tkinter as tk

# Определяме константи
MAX_TURNS = 12

# Създаваме графичното приложение
root = tk.Tk()
root.iconbitmap('icon.ico')
root.title("Бесеница")
root.geometry("600x350")
root.configure(bg='#e6f2ff')

# root.configure(background='white') #background color

# Определяме променливи за думата, познатите букви и грешните опити
word = random.choice(["куче", "котка", "мечка", "лисица", "лимон", "банан"])
guesses = set()
wrong_guesses = set()
wrong_attempts = 0
wrong_attempts_words = ["""
________     
|            
|            
|            
|            
|            
|            
|____________
""",
"""
________     
|      |     
|            
|            
|            
|            
|            
|____________
""",
"""
________     
|      |     
|      O     
|            
|            
|            
|            
|____________
""",
"""
________     
|      |     
|      O     
|      |     
|            
|            
|            
|____________
""",
"""
________     
|      |     
|      O     
|      |     
|      |     
|            
|            
|____________
""",
"""
________     
|      |     
|      O     
|     /|     
|      |     
|            
|            
|____________
""",
"""
________     
|      |     
|      O     
|     /|     
|    / |     
|            
|            
|____________
""",
"""
________     
|      |     
|      O     
|     /|\    
|    / |     
|            
|            
|____________
""",
"""
________     
|      |     
|      O     
|     /|\    
|    / | \   
|            
|            
|____________
""",
"""
________     
|      |     
|      O     
|     /|\    
|    / | \   
|     /      
|            
|____________
""",
"""
________     
|      |     
|      O     
|     /|\    
|    / | \   
|     /      
|    /       
|____________
""",
"""
________     
|      |     
|      O     
|     /|\    
|    / | \   
|     / \    
|    /       
|____________
""",
"""
________     
|      |     
|      O     
|     /|\    
|    / | \   
|     / \    
|    /   \   
|____________
"""
]

# Определяме функция, която връща думата за броя на грешните опити
def get_wrong_attempts_word():
    return wrong_attempts_words[wrong_attempts]


# Дефинираме функцията, която ще бъде извиквана при натискане на буква
def guess_letter(letter):
    if letter in word:
        global wrong_attempts
        guesses.add(letter)
        update_display()
        if all(letter in guesses for letter in word):
            show_message("Поздравления! Познахте думата!")
            # root.quit() # Не затваряме играта веднага след победа
    else:
        wrong_guesses.add(letter)
        wrong_attempts += 1  # увеличаваме брояча на грешните опити
        update_display()
        if wrong_attempts >= MAX_TURNS:
            show_message(f"Загубихте! Думата беше '{word}'.")
            # root.quit()  # Не затваряме играта веднага след загуба


# Дефинираме функцията, която ще обновява дисплея на играта
def update_display():
    display_word = " ".join([letter if letter in guesses else "_" for letter in word])
    display_word_label.config(text=display_word)
    wrong_guesses_label.config(text="Грешни опити: " + ", ".join(sorted(wrong_guesses)))
    # wrong_attempts_label.config(text=f"Брой грешни опити: {wrong_attempts}")  # обновяваме брояча на грешните опити
    wrong_attempts_label.config(text=f"{get_wrong_attempts_word()}")


# Дефинираме функцията, която показва съобщение на екрана
def show_message(message):
    message_label.config(text=message)


# def show_message(wrong_attempts_f):
#     if wrong_attempts == 0:
#         message_label.config(text="Започваме играта. Познай думата!")
#     elif wrong_attempts < MAX_TURNS:
#         message_label.config(text=f"Опит {wrong_attempts} от {MAX_TURNS}. Опитай отново!")
#     else:
#         message_label.config(text=f"Загубихте! Думата беше '{word}'.")


# Добавяме елементи към графичното приложение
display_word_label = tk.Label(root, text=" ".join(["_" for letter in word]), font=('Arial', 25), bg="#e6f2ff", fg="#0000FF")
display_word_label.pack()

letters_frame = tk.Frame(root)

for letter in "абвгдежзийклмнопрстуфхцчшщъьюя":
    letter_button = tk.Button(letters_frame, text=letter, command=lambda letter=letter: guess_letter(letter), bg="#e6f2ff", fg="#0000FF")
    letter_button.pack(side=tk.LEFT)

letters_frame.pack()

wrong_guesses_label = tk.Label(root, text="Грешни опити:", bg="#e6f2ff")
wrong_guesses_label.pack()

message_label = tk.Label(root, text="", bg="#e6f2ff")
message_label.pack()

# wrong_attempts_label = tk.Label(root, text="Брой грешни опити: 0")
# wrong_attempts_label.pack()

wrong_attempts_label = tk.Label(root, text=f"{get_wrong_attempts_word()}", font=('Consolas', 15), fg="#0000FF", bg="#cce6ff")
wrong_attempts_label.pack()

# Стартираме графичното приложение
root.mainloop()

print(wrong_guesses)
