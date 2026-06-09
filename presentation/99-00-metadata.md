# Useful links

```{r}
#| label: metadata
#| echo: false
#| results: hide


# Load the _quarto.yml file
config <- yaml::read_yaml(here::here("_quarto.yml"))

# Access parameters from the YAML config

# Derive the GitHub repository URL from the GITHUB_REPOSITORY environment
# variable (set automatically by GitHub Actions as "owner/repo"). This keeps
# the link portable across forks/repositories.

GITHUB_REPOSITORY <- Sys.getenv("GITHUB_REPOSITORY")
REPOSITORY_URL <- paste0("https://github.com/", GITHUB_REPOSITORY)

```

- {{< fa brands github size=1x >}} [GitHub](`r REPOSITORY_URL`)
- {{< fa home size=1x >}} [`r config$author$name`](`r config$author$homepage`)
- Presentation QR Code:

```{r}
#| echo: false
#| out.width: "100px"
qr_file <- "images/qr.png"
knitr::include_graphics(qr_file)
```

- Last Run on `r Sys.Date()`

Content is licensed [![License: CC BY-NC 4.0](images/cc-by-nc-80x15.png)](https://creativecommons.org/licenses/by-nc/4.0/).
