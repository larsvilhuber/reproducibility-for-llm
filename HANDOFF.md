# Handoff: HDSR manuscript (`reproducibility-ai-hdsr.md`)

Written 2026-08-03. Purpose: carry the state of an AI-assisted editing session
across machines. Read this before resuming work on the HDSR paper.

## Where things stand

`reproducibility-ai-hdsr.md` has just been **restructured onto the four-claim
framework** in the handwritten outline `Hdsr-llm.pdf` (4 scanned pages, in repo
root). The prose was deliberately *not* rewritten — fragments, notation, and
examples were moved to where the outline puts them, and the gaps the outline
opens were marked with HTML comments rather than filled in. Fleshing out the
language is the author's job.

Renders cleanly: `quarto render reproducibility-ai-hdsr.md --to docx`. All
citations resolve, math emits as native Word equations (OMML), HTML comments
stay out of the output.

## The framework (from `Hdsr-llm.pdf`)

Four claims, each with the same internal pattern:

    Claim -> "Here" (analogy in established practice) -> "There" (LLM case) -> what to do

1. **LLMs are code** — analogies: online systems (geocoding via Maps);
   commercial software (Stata mostly preservable, MATLAB pretty good, SAS not
   possible). *Here:* Stata → containers → Docker Hub. *There:* open-weight
   models on Hugging Face.
2. **LLMs are data (training data)** — most social scientists do not train
   de-novo foundation models. *Here:* Clemens raw scans → transcribed data.
   *There:* Dell's American Stories corpus → foundation model. Plus the privacy
   case: Athey et al. fine-tuned on confidential/proprietary career data;
   counter-model is LEHD and statistical agencies generally.
3. **LLMs are used to generate data** — generated data should be preserved and
   shared. *Here:* geocoded output; data obtained via public APIs and
   commercial APIs (Bureau van Dijk, Refinitiv, Bloomberg Terminal).
4. **LLM-generated data is a random draw** — routinely ignored in social science
   *and* computer science. Existing near-misses: probabilistic record linkage,
   imputation for missing data. **"Here: no good analogy!"** — this is the
   structural asymmetry that carries the paper. Recommendation: draw from
   multiple models, provide all draws, use all draws in analysis → multiple
   imputation inference. Margin note in the outline: *make here the importance
   of the statistical foundations of data science.*

Sections outside the four claims: Introduction, Fundamental Reproducibility
Targets (incl. Notation), Some Guidance (logging / environments / cost / best
practices), Conclusion.

**Unresolved:** the outline annotates several examples with circled ℗ and Ⓛ
markers. Their meaning was never settled — possibly preservable / licensed /
large. A comment in the Notation section flags this.

## Notation

Fixed in `## Notation`, under Fundamental Reproducibility Targets, because every
claim is about a different object in it:

- $\mathcal{M}^0$ pre-trained model, $D^t$ fine-tuning data, $\mathcal{M}^t$ tuned model
- $D^*$ researcher's raw data, $\widetilde{D}$ analysis data the model produces
- $\mathcal{M}^t = f(D^t, \mathcal{M}^0)$, $\widetilde{D} = g(\mathcal{M}^t, D^*)$
- zero-shot: $\mathcal{M}^t = \mathcal{M}^0$

Mapping to the claims: Claim 1 → the models; Claim 2 → $D^t$ and the corpus
behind $\mathcal{M}^0$; Claim 3 → $\widetilde{D}$ and the map $g$; Claim 4 → $g$
is stochastic, $\widetilde{D}$ is one draw.

Multiple-imputation combining rules use **partially** synthetic rules
(@reiter2004): $T_p = b_m/m + \bar{v}_m$. This is the right choice because $D^*$
is real and only the derived variable is model-generated; fully synthetic rules
(@ReiterJ.Stat.Plan.Inference2005) would apply otherwise. Stated explicitly in
the text because a referee will ask.

