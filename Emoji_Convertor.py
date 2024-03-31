message = input("> ")
words = message.split(' ')                      # Cannot just do '' for a space delimitor. Must type out the space ' '
print(words)


emojis = {
    ":)": "😊",
    ":(": "😒",
    ":o": "😯",
    "B)": "😎",
    ":|": "😐",
    ":P": "😜",
    ":0": "😮"
}

output = ''
for word in words:
    output += f'{emojis.get(word, word)} '
print(output)