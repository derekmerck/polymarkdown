#! /usr/bin/python
""""
Polymarkdown
A script to invoke alternate markdown processors based on document header metadata.

[Derek Merck](derek_merck@brown.edu)
Spring 2015

<https://github.com/derekmerck/polymarkdown>

Dependencies: pyYAML

See README.md for usage, notes, and license info.

"""

__package__ = "GID_Mint"
__description__ = "A script to invoke alternate markdown processors based on document header metadata."
__url__ = "https://github.com/derekmerck/polymarkdown"
__author__ = 'Derek Merck'
__email__ = "derek_merck@brown.edu"
__license__ = "MIT"
__version_info__ = ('0', '2', '0')
__version__ = '.'.join(__version_info__)

import sys
from subprocess import Popen, PIPE
import yaml

processor = []  # Path arguments pairs

# Get stdin
input = sys.stdin.read()
# input = ''
# for line in sys.stdin:
#     input = input + line + '\n'

header = input.split('---')[0]
meta = yaml.load(header)
# for k,v in meta.items():
#     print k, "->", v, "  \n"

p = meta.get('processor', None)
if p is not None and p is not list:
    path = p.get('path', None)
    arguments = p.get('arguments', None)
    processor.append( {'path': path, 'arguments': arguments})
elif p is not None and p is list:
    for pp in p:
        path = pp.get('path', None)
        arguments = pp.get('arguments', None)
        processor.append({'path': path, 'arguments': arguments})

for proc in processor:
    p = Popen([proc.path]+proc.arguments.split(), stdin=PIPE)
    p.communicate(input=input)[0]  # Push input to stdin

