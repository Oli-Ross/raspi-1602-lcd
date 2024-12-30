from time import sleep 

SLEEP_BETWEEN_SCROLLS = 1.0

def squash_words(lines):
    """
    Ensure as many words as possible are on one line.
    """
    myIterator = iter(lines)
    newLines = []
    currentWord = next(myIterator, None)
    while True:
        nextWord = next(myIterator, None)
        if not nextWord:
            newLines.append(currentWord)
            return newLines
        if len(currentWord + nextWord) > 13:
            newLines.append(currentWord)
            currentWord = nextWord
            continue
        else:
            currentWord += " "
            currentWord += nextWord

def show_many_words(display, words):
    for word in words:
        assert len(word) <= 14
    for i in range(0, len(words), 2):
        word1, word2 = words[i], words[i+1] if i+1 < len(words) else None
        # Last 1 word
        if not word2:
            show_line(display, word1)
        # Last 2 words
        elif i+2 == len(words):
            show_line(display, word1)
            show_line(display, word2, secondLine=True)
        else:
            show_line(display, word1)
            word2 += 14*" "
            word2 = word2[:14] + ".."
            show_line(display, word2, secondLine=True)
        sleep(SLEEP_BETWEEN_SCROLLS)

def de_germanize(message):
    translation = str.maketrans({"ö":"oe", "ü": "ue", "ä": "ae", "ß": "ss"})
    return message.translate(translation)

def show_message(display, message):
    message = de_germanize(message)
    words = message.split(" ")
    words = squash_words(words)
    if len(words) > 2:
        show_many_words(display, words)
    elif len(words) == 2:
        show_line(display,words[0])
        show_line(display,words[1],secondLine=True)
    else:
        show_line(display,words[0])
    sleep(SLEEP_BETWEEN_SCROLLS)
    display.clear()

def show_line(display, string, secondLine=False):
    # Ensure Display isn't overflowed
    if len(string) > 16:
        string = string[0:14] + ".."
    if not secondLine:
        display.clear()
        line = 0
    else:
        line = 1
    display.cursor_pos = (line,0)
    display.write_string(string)
