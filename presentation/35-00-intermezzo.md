# Environments 


## TL;DR

- Search paths and environments are key concepts to create **portable**, **reproducible** code, by **isolating** each project from others.
- Methods exist in all (statistical) programming languages
- For more details, see [other guidance](https://larsvilhuber.github.io/self-checking-reproducibility/10-creating-environments.html)


## What software supports environments?

- R: `renv` package
- Python: `venv` or `virtualenv` module
- Julia: `Pkg` module


## Understanding search paths

Generically, all "environments" simply modify where the specific **software searches** (the "search path") for its components, and in particular any supplementary components (packages, libraries, etc.).[^searchpaths]
 
[^searchpaths]: Formally, this is true for operating systems as well, and in some cases, the operating system and the programming language interact (for instance, in Python).

