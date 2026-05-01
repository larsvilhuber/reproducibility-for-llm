
```{r generate_qr, include=FALSE}
library(qrcode)
code <- qr_code(WEBSITE_URL)
png(filename = "images/qr.png")
plot(code)
invisible(dev.off())
```

:::: {.columns}

::: {.column width="50%"}

![](./images/screenshot-2026-05-01.png)

[`r WEBSITE_SHORT`](`r WEBSITE_URL`) 


:::

::: {.column width="50%"}

![](images/qr.png){width="350" height="350"}

:::


::::

:::: {.columns}

::: {.column width="90%"}

:::

::: {.column width="10%"}

```{r print_pdf, echo=FALSE, results='asis'}
# If PDF_URL is defined, print the link to the PDF
if (exists("PDF_URL") && !is.null(PDF_URL)) {
  cat(paste0("[![](images/pdf-round.png){width=50px}](", PDF_URL, ")"))
}
```
:::
::::
