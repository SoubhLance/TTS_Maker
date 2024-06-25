from gtts import gTTS
import os
import tkinter as tk
from tkinter import ttk, messagebox

# Function to generate speech from input text
def generate_speech():
    input_text = text_entry.get("1.0", "end-1c").strip()  # Get text from the Text widget
    if input_text:
        try:
            language = "en"  # Set language (English)
            voice = gTTS(text=input_text, lang=language, slow=False)
            voice.save("audio.mp3")
            os.system("start audio.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

# Create the main tkinter window
root = tk.Tk()
root.title("Text to Speech Converter")

# Create a Text widget for input
text_entry = tk.Text(root, width=50, height=10, wrap=tk.WORD)
text_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Button to trigger text-to-speech conversion
convert_button = ttk.Button(root, text="Convert to Speech", command=generate_speech)
convert_button.grid(row=1, column=0, padx=10, pady=10)

# Button to close the application
quit_button = ttk.Button(root, text="Quit", command=root.quit)
quit_button.grid(row=1, column=1, padx=10, pady=10)

# Start the tkinter main loop
root.mainloop()
