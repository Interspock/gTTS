from gtts import gTTS

# Crear una instancia de gTTS con el texto y el idioma deseado
tts = gTTS(text="mirá el churro. ¿cuanto tiempo? . un toque", lang='es')
tts.save("salida.mp3")
