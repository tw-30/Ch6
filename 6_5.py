text = ('this is sample text with several words'
        'this is more sample text with other several words too')

word_counts = {}

for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')
    
print('\nNumber of unique words: ', len(word_counts))
print("duplicate words are: ")
counter = 1
for word, count in word_counts.items():
    
    if word_counts[word] > 1:
        
        print(f'{word:<20}{counter:<12}')
        counter += 1

    
        
        
