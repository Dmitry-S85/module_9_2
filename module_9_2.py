first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

def get_lengths(strings):
    result = []
    for string in strings:
        if len(string) >= 5:
            result.append(len(string))
    return result

first_result = get_lengths(first_strings)

def create_pairs(strings1, strings2):
    pairs = []
    for word1 in first_strings:
        for word2 in second_strings:
            if len(word1) == len(word2):
                pairs.append((word1, word2))
    return pairs

second_result = create_pairs(first_strings, second_strings)

def build_dict(strings1, strings2):
    results = {}
    for string1 in (first_strings + second_strings):
        if not len(string1) % 2:
            results[string1] = len(string1)
    return results

third_result = build_dict(first_strings, second_strings)


print(first_result)
print(second_result)
print(third_result)