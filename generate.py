import os
import json
from jinja2 import Environment, FileSystemLoader

j2env = Environment(loader=FileSystemLoader("./_templates"))


def main() -> None:
    bible = {}
    with open('_data/bible.json', 'r') as fd:
        bible = json.loads(fd.read())

    try:
        os.mkdir('docs')
    except:
        pass

    with open('docs/index.html', 'w') as fd:
        fd.write(j2env.get_template("index.html").render(books=bible.keys()))

    for book, data in bible.items():
        with open('docs/{}.html'.format(book.lower()), 'w') as fd:
            fd.write(j2env.get_template("book.html").render(book=book, data=data))


if __name__ == "__main__":
    main()
