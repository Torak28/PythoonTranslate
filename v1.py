# -*- coding: utf-8 -*-

import json
from googletrans import Translator

def changeDict(str, mode, nStr):
    data = json.loads(open("Dict.json").read())
    for _ in range(len(data)):
        if str in data[_].values():
            if mode == 'pl':
                data[_]['pl'] = nStr
                break
            elif mode == 'eng':
                data[_]['eng'] = nStr
                break
    json.dump(data, open('Dict.json', 'w+'))

def translateFromDict(str, it):
    data = json.loads(open("Dict.json").read())
    out = list(data[it].values())
    out.remove(str)
    return out[0]

def translateWordPL(str):
    state, num = checkIfInDict(str)
    if state:
        return translateFromDict(str, num)
    else:
        translator = Translator()
        out = translator.translate(str, dest='pl')
        return out.text


def translateWordEN(str):
    state, num = checkIfInDict(str)
    if state:
        return translateFromDict(str, num)
    else:
        translator = Translator()
        out = translator.translate(str, dest='en')
        return out.text


def checkIfInDict(str):
    data = json.loads(open("Dict.json").read())
    for _ in range(len(data)):
        if str in data[_].values():
            return True, _
    return False, 0

if __name__ == '__main__':
    mode = input('1 - tłumaczenie, 2 - dodawanie')
    if int(mode) == 1:
        num = input("Język docelowy(1 - pl, 2 - eng): ")
        str = input("Słowo do przetłumaczenia: ")
        if int(num) == 1:
            print(translateWordPL(str))
            ch = input("Chcesz zmienić znaczenie? 1 - tak, 2 - nie :")
            if int(ch) == 1:
                nStr = input("Nowe znaczenie: ")
                changeDict(str, 'pl', nStr)
        elif int(num) == 2:
            print(translateWordEN(str))
            ch = input("Chcesz zmienić znaczenie? 1 - tak, 2 - nie :")
            if int(ch) == 1:
                nStr = input("Nowe znaczenie: ")
                changeDict(str, 'eng', nStr)
    elif int(mode) == 2:
        print("TODO")
