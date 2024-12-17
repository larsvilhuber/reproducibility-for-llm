---
jupytext:
  text_representation:
    format_name: myst
    extension: .md
    format_version: '1.3'
    jupytext_version: '1.11.2'
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Metadata

```{code-cell} ipython3
:tags: [remove-input, remove-output]

import yaml
import qrcode
with open("presentation/_quarto.yml", "r") as file:
    config = yaml.safe_load(file)
presentation_url = config['format']['revealjs']['baseurl']
qr_file = "presentation/images/qr.png"
qr_img = qrcode.make(presentation_url)
qr_img.save(qr_file)
```
