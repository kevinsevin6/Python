# Create a function with the emoji converter.

#-----------------------------------------------------
#emojis = {
#    ":)": "😊",
#    ":(": "😒",
#    ":o": "😯",
#    "B)": "😎",
#    ":|": "😐",
#    ":P": "😜",
#    ":0": "😮"
#}

#output = ''
#for word in words:
#    output += f'{emojis.get(word, word)} '
#print(output)
#------------------------------------------------------------------

def emoji_converter(message):
    words = message.split(' ')
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
    return output


anything = input("> ")
print(emoji_converter(anything))