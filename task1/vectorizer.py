import re

def vectorize(text):
    ukr_to_lat_voc = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'iu', 'я': 'ia', 'зг': 'zgh'}
    lat_to_numbers_voc = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    sentences = re.split(r'[.!?]', text)

    result = []

    for sentence in sentences:
        parsed_sentence = []
        for word in sentence.split():
            converted_word = ''
            for character in word:
                if character.lower() in ukr_to_lat_voc:
                    converted_word += ukr_to_lat_voc[character.lower()]
            if len(converted_word) > 0:
                vectorized_word = ''
                for character in converted_word:
                    vectorized_word += str(lat_to_numbers_voc[character])
                parsed_sentence.append(sum(int(x) for x in vectorized_word))
        if len(parsed_sentence) > 0:
            result.append(parsed_sentence)

    for line in result:
        print(' '.join(str(x) for x in line))

with open('PythonInternshipTEXT.txt', 'r') as file:
    text = file.read().replace('\n', '')

vectorize(text)