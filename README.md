# Aufgabe 2, Entropie (Python)
Einsendeaufgabencode: B-MUMB01-XX1-N01  
Bearbeiter: Maxim Heibach  
Matrikelnummer: 909442      

## Aufgabe
Teilaufgaben:
1. Implementieren Sie in einer Programmiersprache Ihrer Wahl eine Funktion *entropy*, der Sie einen Text bzw. String übergeben und die sowohl die maximale Entropie Hmax sowie die tatsächliche Entropie H des übergebenen Texts bestimmt.
Hinweis: Zur Lösung der Aufgabe eignet sich eine Hashmap (in manchen Programmiersprachen auch „Dictionary“ genannt), wobei die Buchstaben als Schlüssel sowie die auftretenden Häufigkeiten als Werte abgelegt werden.  

2. Testen Sie Ihre Implementierung aus Aufgabenteil 1. mit einem String, der nur aus den Buchstaben A, B, C und D besteht mit den folgenden Auftrittswahrscheinlichkeiten:
p(A) = 0,6  
p(B) = 0,2  
p(C) = 0,15  
p(D) = 0,05   

3. Wie lauten Hmax und H für den folgenden Text:  
*"I know that virtue to be in you, Brutus, As well as I do know your outward favour. Well, honour is the subject of my story. I cannot tell what you and other men Think of this life; but, for my single self, I had as lief not be as live to be In awe of such a thing as I myself. I was born free as Caesar; so were you: We both have fed as well, and we can both Endure the winter’s cold as well as he: For once, upon a raw and gusty day, The troubled Tiber chafing with her shores, Caesar said to me ’Darest thou, Cassius, now Leap in with me into this angry flood, And swim to yonder point?’ Upon the word, Accoutred as I was, I plunged in And bade him follow; so indeed he did. The torrent roar’d, and we did buffet it With lusty sinews, throwing it aside And stemming it with hearts of controversy; But ere we could arrive the point proposed, Caesar cried ’Help me, Cassius, or I sink!’ I, as Aeneas, our great ancestor, Did from the flames of Troy upon his shoulder The old Anchises bear, so from the waves of Tiber Did I the tired Caesar. And this man Is now become a god, and Cassius is A wretched creature and must bend his body, If Caesar carelessly but nod on him. He had a fever when he was in Spain, And when the fit was on him, I did mark How he did shake: ’tis true, this god did shake; His coward lips did from their colour fly, And that same eye whose bend doth awe the world Did lose his lustre: I did hear him groan: Ay, and that tongue of his that bade the Romans Mark him and write his speeches in their books, Alas, it cried ’Give me some drink, Titinius,’ As a sick girl. Ye gods, it doth amaze me A man of such a feeble temper should So get the start of the majestic world And bear the palm alone."*

## Anleitung:
Tool in Konsole wie folgt starten:
```sh
python entropy.py "Text"
```
