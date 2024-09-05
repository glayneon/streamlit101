import pyttsx3

speaker = pyttsx3.init()

en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
ko_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0'

# speaker.setProperty('voice', en_voice_id)
speaker.setProperty('voice', ko_voice_id)

speaker.setProperty('rate', 150)
speaker.setProperty('volume', 1.0)

text = "장한아 제발 공부 좀 하거라, 제발, 제발, 제발, 제발..."

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

pdf_path = '"C:\Users\Chase\Downloads\Handbook_Python_Final.pdf"'