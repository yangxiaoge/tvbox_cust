import xml.etree.ElementTree as ElementTree
import os
from googletrans import Translator
from deep_translator import GoogleTranslator


INFILE = input("Enter strings.xml file path（输入待翻译的strings.xml文件路径）")
INPUTLANGUAGE = input("Enter input language, such as (en, tr) （输入源语言，例如en, tr）")
OUTPUTLANGUAGE = input("Enter output language(s), such as: tr or (en, tr, it) （输入目标语言，例如（zh-CN, ja））")

default_output_languages = ['ar', 'hy', 'az', 'be', 'bs', 'bg', 'ca', 'hr', 'cs', 'da', 'nl', 'et', 'tl', 'fi',
                            'fr', 'ka', 'de', 'el', 'iw', 'hi', 'hu', 'is', 'id', 'ga', 'it', 'ja', 'kk', 'ko', 'la',
                            'lb', 'mk', 'ms', 'mt', 'ne', 'no', 'fa', 'pl', 'pt', 'ro', 'ru', 'sr', 'sk', 'sl', 'es',
                            'sv', 'th', 'tr', 'uk', 'ur', 'uz', 'vi', 'fil', 'he', 'zh-cn', 'zh-CN']


def create_directory_if_not_exists(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def create_directories(dir_language):
    create_directory_if_not_exists("translated")

    file_directory = "translated/" + "values-" + dir_language

    create_directory_if_not_exists(file_directory)
    return file_directory


languages_to_translate = OUTPUTLANGUAGE.split(",")

if INFILE is None:
    INFILE = "strings.xml"

if OUTPUTLANGUAGE:
    if len(languages_to_translate) == 0:
        languages_to_translate = [OUTPUTLANGUAGE.strip()]
else:
    languages_to_translate = default_output_languages

translator = Translator()
for language_name in languages_to_translate:
    language_to_translate = language_name.strip()

    translated_file_directory = create_directories(language_to_translate)
    print(" -> " + language_to_translate + " =========================")

    tree = ElementTree.parse(INFILE)
    root = tree.getroot()
    for i in range(len(root)):

        if 'translatable' not in root[i].attrib:
            value = root[i].text

            if value is not None:
                # root[i].text = translator.translate(value, src='en', dest=language_to_translate).text.title().strip()
                root[i].text = GoogleTranslator(source='auto', target=language_to_translate).translate(value) 
                print(value + "-->" + str(root[i].text))

    translated_file = translated_file_directory + "/strings.xml"

    tree.write(translated_file, encoding='utf-8')
