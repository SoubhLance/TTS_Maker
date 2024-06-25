# Text to Speech Converter with GUI
This Python script utilizes the gtts library (Google Text-to-Speech) and tkinter to provide a graphical user interface (GUI) for converting text into speech. Users can enter text directly in the GUI window, and the script will generate an audio file (demo.mp3) that can be played back.

# Features
- Text Input: Enter any text into the provided text area.
- Text-to-Speech Conversion: Convert the entered text into speech using the Google Text-to-Speech engine (gTTS).
- Audio Output: The generated speech is saved as demo.mp3 and played automatically using the default media player on your system.
- Error Handling: Displays error messages if there are issues during text-to-speech conversion.

# Requirements
- Python 3.x
- gtts library: Install using pip install gtts
- tkinter library (included with Python standard library)

# Usage
- Run the script (python text_to_speech_gui.py).
- Enter the text you want to convert into speech in the text area.
- Click on the "Convert to Speech" button.
- The script will generate audio.mp3 and play it using your default media player.
- Click "Quit" to close the application.

# Example
- Enter the text: "Hello! This is a test message."
- Click "Convert to Speech".
- The script will save audio.mp3 and play it, repeating the entered text as speech.

# Notes
- Ensure your system has speakers or headphones connected to hear the audio output.
- Adjust the size and appearance of the GUI widgets (Text, Button) as needed in the script (text_to_speech_gui.py).
- Customize the script further to suit your application's specific requirements or preferences.
