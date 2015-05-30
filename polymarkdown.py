#! /Users/derek/anaconda/bin/python
""""
Polymarkdown
A script to invoke alternate markdown processors based on document header metadata.

[Derek Merck](derek_merck@brown.edu)
Spring 2015

<https://github.com/derekmerck/polymarkdown>

Dependencies: pyYAML

See README.md for usage, notes, and license info.

"""

import sys
from subprocess import Popen, PIPE
import yaml

__description__ = "A script to invoke alternate markdown processors based on document header metadata."
__url__ = "https://github.com/derekmerck/polymarkdown"
__author__ = 'Derek Merck'
__email__ = "derek_merck@brown.edu"
__license__ = "MIT"
__version_info__ = ('0', '2', '0')
__version__ = '.'.join(__version_info__)

processor = []  # Path arguments pairs

# Get stdin
input = sys.stdin.read()
# input = ''
# for line in sys.stdin:
#     input = input + line + '\n'

# Requires an initial demarcation
header = input.split('---')[1]
meta = yaml.load(header)
# for k,v in meta.items():
#     print k, "->", v, "  \n"

# Abort if the 'Custom Processor' tag isn't set
if not meta.get('Custom Processor', False):
    exit(0)

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

    # print [proc['path']]+proc['arguments'].split()
    # print input

    p = Popen([proc['path']]+proc['arguments'].split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    outs = p.communicate(input=input)[0]  # Push input to stdin, the [0] throws out the stderr
    print outs
