# Assignment 5: Read a text file and generate the following information:
#   1) Total word count (number of words in the file)
#   2) Total stopword count (number of stopwords in the file)
#   3) Dictionary of words, and their frequencies, that occur >= 70 times

# this import is needed to reference the String constant, string.punctuation
import string


# Main logic that calls the functions for this program.
def main():
    # Call create_stopwords_list() which will return a list of stopwords
    stopwords_list = create_stopwords_list()

    # Call calculate_word_frequencies(stopwords_list) which will return a dictionary of word_frequencies (key=word, value=frequency)
    word_frequencies = calculate_word_frequencies(stopwords_list)

    # Display the results as shown in the assignment description
    display_results(word_frequencies)


# Open and read the stopwords.txt file.
# Each line in the file contains a stopword to be added to the stopwords list.
# Open the file with the encoding argument, like this: open(filename, 'r', encoding='utf8')
def create_stopwords_list():
    filename = 'stopwords.txt'
    try:
        stopwords_file = open(filename, 'r', encoding='utf8')
        stopwords_list = []
        for stopword in stopwords_file:
            stopwords_list.append(stopword.strip())
        stopwords_file.close()
        return stopwords_list
    except FileNotFoundError as err:
        print('Error: cannot find file,', filename)
        print('Error:', err)
    except OSError as err:
        print('Error: cannot access file,', filename)
        print('Error:', err)
    except ValueError as err:
        print('Error: invalid data found in file', filename)
        print('Error:', err)
    except Exception as err:
        print('An unknown error occurred')
        print('Error:', err)


# This function creates a word_frequencies dictionary where
#   key = word from the file
#   value = frequency, i.e., the number of times the word appears in the file
# Open and read the treasure-island.txt file
# Call tokenize_text(line_of_text) for each line in the file to obtain a list of the tokenized words in the line.
# For each word, either increment its frequency in the dictionary, or increment the stopword counter if the word is in the stopwords list.
# After reading the file, display the total number of words, and total number of stopwords.
def calculate_word_frequencies(stopwords):
    filename = 'treasure-island.txt'
    stopword_count = 0
    word_count = 0
    word_frequencies = {}
    try:
        text_file = open(filename, 'r', encoding='utf8')
        for line in text_file:
            list_of_words = tokenize_text(line)
            for word in list_of_words:
                word_count += 1
                if word in stopwords:
                    stopword_count += 1
                elif word in word_frequencies:
                    word_frequencies[word] += 1
                else:
                    word_frequencies[word] = 1
        print('Total word count:', word_count)
        print('Total stopword count:', stopword_count)
        return word_frequencies
    except FileNotFoundError as err:
        print('Error: cannot find file,', filename)
        print('Error:', err)
    except OSError as err:
        print('Error: cannot access file,', filename)
        print('Error:', err)
    except ValueError as err:
        print('Error: invalid data found in file', filename)
        print('Error:', err)
    except Exception as err:
        print('An unknown error occurred')
        print('Error:', err)


# Creates a list of words found in line_of_text using the split function.
# Removes leading/trailing punctuation from each word in the list.
# Converts each word to lower case, and returns the list of normalized words.
# This function returns a list of tokenized (and lower case) words obtained from a single line of text.
def tokenize_text(line_of_text):
    list_of_words = line_of_text.split()
    tokenized_words = []
    for word in list_of_words:
        tokenized_words.append(word.strip(string.punctuation).lower())
    return tokenized_words


# Sorts the dictionary of word_frequencies in descending order and displays those that have frequencies >= 70.
def display_results(word_frequencies):
    # print(word_frequencies)
    if word_frequencies:
        sorted_by_frequency = ((k, word_frequencies[k]) for k in sorted(word_frequencies, key=word_frequencies.get, reverse=True))
        print("\nWords with frequencies >= 70")
        print(format('WORD', '<15'), format('FREQUENCY', '>12'))
        for k, v in sorted_by_frequency:
            if v >= 70:
                print(format(k, '<12'), format(v, '>10'))
    else:
        print('No word frequencies found')


main()
