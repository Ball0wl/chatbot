# -*- coding: utf-8 -*-
import random

zufallsantworten =["Oh, das ist aber Interessant!", "Aha...", "Das kann man so oder so sehen..",
                   "Ich verstehe..", "Wow! War das ein Geheimnis?", "Eines Tages vielleicht..",
                   "Versuch's doch einfach nochmal!", "Nein", "Sorry! Keine ahnung was du von mir willst :)"]
reaktionsantworten = {"hallo": "guten Tag Brudi",
                      "wasgeht": "Alles was Beine hat.. also ich schon mal nicht :/",
                      "essen": "Ich schmecke nichts :( aber ich behaupte einfach mal Pizza",
                      "farbe": "Lila",
                      "deutsch": "Jawoll!",
                      "englisch": "Yes dear",
                      "chinesisch": "nope",
                      "japanisch": "nope",
                      "mandarin": "Doi Tche Ban",
                      "echt": "Ja, echt!",
                      "alt": "Ich wurde am 1. September 2022 erschaffen",
                      "tier": "Ich habe keine Tiere",
                      "mensch": "Nee..Programm",
                      "wiegehtesdir": "mir geht es gut und selbst?",
                      "gut": "super! das freut mich :)",
                      "name": "Ich bin der Awesom-O-9000",
                      "wieheisstdu":"Ich bin der Awesom-O-9000",
                      "wieheißtdu": "Ich bin der Awesom-O-9000",


}
"""datentyp dictionary/Wörterbuch, wird durch {} gekennzeichnet. erkennt in string worte und gibt abhängig davon aus
multiple ausgaben sind möglich, wenn mehrere keyworte zutreffend sind."""

print("Hallo, ich bin ein Chatbot")
print("Was willst du mit mir besprechen?")
print("Zum Beenden 'bye' eintippen")
print("")
nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
        nutzereingabe = input("Deine Frage/Antwort: ")
    nutzereingabe = nutzereingabe.lower()
    """nutzereingabe = nutzereingabe.replace(" ", "")"""
    nutzerwoerter = nutzereingabe.split()

    intelligenteAntworten = False

    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
            intelligenteAntworten = True
    if intelligenteAntworten == False:
        print(random.choice(zufallsantworten))
        print("")
exit()
print("Dir noch einen schönen Tag! Bis bald.")


