# Defines
def single_root_words(root_word, *other_words):
    same_words = list()
    for word in other_words:
        if root_word.lower() in word.lower():
            same_words.append(word)
    return {'root_word': root_word, 'same_words': same_words}

# Code
craft1_decks = single_root_words('Von Braun', ' Von Braun MedSci Deck', 'UNN Rickenbaker Deck A', 'Von Braun Engineering Deck', 'UNN Rickenbaker Deck B')
craft2_decks = single_root_words('UNN Rickenbaker', ' Von Braun MedSci Deck', 'UNN Rickenbaker Deck A', 'Von Braun Engineering Deck', 'UNN Rickenbaker Deck B')

print(f'System Shock2 craft: {craft1_decks['root_word']}, list decks: {craft1_decks['same_words']}')
print(f'System Shock2 craft: {craft2_decks['root_word']}, list decks: {craft2_decks['same_words']}')