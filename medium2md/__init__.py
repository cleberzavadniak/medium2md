from bs4 import BeautifulSoup
import newspaper


class Importer:
    replacers = {
        'h1': '# {line}',
        'h2': '# {line}',
        'h3': '## {line}',
        'h4': '### {line}',
        'h5': '#### {line}',
        'strong': '#### {line}',
        'blockquote': '    {line}',
    }

    def __init__(self, url):
        self.url = url
        self.buffer = []
        self.title = None
        self.subtitle = None

    @property
    def text(self):
        return '\n'.join(self.buffer)

    def run(self):
        article = newspaper.Article(self.url)
        article.build()
        self.title = article.title

        soup = BeautifulSoup(article.html)

        for line in article.text.split('\n'):
            if len(line) < 1024:
                for tag in soup.find_all():
                    text = tag.text.replace(' ', ' ')
                    if text == line:
                        replacer = self.replacers.get(tag.name, None)
                        if replacer:
                            line = replacer.format(line=line)
                        break

            self.buffer.append(line)

        try:
            title = self.buffer[0]
            subtitle = self.buffer[2]
        except IndexError:
            return

        if len(title) > 128:
            return

        self.title = title.replace('# ', '')
        self.buffer = self.buffer[1:]

        if len(subtitle) > 128:
            return

        self.subtitle = subtitle
        self.buffer = self.buffer[2:]
