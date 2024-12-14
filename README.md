# Reproducibility and LLM

How to think about reproducibility in an AI world.

## Author

Lars Vilhuber

## All versions (archived)


## Building

This repository contains two parts: a web page, built on Jupyter Book, and a presentation, built on Quarto with reveal.js. They are both built by the GH CI system, but can be built individually.

### Web page

Can be built with Python 3.10. To run locally, run `_setup.sh`  locally, then use the `run_jupyter_book.sh` script, which in turn relies on Docker and `_test.sh` to build the book. Standard Jupyter Book practices apply: see `_toc.yml` for the table of contents, and `_config.yml` for the configuration.

## License


Content is [![License: CC BY-NC 4.0](/images/cc-by-nc-80x15.png)](https://creativecommons.org/licenses/by-nc/4.0/).

