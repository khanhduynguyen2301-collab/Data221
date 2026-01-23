def nested_dictionary(string):
    dictionary = {}
    for item in string.split():
        dictionary[item] = {'length': len(item),
                            'parity': 'even' if len(item) % 2 == 0 else 'odd'}
    return dictionary

string = 'data science'
print(nested_dictionary(string))