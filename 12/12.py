# Голосовой ассистент КЕША 1.0 BETA
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

# настройки
opts = {
    "alias": ('привет', 'доктор', 'врач', 'врача', 'мне плохо', 'помоги',
              'помогите', 'умираю', 'спасай', 'айболит', 'эй доктор', 'слушай а', "слушай"),
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'будь любезен', 'быстро', "включи"),
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час', 'время', 'сколько времени', 'который сейчас час',),
        "radio": ('включи музыку', 'воспроизведи радио', 'включи радио', 'буль буль', "радио"),
        "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты'),
        "security": ('врача зови', 'помоги', 'помогите', 'умираю', 'звони в скорую', 'спасай', 'айболит', 'эй доктор')
    }
}
# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Кеше
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'ctime':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'radio':
        # воспроизвести радио
        #os.system("C:\\Users\\Кулиев\\PycharmProjects\\proj1\\12\\Баловать")
        os.startfile("Баловать.mp3")
        #os.system('http://prem1.rockradio.com:80/bluesrock?9555ae7caa92404c73cade1d')

    elif cmd == 'stupid1':
        # рассказать анекдот
        speak("Около трети россиян боятся потерять работу из-за искусственного интеллекта. Зря боятся, никакой интеллект за 15 тыр работать не будет.")

    elif cmd == 'security':
        # звонить в 112
        speak("Сейчас только за телефоном сбегаю!")

    else:
        print('Команда не распознана, повторите!')


# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[-1].id)

# forced cmd test
speak("Добрый день, Сердар")
speak("Ваш персональный доктор слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)  # infinity loopдд