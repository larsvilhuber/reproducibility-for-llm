# Conclusion

## AI and LLMs are not special

... when it comes to reproducibility

## But difficulties are magnified

... compared to the **average** difficulty in economics papers

## Solutions

- Be **reproducible** from the start
  - Use **environments**
  - Use **logging** as evidence, especially when **repetitions** are expensive

## Solutions

- **Computational empathy**
  - Remember your own difficulties in getting this to work
  - Now put yourself in others' computer (shoes)
  - Be very clear about what is needed - you are **cutting edge**, others may not be!

## Solutions

- Be **precise** about **versions**
  - of input data (including RAG/training/fine-tuning)
  - of software used (Python, libraries, but also *models* - do not use "latest"!)

## Solutions

- Include **all code**
  - that includes *prompts*, intermediate *responses*
  - even if data are not included

## Solutions

- Include all **metadata**
  - fix random seeds, where possible
  - **hyperparameters**, *temperature*, or whatever it is called
  - *prompts* could be considered **metadata**

## Solutions

- Include **data** where possible
  - licenses
  - size
  - intermediate data where useful/time-consuming (but: license!)

## Solutions

- Consider how and where to **preserve** 
  - industry repositories may be fine for **sharing**
  - academic repositories (**Zenodo**, **Dataverse**) handle **preservation**
  - Toolkit is still in its infancy for the preservation of large data ($>=$ 200GB)


## Solutions

- Use existing **resources**
  - [Template README](https://social-science-data-editors.github.io/template_README/) ([presentation](https://larsvilhuber.github.io/readme-presentation/)) as guidance
  - [Self-check your code](https://larsvilhuber.github.io/self-checking-reproducibility/) ([presentation](https://larsvilhuber.github.io/self-checking-reproducibility/presentation/))
  