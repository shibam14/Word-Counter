def word_counter(text):
    """
    Function to count the number of words in the given text.
    
    Args:
    text (str): The input text to count words from.
    
    Returns:
    int: The number of words in the input text.
    """
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Count the number of words
    word_count = len(words)
    return word_count

def main():
    """
    Main function to handle user input, word counting, and output.
    """
    # Prompt the user to enter a sentence or paragraph
    input_text = input("Enter a sentence or paragraph: ")
    
    # Check if the input is empty
    if not input_text.strip():
        print("Error: Empty input. Please enter some text.")
        return
    
    # Count words in the input text
    count = word_counter(input_text)
    
    # Print the word count to the console
    print("Word count:", count)

if __name__ == "__main__":
    main()