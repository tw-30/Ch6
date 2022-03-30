#original 
#from collections import Counter
#text = ('to be or not to be that is the question')
#counter = Counter(text.split())
#for word, count in sorted(counter):
#    print(f'{word:<12}{count}')

#edit 
'''The original didnt have counter.items() in the sorted assignment, which gave the value error because there were 
too many variables to unpack'''

from collections import Counter
text = ('to be or not to be that is the question')
counter = Counter(text.split())
for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')