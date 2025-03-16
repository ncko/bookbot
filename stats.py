def get_num_words(text):
    lines = text.splitlines()
    count = 0
    for line in lines:
        tokens = line.split(' ')
        filtered_tokens = [token for token in tokens if token]
        count = count + len(filtered_tokens)

    return count


def get_char_counts(text):
    counts = {}
    for char in text:
        lower_char = char.lower()
        counts[lower_char] = counts.get(lower_char, 0) + 1

    return counts


def flatten_and_sort_dict(dictionary):
    keys = dictionary.keys()
    list_of_dicts = []
    for key in keys:
        count = dictionary.get(key)
        list_of_dicts.append({
            'char': key,
            'count': count
        })

    list_of_dicts.sort(key=lambda x: x.get('count'), reverse=True)
    return list_of_dicts


