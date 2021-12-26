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


def get_posts_by_tag(data, tag):
    results = []

    for record in data:
        if f'#{tag}' in record['content']:
            results.append(record)
    return results


def save_post(filename, post):
    data = read_post(filename)
    data.append(post)
    with open(filename, 'w', encoding='utf=8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
