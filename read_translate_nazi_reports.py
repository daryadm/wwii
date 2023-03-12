PYDEVD_WARN_EVALUATION_TIMEOUT = 30
import os
import easyocr
from deep_translator import GoogleTranslator
reader = easyocr.Reader(['de','en'])
path_to_files = 'C:/Users/opppe/Downloads/T315 R1677/'
files = [f for f in os.listdir(path_to_files)]

for f in files:
    result = reader.readtext(path_to_files+f, detail=0, paragraph=True)
    page = ' '.join(result)
    my_translator = GoogleTranslator(source='auto', target='en')
    translated_eng = my_translator.translate(page)
    my_translator.target = 'ru'
    translated_rus = my_translator.translate(page)
    with open("roll1677_deu.txt", "a+", encoding="utf8") as file_deu:      
        file_deu.write("=================== " + f + " ===================\n")
        file_deu.write(page + "\n")
        file_deu.write("=========end of======== " + f + " =================\n" )
    with open("roll1677_eng.txt", "a+", encoding="utf8") as file_eng:      
        file_eng.write("=================== " + f + " ===================\n")
        file_eng.write(translated_eng + "\n")
        file_eng.write("=========end of======== " + f + " =================\n" )
    with open("roll1677_rus.txt", "a+", encoding="utf8") as file_rus:
        file_rus.write("=================== " + f + " ===================\n")
        file_rus.write(translated_rus + "\n")
        file_rus.write("=========end of======== " + f + " =================\n" )

