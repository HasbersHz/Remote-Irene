"""
Абсолютно минимальный вариант для удаленного управления Ириной через командную строку
Только на нативных функциях Python
(требует файл pysimpleurl.py для GET-запросов, может быть заменен на requests, пример в run_remoteva_cmdline.py)
Может быть собран с помощью auto-py-to-exe в один файл.
"""
import json

from pysimpleurl import request

version="1.3"

# ---------- main options -------------
with open('options.json', 'r', encoding="utf-8") as f:
    saved_options = json.loads(f.read(10000000))

ttsFormat = saved_options["ttsFormat"] # "none" (TTS on server) or "saytxt" (text on client)
ttsFormatList = ttsFormat.split(",")
if ttsFormat == "saywav": ttsFormat = "saytxt" # saywav не поддерживается
baseUrl = saved_options["baseUrl"] # server with Irene WEB api

# ----- main procedure -------
if __name__ == "__main__":
    print("Remote Irene (Command line variation min) v{0} started! ttsFormat={1}, baseUrl={2}".format(version,ttsFormat,baseUrl),
          "---------------------",
          "Введите команду для голосового помощника.",
          "Пример 'привет', 'брось кубик', 'exit'.")
    cmd = input("VA CMD> ")
    while cmd not in ["exit", "q", "выход"]:
        if cmd:
            try:
                r = request(baseUrl + "sendTxtCmd", params={"cmd": cmd, "returnFormat": ttsFormat})
                if r.status == 200:
                    if r.body:
                        res = json.loads(r.body)
                        if res: # there is some response to play
                            if "restxt" in res.keys():
                                print("OUTPUT: " + res["restxt"])
                else:
                    print("Ошибка: статус не 200")
            except Exception as e:
                print("Ошибка связи с сервером (вероятно) или обработки результата", e)
        cmd = input("VA CMD> ")
