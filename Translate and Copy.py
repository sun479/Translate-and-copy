# Mapping English keyboard input to Hebrew keyboard equivalent
import pyperclip

ENGLISH_TO_HEBREW = {
    'a': 'ש', 'b': 'נ', 'c': 'ב', 'd': 'ג', 'e': 'ק',
    'f': 'כ', 'g': 'ע', 'h': 'י', 'i': 'ן', 'j': 'ח',
    'k': 'ל', 'l': 'ך', 'm': 'צ', 'n': 'מ', 'o': 'ם',
    'p': 'פ', 'q': '/', 'r': 'ר', 's': 'ד', 't': 'א',
    'u': 'ו', 'v': 'ה', 'w': "'", 'x': 'ס', 'y': 'ט',
    'z': 'ז', ',': 'ת', '.': 'ץ', '/': '.',
    'A': 'ש', 'B': 'נ', 'C': 'ב', 'D': 'ג', 'E': 'ק',
    'F': 'כ', 'G': 'ע', 'H': 'י', 'I': 'ן', 'J': 'ח',
    'K': 'ל', 'L': 'ך', 'M': 'צ', 'N': 'מ', 'O': 'ם',
    'P': 'פ', 'Q': '/', 'R': 'ר', 'S': 'ד', 'T': 'א',
    'U': 'ו', 'V': 'ה', 'W': "'", 'X': 'ס', 'Y': 'ט',
    'Z': 'ז', '<': 'ת', '>': 'ץ', '?': '.'
}

def translate_to_hebrew(english_text):
    """
    Translates an English keyboard input to Hebrew keyboard equivalent.
    :param english_text: Input text typed as if on an English keyboard.
    :return: Translated Hebrew text.
    """
    hebrew_text = ""
    for char in english_text:
        hebrew_text += ENGLISH_TO_HEBREW.get(char, char)  # Default to the char if no mapping found
    return hebrew_text

def main():
    print("Welcome to the English-to-Hebrew Keyboard Translator!")
    print("Enter text typed in English keyboard layout, and it will be converted to Hebrew.")
    print("Type 'exit' to quit the application.\n")

    while True:
        english_text = input("Enter English text: ")
        if english_text.lower() == 'exit':
            print("Exiting the translator. Goodbye!")
            break
        hebrew_text = translate_to_hebrew(english_text)
        pyperclip.copy(hebrew_text)
        print(f"Translated Hebrew text: {hebrew_text}")
        print("The translated text has been copied to your clipboard.\n")

if __name__ == "__main__":
    main()
