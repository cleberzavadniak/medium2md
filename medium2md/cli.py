import sys

from . import Importer


def run():
    url = sys.argv[1]
    importer = Importer(url)
    importer.run()
    print(importer.text)
