#!/usr/bin/env python

import json
import random
from colorama import Fore

qstr = "Quelle assertion répond le mieux à la définition ci-dessous:\n\n{}\n\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n"


def ini(fpath: str):
    jfile = open(fpath, mode="r", encoding="utf8")
    data = json.load(jfile)
    nbq = int(input("À combien de questions voulez-vous répondre?\n"))
    return data, nbq


def genrandlist(n: int, l: int):
    res = []
    while len(res) != n:
        tmp = random.randint(0, (l-1))
        if tmp not in res:
            res.append(tmp)
            pass
        pass
    return res


def askquestion(qlist):
    lnb = []
    for i in range(len(qlist)):
        lnb.append(i)
        pass
    random.shuffle(lnb)
    rep = int(input(qstr.format(qlist[0][1], qlist[lnb[0]][0],
                qlist[lnb[1]][0], qlist[lnb[2]][0], qlist[lnb[3]][0])))
    if lnb[(rep-1)] == 0 :
        print(Fore.GREEN + "Success" + Fore.RESET)
        return True
    print(Fore.RED + "Fail" + Fore.RESET)
    print("La bonne reponse est : {}".format(qlist[0][0]))
    return False


def quizz(glossaire: list, nbq: int):
    note = 0
    for i in range(nbq):
        qlist = []
        l = len(glossaire)
        rnb = genrandlist(4, l)
        for nb in rnb:
            for key, val in glossaire[nb].items():
                val = val.strip()
                qlist.append((key, val.capitalize()))
                pass
            pass
        if askquestion(qlist):
            note += 1
        pass
    print("vous avez eu {} bonne reponse sur {} question".format(note, nbq))
    pass


if __name__ == '__main__':
    data, nbq = ini("./glossaire.json")
    glossaire = data["glossaire"]
    quizz(glossaire,nbq)
    pass
