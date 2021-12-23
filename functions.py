import json


def read_post(filename):
    with open(filename, encoding='utf=8') as f:
        return json.load(f)


def get_tags(data):
    results = set()

    for records in data:
        content = records['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                results.add(word[1:])
    return results
