# -*- coding: utf-8 -*-

import json
from googletrans import Translator
from tkinter import *
from PIL import Image, ImageTk

fields = 'Słowo PL', 'Słowo ENG'

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

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

def checkIfInDict(str):
    data = json.loads(open("Dict.json").read())
    for _ in range(len(data)):
        if str in data[_].values():
            return True, _
    return False, 0

def add_2_dict(pl, eng):
    data = json.load(open("Dict.json"))
    upt = {"eng" : eng, "pl" : pl}
    data.append(upt)
    json.dump(data, open('Dict.json', 'w+'))

def isWord(str):
    if ' ' in str or str == '':
        return False
    else:
        return True

def translate_2_PL(str):
    if isWord(str):
        state, num = checkIfInDict(str)
        if state:
            return translateFromDict(str, num)
        else:
            translator = Translator()
            out = translator.translate(str, dest='pl')
            return out.text
    else:
        return False

def translate_2_EN(str):
    if isWord(str):
        state, num = checkIfInDict(str)
        if state:
            return translateFromDict(str, num)
        else:
            translator = Translator()
            out = translator.translate(str, dest='en')
            return out.text
    else:
        return False

def translateButton_2_PL(str):
    out = translate_2_PL(str)
    if out is False:
        return 'Pole EN musi zawierać pojedyncze slowo!'
    else:
        return out


def translateButton_2_EN(str):
    out = translate_2_EN(str)
    if out is False:
        return 'Pole PL musi zawierać pojedyncze slowo!'
    else:
        return out

def To_Eng(e):
    e[1][1].delete(0, END)
    e[1][1].insert(0, translateButton_2_EN(e[0][1].get()))

def To_Pl(e):
    e[0][1].delete(0, END)
    e[0][1].insert(0, translateButton_2_PL(e[1][1].get()))

def clearEnts(e):
    e[0][1].delete(0, END)
    e[1][1].delete(0, END)

def Dict(e):
    if isWord(e[0][1].get()) and isWord(e[1][1].get()):
        is_PL_Dict, id_PL = checkIfInDict(e[0][1].get())
        is_EN_Dict, id_EN = checkIfInDict(e[1][1].get())
        if is_PL_Dict:
            changeDict(e[0][1].get(), 'eng', e[1][1].get())
        elif is_EN_Dict:
            changeDict(e[1][1].get(), 'pl', e[0][1].get())
        else:
            add_2_dict(e[0][1].get(), e[1][1].get())
        e[0][1].delete(0, END)
        e[0][1].insert(0, 'Dodano!')
        e[0][1].delete(0, END)
    else:
        e[0][1].delete(0, END)
        e[0][1].insert(0, 'Oba pola muszą zawierać pojedyncze slowa!')

def Info():
    window = Toplevel(root)
    photo = PhotoImage('pic.gif')
    w = Label(window, image=photo, justify=LEFT, text="Aplikacja do porostego tłumaczenia wyrazów\nAutor: Jarosław Ciołek-Żelechowski\nurl: https://github.com/Torak28/PythoonTranslate")
    w.pack(side="bottom", fill="both", expand="yes")

if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    to_eng = Button(root, text='Na Angielski', command=(lambda e=ents: To_Eng(e)))
    to_eng.pack(side=LEFT, padx=5, pady=5)
    to_pl = Button(root, text='Na Polski', command=(lambda e=ents: To_Pl(e)))
    to_pl.pack(side=LEFT, padx=5, pady=5)
    clr = Button(root, text='Czyść wejścia', command=(lambda e=ents: clearEnts(e)))
    clr.pack(side=LEFT, padx=5, pady=5)
    add_Dict = Button(root, text='Dodaj tłumaczenie', command=(lambda e=ents: Dict(e)))
    add_Dict.pack(side=LEFT, padx=5, pady=5)
    Info = Button(root, text='Info', command=Info)
    Info.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
