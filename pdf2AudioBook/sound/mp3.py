from gtts import gTTS

def convertStringToMp3(content:str, fname:str):
    t2s = gTTS(content)
    t2s.save(f'{fname}.mp3')
    return fname