Notation choices that depart from the slide deck, and why:
- $\mathcal{M}$ for models where slides used backticked words — prose needs a
  symbol, and plain $M$ would collide with MI's $m$.
- $f$ and $g$ for the two steps where slides used $f$ for both — they are
  genuinely different functions.
- Repeated draws are $\widetilde{D}_i$, $i=1,\dots,m$.

**Known inconsistency in the presentation, not yet fixed:**
`presentation/10-data-provenance.md` defines $D^*$ as *raw* data, but
`presentation/31-run_it_again.md` writes the repeated draws as $D^*_m$, reusing
$D^*$ for *generated* data. The paper is internally consistent; the slides
should be updated to match.

## Open TODOs in the manuscript

Ten HTML comments mark work to be done. Grep for `TO BE WRITTEN`, `TO BE FLESHED
OUT`, and `TODO`. In document order:

| Location | What is needed |
|---|---|
| Introduction | Roadmap paragraph exists in draft form; confirm wording. |
| Notation | Decide what ℗/Ⓛ meant; state the claim→notation mapping explicitly. |
| Claim 1, *Here: online systems* | Write the geocoding analogy. Needs a citation for a geocoding-in-economics example. |
| Claim 1, *Here: commercial software* | Write the Stata/MATLAB/SAS preservability spectrum. Verify the version-and-licensing facts behind each ranking. |
| Claim 1, *There* | Make the "Docker Hub : Stata :: Hugging Face : open-weight model" parallel explicit. |
| Claim 2, *Here* | Note that raw-corpus/derived-artifact is the same relation as training-corpus/model. |
| Claim 2, *There* | Flag the recursion: American Stories is itself LLM-generated data (Claim 3) serving as a training corpus (Claim 2). |
| Claim 2, *Privacy* | Flesh out the Athey example (citations now in place, see below). Add LEHD / statistical agencies as the counter-model. |
| Claim 3, *Here* ×2 | Write geocoded-output and API analogies. Commercial API vendors named in the comment. |
| Claim 4, *Here: no good analogy* | The key section. Probabilistic record linkage (hook: Census Linking Project, already cited in Claim 3) and missing-data imputation. Needs citations. Place the statistical-foundations point here. |
| Claim 4, *There* | Extend to drawing from multiple **models**, not just multiple runs. Note the tension: combining rules assume a common generating process, which distinct models are not. |
| Conclusion | Close the loop: Claims 1–3 have tools that merely need applying; Claim 4 has tools in statistics not being applied in this domain. That asymmetry is the contribution. |

## Citations added this session

Three Athey/Vafa items pulled from Zotero and appended to `references.bib`
(abstracts, keywords, and local `file =` paths stripped to match house style;
Zotero citation keys kept):

- `vafaCAREERFoundationModel2024` — CAREER: A Foundation Model for Labor Sequence Data (arXiv, 2024)
- `vafaEstimatingWageDisparities2025` — Estimating wage disparities using foundation models (*PNAS*, 2025)
- `atheyLABORLLMLanguageBasedOccupational2026` — LABOR-LLM (arXiv, 2026)

They are cited in one skeletal sentence in Claim 2 → Privacy so they are not
orphans. The substantive point available from them, and worth making: the resume
corpus is *proprietary* while the survey data are *restricted*, and the
fine-tuned model inherits both constraints at once — a sharper claim than "the
data are confidential."

Deliberately **not** added: Athey & Imbens (2019), "Machine Learning Methods That
Economists Should Know About." It is the fourth Athey hit in Zotero but is
unrelated to the personnel-data example.

**Orphaned entries** in `references.bib` (present, uncited — harmless to Quarto):
`kranzEconomicArticles2023`, `korinekGenerativeAIEconomic2023`,
`korinekDataCodeGenerative2023`. They were stranded when the 31%/8,280
controller-script statistic and the Korinek case study were cut from the
manuscript.

## Relationship to the companion paper

