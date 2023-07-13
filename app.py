import PyPDF2, pyttsx3, tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pdf2image.pdf2image import convert_from_path 

def load_pdf():
    global images, pdfReader
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if pdf_path:
        path = open(pdf_path, 'rb')
        pdfReader = PyPDF2.PdfReader(path)
        images = convert_from_path(pdf_path)
        status_label.config(text="PDF carregado com sucesso!")
        start_button.config(state=tk.NORMAL)


def start_reading():
    engine.setProperty('voice', voice_selection.get())
    for page in range(len(pdfReader.pages)):
        text = pdfReader.pages[page].extract_text()
        image = ImageTk.PhotoImage(images[page])
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        engine.say(text)
        engine.runAndWait()


def stop_reading():
    engine.stop()

root = tk.Tk()

engine = pyttsx3.init()

# Get list of available voices
voices = engine.getProperty('voices')

voice_label = tk.Label(root, text="Selecione uma voz:")
voice_label.pack()

voice_selection = tk.StringVar(root)
voice_selection.set(voices[0].name)

voice_menu = tk.OptionMenu(root, voice_selection, *[voice.name for voice in voices])
voice_menu.pack()

load_button = tk.Button(root, text="Carregar PDF", command=load_pdf)
load_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

start_button = tk.Button(root, text="Iniciar leitura", command=start_reading, state=tk.DISABLED)
start_button.pack()

stop_button = tk.Button(root, text="Parar leitura", command=stop_reading)
stop_button.pack()

canvas = tk.Canvas(root, width=300, height=400)
canvas.pack()

root.mainloop()




