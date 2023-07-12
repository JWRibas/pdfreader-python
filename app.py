import PyPDF2, pyttsx3

#your .pdf file
path = open('test.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(path)

speak = pyttsx3.init()

for pages in range(len(pdfReader.pages)):
    text = pdfReader.pages[pages].extract_text()
    speak.say(text)
    speak.runAndWait()
speak.stop()