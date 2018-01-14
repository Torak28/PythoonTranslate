# -*- coding: utf-8 -*-

import json, re
from googletrans import Translator


def translateWordPL(str):
    if checkIfInDict(str):
        return 'xd'
    else:
        translator = Translator()
        out = translator.translate(str, dest='pl')
        return out.text


def translateWordEN(str):
    if checkIfInDict(str):
        return 'xd'
    else:
        translator = Translator()
        out = translator.translate(str, dest='en')
        return out.text


def checkIfInDict(str):
    data = json.loads(open("Dict.json").read())
    r = re.compile("\'(.*?)\'")
    tab = r.findall(str(data[0].values()))
    if str in tab:
        return True
    return False


print(translateWordPL('horse'))
print(translateWordEN('koń'))

slownik = [
    {
        "eng": "horse",
        "pl": "koń"
    }, {
        "eng": "tree",
        "pl": "drzewo"
    }
]

json.dump(slownik, open('Dict.json', 'w+'))
