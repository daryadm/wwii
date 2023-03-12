
# create a list of files
# open first file   
    # save its name
    # easyocr it from german or english
    # translate the text
    # save the text
    # indicate the end pof the file
PYDEVD_WARN_EVALUATION_TIMEOUT = 30
import os
import easyocr
from deep_translator import GoogleTranslator
reader = easyocr.Reader(['de','en'])
my_translator = GoogleTranslator(source='auto', target='en')
path_to_files = 'C:/Users/opppe/Downloads/T315 R1677/'

files = [f for f in os.listdir(path_to_files)]
for f in files:
    result = reader.readtext(path_to_files+f, detail=0, paragraph=True)
    page = ' '.join(result)
    with open("roll1677_eng.txt", "a+") as file_eng:
        file_eng.write("===================" + f + "===================\n")
        file_eng.write(page+"\n")
        file_eng.write("=========end of========" + f + "=========end of========\n" )
    my_translator.target = 'ru'
    translated_ru = my_translator.translate(page)
    with open("roll1677_rus.txt", "a+") as file_rus:
        file_rus.write("===================" + f + "===================\n")
        file_rus.write(page+"\n")
        file_rus.write("=========end of========" + f + "=========end of========\n" )

