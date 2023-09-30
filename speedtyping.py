import tkinter as tk
import random
import time

# Initialize the GUI
window = tk.Tk()
window.title("Speed Typing Test")

# Function to start the test
def start_test():
    global start_time
    text_entry.config(state=tk.NORMAL)
    text_entry.delete(1.0, tk.END)
    start_time = time.time()
    text_entry.focus()
    start_button.config(state=tk.DISABLED)
    finish_button.config(state=tk.NORMAL)

# Function to finish the test
def finish_test():
    end_time = time.time()
    text_entry.config(state=tk.DISABLED)
    typed_text = text_entry.get(1.0, tk.END)
    typed_words = typed_text.split()
    elapsed_time = end_time - start_time
    words_per_minute = len(typed_words) / (elapsed_time / 60)
    result_label.config(text=f"Your typing speed: {words_per_minute:.2f} WPM")
    finish_button.config(state=tk.DISABLED)
    start_button.config(state=tk.NORMAL)

# Create the test interface
start_button = tk.Button(window, text="Start Test", command=start_test)
finish_button = tk.Button(window, text="Finish Test", command=finish_test, state=tk.DISABLED)
text_entry = tk.Text(window, width=40, height=5, wrap=tk.WORD)
result_label = tk.Label(window, text="", font=("Arial", 14))

start_button.pack(pady=10)
text_entry.pack(pady=10)
finish_button.pack(pady=10)
result_label.pack()

# Start the GUI application
window.mainloop()
