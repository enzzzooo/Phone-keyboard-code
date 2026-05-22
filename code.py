pairs = {
    "q": "1",
    "w": "2",
    "e": "3",
    "r": "4",
    "t": "5",
    "y": "6",
    "u": "7",
    "i": "8",
    "o": "9",
    "p":"0",
    "a":"-",
    "s":"/",
    "d":":",
    "f":";",
    "g":"(",
    "h":")",
    "j":"€",
    "k":"&",
    "l":"@",
    "k":"&",
    "l":"@",
    "ñ":"\"",
    "z":".",
    "x":",",
    "c":",",
    "v":"?",
    "b":"!",
    "n":"!",
    "m":"'",
    " ":" "
}
inputS = input("Enter code ")
for letter in inputS:
    letter = pairs.get(letter)
print(inputS)