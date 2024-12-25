# Mapping English keyboard input to Hebrew keyboard equivalent
import pyperclip  # Import pyperclip to interact with the clipboard

# Dictionary mapping English characters to Hebrew keyboard equivalents
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
    hebrew_text = ""  # Initialize an empty string to store the translated Hebrew text
    for char in english_text:  # Loop through each character in the input string
        # Lookup each character in the ENGLISH_TO_HEBREW dictionary.
        # If no match is found, return the character itself.
        hebrew_text += ENGLISH_TO_HEBREW.get(char, char)
    return hebrew_text  # Return the fully translated Hebrew text

def main():
    """
    Main function to handle user interaction and text translation.
    """
    print("Welcome to the English-to-Hebrew Keyboard Translator!")
    print("Enter text typed in English keyboard layout, and it will be converted to Hebrew.")
    print("Type 'exit' to quit the application.\n")

    while True:  # Infinite loop to keep the program running until user exits
        english_text = input("Enter English text: ")  # Prompt the user for input
        if english_text.lower() == 'exit':  # If the user types 'exit', end the loop
            print("Exiting the translator. Goodbye!")
            break  # Exit the while loop

        hebrew_text = translate_to_hebrew(english_text)  # Convert the input text to Hebrew
        pyperclip.copy(hebrew_text)  # Copy the translated Hebrew text to the clipboard
        print(f"Translated Hebrew text: {hebrew_text}")  # Display the translated text
        print("The translated text has been copied to your clipboard.\n")  # Notify the user that the text is copied

if __name__ == "__main__":
    """
    Entry point for the program to start the main function.
    """
    main()  # Call the main function to begin the translation process
