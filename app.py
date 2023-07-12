import PyPDF2, pyttsx3, tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

upload_file = input("Upload your file now? (y/n): ")

if upload_file == 'y':
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
else:
    pdf_path = input("Enter the path to the PDF file: ")

#your .pdf file
path = open(pdf_path, 'rb')

pdfReader = PyPDF2.PdfReader(path)

engine = pyttsx3.init()

# Get list of available voices
voices = engine.getProperty('voices')

print("Select a voice:")
for i, voice in enumerate(voices):
    language = voice.languages[0] if voice.languages else "Unknown"
    print(f"{i+1}: {voice.name} ({language})")

# Get user selection
voice_selection = int(input("Enter the number of the desired voice: ")) - 1

# Set selected voice
engine.setProperty('voice', voices[voice_selection].id)

start_reading = input("Start reading? (y) or Quit (q): ")

if start_reading == 'y':
    for pages in range(len(pdfReader.pages)):
        text = pdfReader.pages[pages].extract_text()
        engine.say(text)
        engine.runAndWait()
        user_input = input("Press 'c' to continue or 'q' to quit: ")
        if user_input == 'q':
            break
engine.stop()






