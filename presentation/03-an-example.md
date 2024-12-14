# An example

## Korinek (2023)



## Existing Replication Package

- Article [@korinekGenerativeAIEconomic2023] (also NBER WP [@korinekGenerativeAIEconomic2024])
- Package at [@korinekDataCodeGenerative2023]
- Additional materials at <https://www.genaiforecon.org/index.html>
- I vetted this package!

## Created in 2023

- Python based
- README states

```
Ensure you have the necessary Python libraries installed:

  pip install openai pandas numpy
​

To execute the simplest example, run the script:

 python simple_example_chat1.py
​
​
The results will be displayed on the screen.
```

## Ex-post critique

- Missing a `requirements.txt`
- No instructions to set an environment

> These are now systematically requested for replication packages!

## Trying it out

I created a `requirements.txt` file

```bash
numpy==2.2.0
openai==1.57.4
pandas==2.2.3
openpyxl
```

*(note: created using [`pipreqs`](https://pypi.org/project/pipreqs/) Python package, plus hand-edit).*

## Trying it out (2)

Create environment

```bash
python3.11 -m venv venv-311
source venv-311/bin/activate
pip install -r requirements.txt
```

*(note: running on Linux, openSUSE, Python 3.11.10)*

## Trying it out (3)

Get the API key

- Go to <https://platform.OpenAI.com>
- Go to `API keys` on the left side
- Verify phone number (a challenge while roaming!)
- `+ Create new secret key`
- Save the API key in file `.env`

## Trying it out (4)

Run the script

```bash
python simple_example_chat1.py 
```

## Failure!

```bash
> python simple_example_chat1.py 
Please enter your OpenAI API key: 
  File "/path/korinek-2023/simple_example_chat1.py", line 24, in <module>
    openai.api_key = input("Please enter your OpenAI API key: ")
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

```

## Attempt to fix

- README speaks of environment variable

```bash
export OPENAI_API_KEY=sk-proj-lxxxxxxxxxx
```

- Run again, same error!

## Reasons

- Not scripted enough, requires manual intervention!
- Ignores `.env` file (one way of doing it)
- Ignores environment variable (another way), despite doing it in another script!

## Quick fix

- I fixed the script to read from environment variable.

```python
openai.api_key = os.environ.get('OPENAI_API_KEY')

# If the API key isn't found in the environment variable, prompt the user for it
if not openai.api_key:
    openai.api_key = input("Please enter your OpenAI API key: ")
```

> NEVER RECORD YOUR API KEY IN SCRIPTS!

## IMPORTANT

- These are **standard Python** issues, *not AI issues*!
- But they are crucial for reproducibility!

## Result {.smaller}

```{.bash code-line-numbers="9,13" fold=true}
Traceback (most recent call last):
  File "/path/korinek-2023/simple_example_chat1.py", line 37, in <module>
    completion = openai.ChatCompletion.create(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/path/korinek-2023/venv-311/lib64/python3.11/site-packages/openai/lib/_old_api.py", line 39, in __call__
    raise APIRemovedInV1(symbol=self._symbol)
openai.lib._old_api.APIRemovedInV1: 

You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.

You can run `openai migrate` to automatically upgrade your codebase to use the 1.0.0 interface. 

Alternatively, you can pin your installation to the old version, e.g. `pip install openai==0.28`

A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742
```

## THIS IS A STANDARD PYTHON - API ISSUE! {.smaller}

- These are **standard API** issues, *not AI issues*!
- APIs change
- Libraries change
- Having **latest** is not always best. 
- But they are crucial for reproducibility!

> Provide `requirements.txt` and pin versions!

*(We will talk later about API issues!)*

## Next attempt {.smaller}

- Fix `requirements.txt`, re-install

```{.bash code-line-numbers="9" fold=true}
> python simple_example_chat1.py 
Traceback (most recent call last):
  File "/path/korinek-2023/simple_example_chat1.py", line 37, in <module>
    completion = openai.ChatCompletion.create(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
<snip>
  File "/path/korinek-2023/venv-311/lib64/python3.11/site-packages/openai/api_requestor.py", line 765, in _interpret_response_line
    raise self.handle_error_response(
openai.error.InvalidRequestError: The model `gpt-4-0613` does not exist or you do not have access to it.
```

## Fixing this {.smaller}

![CoPilot response](images/copilot-screenshot-20241214.png)

*(note: `github.copilot-chat` 0.23.1, updated 2024-12-14, 15:31:36)*

## Turns out...

- I thought I had credits, I did not.
- It was the `you do not have access to it` part that was crucial!

## Results {.smaller}

:::: {.columns}

::: {.column width=50%}

Original content

```{r}

# Call the function with the original file
mylines("korinek-2023/simple-example-orig.txt")
```

:::

::: {.column width=50%}

Content as of 2024-12-14:

```{r}
# Call the function with the updated file
mylines("korinek-2023/simple-example-20241214.txt")
```

:::

::::

