# Hands-off running: Creating a controller script

- Your code must run, **beginning to end**, top to bottom, without error, and **without any user intervention**. 

- This should in principle (re)create all **figures**, **tables**, and **in-text numbers** you include in your paper. 


::: {.notes}
We have seen users who appear to highlight code and to run it interactively, in pieces, using the program file as a kind of notepad. This is not reproducible, and should be avoided. It is fine for debugging.
:::

## Seem trivial?

> Out of **8280** replication packages in ~20 top econ journals, only  **2594** (**31.33%**) had a main/controller script.[^resultsmain]

[^resultsmain]: Results computed on Nov 26, 2023 based on a scan of replication packages conducted by Sebastian Kranz. 2023. "Economic Articles with Data". https://ejd.econ.mathematik.uni-ulm.de/, searching for the words `main`, `master`, `makefile`, `dockerfile`, `apptainer`, `singularity` in any of the program files in those replication packages. Code not yet integrated into this presentation.

## TL;DR

- Create a "main" file that runs all the other files in the correct order.
- Run this file, without user intervention.
- It should run without error.

## Creating a main or master script

In order to be able to enable "hands-off running", the **main (controller) script is key**. 

## Example 1: Querying Claude.ai

- for the first example, I was **lazy** - I typed the prompt into the Claude.ai website.
- Can you repeat it?
- What if I have to repeat it 100 times, with slight variations?



## R {auto-animate=true}


:::: {.columns}

::: {.column width=40%}

Set the root directory (using `here()` or `rprojroot()`).

:::

::: {.column width=60%}

```{.r code-line-numbers="3-4"}
# main.R
## Set the root directory
# If you are using Rproj files or git
rootdir <- here::here()
# or if not
# rootdir <- getwd()
## Run the data preparation file
source(file.path(rootdir, "01_data_prep.R"), 
       echo = TRUE)
## Run the analysis file
source(file.path(rootdir, "02_analysis.R"), 
       echo = TRUE)
## Run the table file
source(file.path(rootdir, "03_tables.R"), echo = TRUE)
## Run the figure file
source(file.path(rootdir, "04_figures.R"), echo = TRUE)
## Run the appendix file
source(file.path(rootdir, "05_appendix.R"), echo = TRUE)
```

:::
::::


## R {auto-animate=true}


:::: {.columns}

::: {.column width=40%}

Call each of the component programs, using `source()`.

:::

::: {.column width=60%}


```{.r code-line-numbers="8-9|11-12|14|16|18"}
# main.R
## Set the root directory
# If you are using Rproj files or git
rootdir <- here::here()
# or if not
# rootdir <- getwd()
## Run the data preparation file
source(file.path(rootdir, "01_data_prep.R"), 
       echo = TRUE)
## Run the analysis file
source(file.path(rootdir, "02_analysis.R"), 
       echo = TRUE)
## Run the table file
source(file.path(rootdir, "03_tables.R"), echo = TRUE)
## Run the figure file
source(file.path(rootdir, "04_figures.R"), echo = TRUE)
## Run the appendix file
source(file.path(rootdir, "05_appendix.R"), echo = TRUE)
```

:::
::::

## Notes for R {auto-animate=true}

The use of `echo=TRUE` is best, as it will show the code that is being run, and is thus more transparent to you and the future replicator.

## Notes for Python {auto-animate=true}

- There are many ways to do this in Python (as there are more in R)
- Defining **functions** separately, and then calling them in the **main** file.
- Constructing a **package** and calling that package.

## Notes for Python {auto-animate=true}

If using **procedural** Python code, might use a `bash` script:

```bash
# This is main.sh
python 01_data_prep.py
python 02_analysis.py
python 03_tables.py
python 04_figures.py
```

## Caution

What you do should remain **transparent** to other users!

## Caution

Writing a scientific paper is different than writing a useful function on the internet.

> You are not writing `mynumpy`, you are writing a paper.

*... though there are grey areas there.*


## Takeaways {.smaller}


- [x]  your code runs without problem, after all the debugging.
- [x] your code runs without manual intervention, and with low effort
- [ ] it actually produces all the outputs
- [ ] your code generates a log file that you can inspect, and that you could share with others.
- [ ] it will run on somebody else's computer


