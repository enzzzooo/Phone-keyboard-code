pairs = {
    "1": "q",
    "2": "w",
    "3": "e",
    "4": "r",
    "5": "t",
    "6": "y",
    "7": "u",
    "8": "i",
    "9": "o",
    "0": "p",
    "-": "a",
    "/": "s",
    ":": "d",
    ";": "f",
    "(": "g",
    ")": "h",
    "€": "j",
    "&": "k",
    "@": "l",
    '"': "ñ",
    ".": "z",
    ",": "c",
    "?": "v",
    "!": "n",
    "'": "m",
    " ": " "
}
inputS = input("Enter code ")
decoded = ""
for letter in inputS:
    decoded += pairs.get(letter, letter)
print(decoded)