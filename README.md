Custom Processor: true
processor:
  path: "/usr/bin/pandoc"
  arguments: "-f markdown+pipe_tables+table_captions+yaml_metadata_block+example_lists+implicit_figures -t html5 --filter pandoc-citeproc --bibliography myrefs.bib"
---

# Polymarkdown

[Derek Merck](email:derek_merck@brown.edu)  

<https://github.com/derekmerck/polymarkdown>


## Overview

Script for processing markdown content according to a YAML header in the document.
 
It is intended to be used as a processor for [Marked 2] that enables the user to assign processors such as pandoc, scholdoc, and mmd as a header of the actual document.


## Dependencies

- Python 2.7


## Usage

```markdown
---
Custom Processor: True
processor:
  path: "/usr/bin/pandoc"
  arguments: "-f markdown+pipe_tables+table_captions+yaml_metadata_block+example_lists+implicit_figures -t html5 --filter pandoc-citeproc --bibliography myrefs.bib"
---
Here is a citation[&my_cite2000]
```

In Marked 2, set your custom processor to `polymarkdown.py` or `python -m polymarkdown` depending on how the script is installed.

To generate a word file, just change the `-t` argument to `doc` and redirect the output to a file.

```markdown
  arguments: "-f markdown+pipe_tables+table_captions+yaml_metadata_block+example_lists+implicit_figures -t doc --filter pandoc-citeproc --bibliography myrefs.bib"
```

```bash
$ ./polymarkdown.py < my_text.md >my_text.doc
```

To generate a word doc from [Scrivener], I use Marked 2 as an intermediary and generate both html and doc file output.  You can do this by adding a secondary processor and argument set to the header.  For pandoc, it is straightforward to generate an output file from the command line.

```yaml 
---
Custom Processor=True
processor:
  -path: "/usr/bin/pandoc"
   arguments="-f markdown+pipe_tables+table_captions+yaml_metadata_block+example_lists+implicit_figures -t html5 --filter pandoc-citeproc --bibliography myrefs.bib"
  -path: "/usr/bin/pandoc"
   arguments2="-f markdown+pipe_tables+table_captions+yaml_metadata_block+example_lists+implicit_figures -t doc --filter pandoc-citeproc --bibliography myrefs.bib my_file.doc"
---
Here is a citation[&my_cite2000]
```


### Future Work

Add [Madoku] support


[scrivener]:
[marked2]:
[madoku]:
[pandoc]:
[scholdoc]: