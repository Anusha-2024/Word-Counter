# Word Counter Program

def count_words(text):
    """
    Function to count the number of words in a given text.
    :param text: str - The input text from the user.
    :return: int - The number of words in the input text.
    """
    words = text.split()  # Split the text into words based on spaces
    return len(words)  # Return the number of words

def main():
    """
    Main function to handle user input, call the word counting function,
    and display the word count.
    """
    while True:
        text = input("Please enter a sentence or paragraph: ").strip()  # Get input from user and remove leading/trailing spaces
        
        if not text:
            print("Error: Input cannot be empty. Please enter some text.")  # Error handling for empty input
        else:
            word_count = count_words(text)  # Count the words using the count_words function
            print(f"The number of words is: {word_count}")  # Display the word count
            break  # Exit the loop once valid input is provided

if __name__ == "__main__":
    main()  # Run the main function
