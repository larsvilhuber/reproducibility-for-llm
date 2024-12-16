# Creating log files

In order to document that you have actually run your code, a **log file**, a transcript, or some other evidence, may be useful. It may even be required by certain journals.

## TL;DR

- **Log files** are a way to document that you have run your code.
- In particular for code that runs for a very long time, or that uses data that cannot be shared, log files may be the only way to document basic reproducibility.

## Overview

::: {.incremental}

- Most statistical software has ways to keep a record that it has run, with the details of that run.
- Some make it easier than others. 
- You may need to instruct your code to be "verbose", or to "log" certain events. 
- You may need to use a command-line option to the software to create a log file.

:::

:::{.notes}
I do note that we are typically only looking to document what the statistical code does, at a high level. We are not looking to document system calls, fine-grained data access, etc. Computer scientists and IT security mavens may be interested in such details, but economists are typically not.
:::

---

In almost all cased, the generated log files are simple text files, without any formatting, and can be read by any text editor (e.g., Visual Studio Code, Notepad++, etc.). 

If not, ensure that they are (avoid *Stata SMCL* files, for example, or *iPython* output).

## Creating log files explicitly

Generically: see [*separate* tutorial](https://larsvilhuber.github.io/self-checking-reproducibility/presentation/#/creating-log-files).

## Python {auto-animate=true}

:::: {.columns}

::: {.column width=30%}

Create a wrapper that will capture the calls for any function

:::

::: {.column width=70%}


```{.python code-line-numbers="2-9"}
from datetime import datetime
def track_calls(func):
    def wrapper(*args, **kwargs):
        with open('function_log.txt', 'a') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[{timestamp}] Calling {func.__name__} with args: {args}, kwargs: {kwargs}\n")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Usage
@track_calls
def my_function(x, y,default="TRUE"):
    return x + y

my_function(1, 2,default="false")
```

:::
::::


## Python {auto-animate=true}

:::: {.columns}

::: {.column width=30%}

Activate the wrapper

:::

::: {.column width=70%}

```{.python code-line-numbers="12"}
from datetime import datetime
def track_calls(func):
    def wrapper(*args, **kwargs):
        with open('function_log.txt', 'a') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[{timestamp}] Calling {func.__name__} with args: {args}, kwargs: {kwargs}\n")
        result = func(*args, **kwargs)
        return result
    return wrapper

# Usage
@track_calls
def my_function(x, y,default="TRUE"):
    return x + y

my_function(1, 2,default="false")
```

:::
::::

## Python {auto-animate=true}

:::: {.columns}

::: {.column width=30%}

Ideally, capture the output

:::

::: {.column width=70%}


```{.python code-line-numbers="8"}
# Usage
@track_calls
def my_function(x, y,default="TRUE"):
    return x + y

my_function(1, 2,default="false")
# Output
# [2024-12-15 12:05:37] Calling my_function with args: (1, 2), kwargs: {'default': 'false'}

```

:::
::::



# Creating log files automatically

An alternative (or complement) to creating log files explicitly is to use native functionality of the software to create them. This usually is triggered when using the **command line** to run the software, and thus may be considered an **advanced topic.** The examples below are for Linux/macOS, but similar functionality exists for Windows.

## Python {auto-animate=true transition="fade"}

In order to capture screen output in  Python, on Unix-like system (Linux, macOS), the following can be run:

```bash
python main.py | tee main.log
```

which will create a log file with everything that would normally appear on the console using the `tee` command. 


## Takeaways {.smaller}


- [x]  your code runs without problem, after all the debugging.
- [x] your code runs without manual intervention, and with low effort
- [x] it actually produces all the outputs
- [x] your code generates a log file that you can inspect, and that you could share with others.
- [ ] it will run on somebody else's computer
