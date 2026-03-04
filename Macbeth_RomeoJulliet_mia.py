'''
*/
mia_delacruz 
Function: for each function user gets to see the frequency of words in the play macbeth besides fill in words listed belwo 
bugs: were a lot of syntax and indentation that at first would not run my code 
Log 1.0 M
'''
import string
import csv

def count_words(fname):
    '''
    Args:
        vairable(type): Description of variable. list fill in words that could appear in Macbeth that are not necessary 
    Returns:
        variable(type): displays words in frequency order 
    Raises:
        Error: none 
    Description: opens file and cleans up junk words, then sorts the words into dictionary and writes the dictionary to csv then plots the words by frequency

    '''
    try:
        print(fname)

        fill_in_words = ["and", "or", "i", "the", "a", "an", "but", "however", "thou", "tis", "thee","of","yet","did", "shall", "in", "you", "my", "is", "to", "it"]
        words = dict()

        for line in fname:
            line = line.translate(str.maketrans("", "", string.punctuation))
            line = line.lower()
            line = line.split()

            for word in line:
                if word not in fill_in_words:
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
            
        sorted_words = dict(sorted(words.items(), key=lambda x: x[1], reverse = True))
        counts = dict()

        for word, count in sorted_words.items(): 
                if count > 30:
                    print(f"{word}: {count}")
                    counts[word] = count
        return counts
    except FileNotFoundError:
        print(f"Error: The file {fname} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def export_words(counts, output):
    '''
    '''
    fieldnames = ['Word', 'Count']

    with open(output, 'w', newline = '') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for word, count in counts.items():
            writer.writerow({'Word': word, 'Count': count})
        
    print(f'Data exported to {output}')

def main():
    fname1 = open('Macbeth.txt', 'r')
    fname2 = open('Romeo and Juliet.txt', 'r')

    counts1 = count_words(fname1)
    export_words(counts1, 'Macbeth.csv')

    counts2 = count_words(fname2)
    export_words(counts2, 'Romeo and Juliet.csv')
main()