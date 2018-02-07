# Tłumacz Polsko - Angielski

Aplikacja służy do tłumaczenia słów z języka angielskiego na polski i na odwrót. Oprócz możliwości tłumaczenia ma możliwość dodawania własnych tłumaczeń jak i ich zmieniania.

### Budowa

Aplikacja korzysta z googletrans w wersji 2.2.0 do tłumaczenia i z pliku JSON z własnymi tłumaczeniami. Ideą działania jest sprawdzenie pierw czy szukane słowa nie znajdują się już w naszym lokalnym słowniku JSON. Jak tak to są one nam zwracane, jak nie to aplikacja odpytuje googletrans.

Aplikacja została zbudowana przy pomocy `tkinter`.

**Funkcja tłumacząca:**

```python
from googletrans import Translator

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
```

**Funkcja przeszukująca "nasz" słownik:**

```python
import json

def checkIfInDict(str):
    data = json.loads(open("Dict.json").read())
    for _ in range(len(data)):
        if str in data[_].values():
            return True, _
    return False, 0
```

### Sposób działania:

![alt text](https://i.imgur.com/O7nAr11.gifv "")