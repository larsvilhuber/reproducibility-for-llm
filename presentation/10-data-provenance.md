# Let's talk about data

## Types of Data

- Data used for training
- Data used for analysis
- Data output by the algorithm

## Questions for Data  {auto-animate=true transition=fade .smaller}

::: incremental

- Where did the (training/analysis) data come from? 
  - Can you share it? 
  - Can others obtain access? 
  - Is it still there? 
- Where did you put the analysis data?
  - Can you share it?
  - If not, why not? 
  - Can you preserve it?

:::

## Guidance in README

[![](images/readme-dcas.png)](https://social-science-data-editors.github.io/template_README/template-README.html#data-availability-and-provenance-statements)


## Data Provenance

> Are **models** data or software?
>  - will treat as **software** here.

## Data Provenance

- Are the source data **preserved**?
  - Often large **text** archives
  - Format relevant: physical or electronic copy?

## Good example  {auto-animate=true .smaller}

"Immigration Restrictions as Active Labor Market Policy: Evidence from the Mexican Bracero Exclusion, Replication files and raw data" (Michael Clemens)

- Hosted on **Harvard Dataverse** at <https://dataverse.harvard.edu/dataverse/bracero>
- Contains two datasets:
    - Clemens, Michael, 2017, “**Raw scanned PDFs of primary sources for workers, wages, and crops**”, <https://doi.org/10.7910/DVN/DJHVHB>, Harvard Dataverse, V1


## Your analysis data

Probably requires

- substantial computing resources (time, cost, space)
- lesser storage resources 

## Good example  {auto-animate=true .smaller}

> "Immigration Restrictions as Active Labor Market Policy: Evidence from the Mexican Bracero Exclusion, Replication files and raw data" (Michael Clemens)

- Hosted on **Harvard Dataverse** at <https://dataverse.harvard.edu/dataverse/bracero>
- Contains two datasets:
    - Clemens, Michael, 2018, “Replication Data for: Immigration Restrictions as Active Labor Market Policy: Evidence from the Mexican Bracero Exclusion”, <https://doi.org/10.7910/DVN/17M4ZP>, Harvard Dataverse, V1

## LLM-specific considerations

Generically,

`pre-trained LLM` ▶️ `tuned LLM` ▶️ `analysis data`

## LLM-specific considerations

- `tuned LLM` = f(`raw data`,`pre-trained LLM`)
- `analysis data` = f(`tuned LLM`,`raw data`)

**Both should be preserved**

## LLM-specific considerations

- size?
- where?

## LLM-specific considerations

`tuned LLM`:

- can you release it? (privacy)
- does **Hugging Face** have a preservation policy? (*no*)
- license to apply to it?

## LLM-specific considerations

`analysis data`:

- can be preserved as part of the replication package
- could be preserved elsewhere, if multi-purpose