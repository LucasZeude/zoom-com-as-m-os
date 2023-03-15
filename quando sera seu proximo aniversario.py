from datetime import date

anoatu = date.today().year
mesatu = date.today().month
diaatu = date.today().day

anoani = int(input('qual ano você nasceu: '))
diaani = int(input('qual dia você nasceu: '))
mesani = int(input('qual mes você nasceu: '))

if mesani > mesatu and diaatu >= diaani:
    print(f'falta {(mesani - mesatu) - 1} meses')

elif mesatu == mesani and diaatu > diaani:
    print(f'falta 11 meses')

elif mesani >= mesatu:
    print(f'falta {mesani - mesatu} meses')

elif mesani < mesatu and diaatu >= diaani:
    print(f'falta {11 - (mesatu - mesani)} meses')

else:
    print(f'falta {12 - (mesatu - mesani)} meses')

if mesatu - mesani == 0 and diaatu > diaani:
    print(f'falta {diaani} dias')

elif diaatu >= diaani:
    print(f'falta {30 - (diaatu - diaani)} dias')

elif diaani >= diaatu:
    print(f'falta {diaani -diaatu} dias')

if mesatu - mesani == 0 and diaatu - diaani == 0:
    print(f'hoje e seu aniversario de {anoatu - anoani} anos')

elif mesani > mesatu or mesatu == mesani and diaani > diaatu:
    print(f'voce tem {(anoatu - 1) - anoani} anos')

else:
    print(f"voce tem {anoatu - anoani} anos")
