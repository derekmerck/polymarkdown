---
Custom Processor: True
processor:
  path: "/usr/local/bin/pandoc"
  arguments: "-f markdown+pipe_tables+table_captions+yaml_metadata_block+example_lists+implicit_figures -t html5 --bibliography /Users/derek/dev/polymarkdown/ref.bib"
---

# Polymarkdown

[Derek Merck](email:derek_merck@brown.edu)  

<https://github.com/derekmerck/polymarkdown>


## Overview

Script for processing markdown content according to a YAML header in the document.
 
It is intended to be used as a processor for [Marked 2] that enables the user to assign processors such as [pandoc] and [scholdoc] in the header of the actual document.


## Dependencies

- Python 2.7
- pyyaml
- pandoc, scholdoc, or other markdown processor


## Usage

```yaml
---
Custom Processor: True
processor:
  path: "/usr/bin/pandoc"
  arguments: "-f markdown+pipe_tables+table_captions+yaml_metadata_block+example_lists+implicit_figures -t html5 --filter pandoc-citeproc --bibliography full_path/ref.bib"
---
Here is a citation [@polymd2015]
```

In Marked 2, set your custom processor to `polymarkdown.py` or `python -m polymarkdown` depending on how the script is installed.

If all works as planned, you can view this readme and this will appear as a proper citation: [@polymd2015] and the bibliogrpahic reference will be appended at the end of the page.

To generate a word doc from [Scrivener], I use Marked 2 as an intermediary and generate both html and doc file output.  This can be accomplished by adding a secondary processor and argument set to the header.

```yaml 
---
Custom Processor=True
processor:
  -path: "/usr/local/bin/pandoc"
   arguments="-f markdown+pipe_tables+table_captions+yaml_metadata_block+example_lists+implicit_figures -t html5 --filter pandoc-citeproc --bibliography ref.bib"
  -path: "/usr/local/bin/pandoc"
   arguments2="-f markdown+pipe_tables+table_captions+yaml_metadata_block+example_lists+implicit_figures -t doc --filter pandoc-citeproc --bibliography ref.bib my_file.doc"
---
Here is a citation [@polymd2015]
```


### Future Work

- Add [Multimarkdown] support; should be straightfoward. 
- Add [Madoku] support.  This is non-trivial b/c of all the required output and input files.


[scrivener]: https://www.literatureandlatte.com/scrivener.php
[marked 2]: http://marked2app.com
[madoku]: https://www.madoko.net
[pandoc]: http://pandoc.org
[scholdoc]: http://scholdoc.scholarlymarkdown.com
[multimarkdown]: http://fletcherpenney.net/multimarkdown/