`~/Dropbox/Correspondence2026/ILR/Papers/Randomness_LLMs/MS_2026-07-27.tex`
(Coqueret, Llull, Oswald, Pérignon, Scheuch, Vilhuber — cited as
`coqueretRandomnessLLMs2026`) is a six-author working paper the author is a
co-author on. **It is not in this repo and will not transfer with it.**

The two papers differ on axis, which is what keeps this one distinct:

- **This paper:** curation and preservation; continuity thesis ("the challenges
  are real but not new").
- **Companion:** measurement and inference; discontinuity thesis ("LLM outputs
  are draws from a distribution, not fixed measurements").

The companion contains a 200-run 10-K sentiment experiment, a sources-of-
variation table (local vs. API controllability), and a two-check verification
protocol with an itemized reporting standard.

**Priority note worth preserving:** the multiple-imputation framing is the
author's own prior art — the May 2026 presentation in `presentation/` predates
the July 2026 companion draft, and MI is *absent* from the companion paper. An
earlier version of the text carried the phrase "that the companion paper does
not pursue" to mark this; it was cut during editing. Recommendation on record:
restore it or an equivalent, since without it a reader who knows both papers
sees MI applied to LLM variability with no signal about provenance.
Self-citation of `coqueretRandomnessLLMs2026` currently occurs at several
touchpoints, which is the clean defense against any appearance of overlap.

## Repo state and environment notes

Uncommitted at time of writing: `references.bib` (modified),
`reproducibility-ai-hdsr.md` (added + modified). Untracked: `Hdsr-llm.pdf`
(**the outline — commit this, the framework is unreadable without it**),
`IDCC26_Vilhuber.docx`, `reproducibility-ai.docx`,
`reproducibility-ai-hdsr.docx`, `.claude/`.

`reproducibility-ai.md` is the earlier IDCC-oriented version, still in the repo.
`reproducibility-ai-hdsr.md` is the HDSR branch of the same material and is the
one under active work.

Rendered `.docx` files are build products; consider `.gitignore` rather than
committing them.

**Zotero:** the local API must be enabled to query it — Edit → Settings →
Advanced → "Allow other applications on this computer to communicate with
Zotero". It is off by default and will be off on the new machine. Once on:
`curl -s "http://localhost:23119/api/users/0/items?q=<query>&format=json"`, and
`&format=bibtex` for export.

**Verification after rendering** (unzip the docx, strip XML, check for problems)
— worth repeating on the new machine to confirm the toolchain matches:

```bash
REPO=$(pwd)
quarto render reproducibility-ai-hdsr.md --to docx
rm -rf /tmp/docxcheck && mkdir -p /tmp/docxcheck && cd /tmp/docxcheck
unzip -q "$REPO/reproducibility-ai-hdsr.docx"
python3 -c "
import re; t=open('word/document.xml').read(); txt=re.sub(r'<[^>]+>','',t)
print('OMML math:', t.count('<m:oMath'))
print('Unresolved citations:', re.findall(r'@[a-zA-Z]\w+', txt) or 'none')
print('HTML comments leaked:', 'YES' if '<!--' in txt else 'none')"
```

Note: `\$` currency escapes in the Cost section are intentional and will show up
in any naive grep for stray dollar signs — they are not leaked math delimiters.

PDF output has **never been tested**; only docx has been rendered. The front
matter declares `pdf: default`, so the LaTeX path is untried and may need work.

## Known rough edges in the prose

Not fixed, because they are editorial calls:

- "ubitiquous" typo, in the environment-management section.
- The Clemens example now does double duty — it illustrates corpus/derived-
  artifact in Claim 2, and a short paragraph in Claim 3 preserves the older
  $D^*$/$\widetilde{D}$ reading. Decide whether one example can carry both.
- Bold pseudo-headings were replaced with real Markdown headings (`#`, `##`)
  because the framework is two levels deep. Revert if HDSR's style requires it.
