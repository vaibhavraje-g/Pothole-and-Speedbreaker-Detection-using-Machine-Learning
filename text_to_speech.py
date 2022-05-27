import gtts
from playsound import playsound
t1 = gtts.gTTS("Alert ! there is speed breaker ahead !")
t1.save("sp_ahead.mp3")
playsound("sp_ahead.mp3")
