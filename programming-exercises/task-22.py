# Należy wykorzystać plik wordlist_10000.txt i stworzyć funkcję wyszukującą najdłuższy wyraz w tym pliku oraz drugą funkcję, która wyszuka wyrazy o długości 10.

def find_longest_word(file_path):
    longest_word = ""
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            if len(word) > len(longest_word):
                longest_word = word
    return longest_word


def find_words_of_length(file_path, length):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            if len(word) == length:
                words.append(word)
    return words


if __name__ == "__main__":
    file_path = 'wordlist_10000.txt'
    
    longest_word = find_longest_word(file_path)
    print(f"The longest word is: {longest_word}")
    
    ten_length_words = find_words_of_length(file_path, 10)
    print(f"Words of length 10: {ten_length_words}")