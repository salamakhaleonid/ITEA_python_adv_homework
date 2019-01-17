

def polindrom(word):
    if word[0] == word[-1]:
        word = word[1:-1]
        if len(word) != 1 and len(word) != 0:
            if polindrom(word):
                return True
            else:
                return False
        else:
            return True

if __name__ == "__main__":
    print polindrom("asdfdsa")
