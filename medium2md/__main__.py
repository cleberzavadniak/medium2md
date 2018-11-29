import sys

from . import Importer


url = sys.argv[1]
importer = Importer(url)
importer.run()
print(importer.text)
