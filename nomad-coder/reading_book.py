import pyttsx3
import PyPDF2
import time


en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
ko_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0'


def playtext(text, voice_id='en'):
    speaker = pyttsx3.init()
    
    if voice_id == 'en':
        speaker.setProperty('voice', en_voice_id)
    elif voice_id == 'ko':
        speaker.setProperty('voice', ko_voice_id)

    speaker.setProperty('rate', 150)
    speaker.setProperty('volume', 1.0)

    speaker.say(text)
    speaker.runAndWait()

# voices = speaker.getProperty('voices')
# for voice in voices:
#     print("Voice:")
#     print(" - ID: %s" % voice.id)
#     print(" - Name: %s" % voice.name)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)

def pdf_to_text(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the text
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        return text


hans_routines = [
    '피아노 쳤니?',
    '강의 다 들었니?',
    '책 읽었니?',
    '숙제 다 했니?',
]

for routine in hans_routines:
    routine = f"장한아, {routine}, 젭알!! 젭알!!"
    playtext(routine, 'ko')
    time.sleep(3)

# if __name__ == "__main__":
#     pdf_path = r"C:\Users\Chase\Downloads\Handbook_Python_Final.pdf"

#     text = pdf_to_text(pdf_path)
#     playtext(text, 'ko')

#     print("PDF converted to text successfully!")