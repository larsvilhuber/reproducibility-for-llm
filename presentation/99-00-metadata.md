# Useful links

```{r}
#| label: setup
#| echo: false
#| results: hide


# Load the _quarto.yml file
config <- yaml::read_yaml(here::here("_quarto.yml"))

# Access parameters from the YAML config

```

- {{< fa brands github size=1x >}} [GitHub](`r config$github$url`)
- {{< fa home size=1x >}} [`r config$author$name`](`r config$author$homepage`)
- Presentation QR Code:

```{r}
#| echo: false
#| out.width: "100px"
qr_file <- "images/.png"
knitr::include_graphics(qr_file)
```

- Last Run on `r Sys.Date()`

Content is licensed [![License: CC BY-NC 4.0](images/cc-by-nc-80x15.png)](https://creativecommons.org/licenses/by-nc/4.0/).
