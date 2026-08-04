---
title: "Reproducibility in an Artificial Intelligence World: Challenges and Solutions for Scientific Research"
author:
  - name: Lars Vilhuber
    affiliations:
      - name: Cornell University
bibliography: references.bib
link-citations: true
format:
  docx: default
  pdf: default
---

# Introduction

The use of artificial intelligence in producing scientific articles has grown fast. Most of the discussion is about text generation, not about the growing use of AI inside the research process itself.

I approach this as a data editor, responsible for verifying reproducibility in economics. My argument is simple. The challenges posed by AI-supported research are real. They are not new. Economics has long dealt with opaque software, proprietary data, very large data, and APIs the researcher does not control. Labelling a system "AI" does not change how it should be curated. It changes how often the hard cases come up.

The argument has four claims. LLMs are code. LLMs are data. LLMs are used to generate data. And LLM-generated data is a random draw. The first three have good analogies in established practice. The fourth does not. Elsewhere we treat the sources of model variability [@coqueretRandomnessLLMs2026]; here I ask what must be deposited.

# Targets and notation

Verification requires more than re-running code. Materials must remain accessible to others, later, within a reasonable time. The standard solution is a compendium in a trusted repository holding all code and shareable data, with a documented access path for the rest [@vilhuberTemplateREADME2022].

Restricted data are not the exception in economics. They are the norm. Of 384 papers my team assessed at the American Economic Association in 2025, only 38% used unrestricted data [@vilhuberReportAEA2026]. We obtained private access for 45% of the rest. Inaccessible inputs do not preclude verification.

Fix notation. Let $\mathcal{M}^0$ be a pre-trained model, $D^t$ any fine-tuning data, $\mathcal{M}^t$ the tuned model, $D^*$ the researcher's raw data, and $\widetilde{D}$ the analysis data the model produces. Then

$$\mathcal{M}^t = f(D^t, \mathcal{M}^0), \qquad \widetilde{D} = g(\mathcal{M}^t, D^*).$$

In the zero-shot case $\mathcal{M}^t = \mathcal{M}^0$. All five must be accounted for, and differ sharply in size, licensing, privacy exposure, and preservability. Claim 1 concerns the models, Claim 2 $D^t$, Claim 3 $\widetilde{D}$, Claim 4 $g$.

# Claim 1: LLMs are code

**Here: online systems.** Economists already call remote services they do not control. A geocoder can change silently between research and replication, and an API call to a model is the same thing.

**Here: commercial software.** "Proprietary" is not binary. Old Stata versions still run and licenses transfer, so Stata is mostly preservable. MATLAB is close behind. SAS is not preservable at all. Open-source software is better archived, and every old R version remains on CRAN, but its distribution infrastructure fails too [@theregisterLeftPad2016]. The fix is containerization: the data editors' Docker Hub archive <https://hub.docker.com/u/dataeditors> keeps specific versions runnable after the license, vendor, or operating system has moved on.

**There: open-weight models.** Docker Hub is to Stata what Hugging Face is to an open-weight model, except that the preservation guarantee is weaker and the artifact far larger. Hugging Face assigns DOIs to some models and guarantees nothing. OpenAI released GPT-2 openly in 2019 [@OpenaicommunityGpt2Hugging] and did not release GPT-3. Researchers also want the newest model, which is usually the one that cannot be downloaded. And weights alone are not enough: the inference library, numerical precision, drivers, and processor all take part, so the guarantee attaches to the serving stack [@coqueretRandomnessLLMs2026]. That is environment management, extended to hardware.

# Claim 2: LLMs are data

Few social scientists train foundation models. They inherit the training data's curation problem anyway, and create a new one when they fine-tune.

**Here.** @clemensImmigrationRestrictions2018 deposited the raw scans of his primary sources [@clemensRawScans2017] and the processed replication data [@clemensReplicationData2018] as two separate citable deposits. Transcribing the scans by hand is expensive and will not be repeated, but transparent science requires only that it be possible. Here it is.

**There.** The same structure applies to $D^t$ and $\mathcal{M}^t$. Dell's "American Stories" corpus [@dell_research_harvard_2023] is documented on Hugging Face with a DOI; a model trained on it is the derived object, subject to Claim 1. Note the recursion: that corpus was itself extracted by language models, so Claim 3 feeds Claim 2.

**Privacy.** Fine-tuning on confidential data can produce a model that cannot be released. CAREER [@vafaCAREERFoundationModel2024] is fit to 24 million job sequences from proprietary resume data, then fine-tuned on survey data and applied to wage gaps [@vafaEstimatingWageDisparities2025; @atheyLABORLLMLanguageBasedOccupational2026]. The resume corpus is proprietary, the survey data restricted. The tuned model inherits both, and may leak what it memorized, so withholding $D^t$ is not sufficient. Statistical agencies already run this pattern: LEHD inputs are permanently confidential, the derived output verifiable through a secure enclave. Point that machinery at models.

# Claim 3: LLMs are used to generate data

**Here.** Geocoded output is deposited today precisely because the service cannot be relied on to return the same answer later: the same system as in Claim 1, seen once as code and once as a data generator. Data from commercial APIs such as Bureau van Dijk or Bloomberg are licensed, often non-redistributable, and revised silently. Researchers deposit an extract where permitted and document the access path where not.

**There.** The LLM API is the same object and takes the same solutions. Where licensing, confidentiality, and privacy permit, deposit the raw inputs and outputs of every run, before any parsing or cleaning. This is the most durable item in the package: it survives the model changing, becoming too expensive to re-run, or disappearing, and lets a verifier confirm that the deposited outputs do produce the published tables [@coqueretRandomnessLLMs2026]. Where the generated data serve many articles, deposit them separately, as the Census Linking Project <https://censuslinkingproject.org/> does.

# Claim 4: LLM-generated data is a random draw

The function $g(\mathcal{M}^t, D^*)$ is not deterministic. This is routinely ignored, in social science and in computer science alike. Setting temperature to zero removes deliberate token sampling but does not make a hosted API deterministic: model names are reused across silent updates, and floating-point rounding depends on server load and assigned hardware [@coqueretRandomnessLLMs2026]. Several frontier reasoning models have removed user-settable temperature entirely: the commercial frontier is moving away from researcher control, not toward it.

The consequence is statistical. @coqueretRandomnessLLMs2026 repeat one classification task 200 times with an unchanged prompt and model. Some runs cross conventional significance thresholds and others do not. A researcher who queries once has drawn one realization.

**Here: no good analogy.** Claims 1 through 3 each had one. This one does not: social scientists routinely consume the output of a stochastic process as if it were fixed. Probabilistic record linkage makes the same error: analysis conditions on one linkage as though it were certain. Missing-data imputation is what the discipline gets right, because multiply-imputed products ship with combining rules. The tools exist. The field is not applying them here.

**There.** Run the query $m$ times, ten say, with prompt, model, and settings fixed. Retain each $\widetilde{D}_i$, run the analysis on each, and obtain an estimate $q_i$ and variance $v_i$. Following @reiter2004, and after @rubin1993, compute

$$\bar{q}_m = \sum_{i=1}^{m} q_i/m, \quad b_m = \sum_{i=1}^{m} (q_i-\bar{q}_m)^2/(m-1), \quad \bar{v}_m = \sum_{i=1}^{m} v_i/m,$$

and report $\bar{q}_m$ with variance $T_p = b_m/m + \bar{v}_m$. These are the partially synthetic rules: $D^*$ is real, and only the derived variable is generated. The fully synthetic rules [@ReiterJ.Stat.Plan.Inference2005] apply otherwise.

The decomposition is the point. The term $\bar{v}_m$ is the sampling variability the researcher always faced; $b_m$ is what the model added. Reporting both makes the second visible rather than absorbing it into the estimate. A large $b_m$ also warns that a replicator should not expect to recover the numbers.

Three recommendations follow. Draw from multiple models, not only multiple runs of one. Provide all draws. Use all draws. The first carries a caveat, since the combining rules assume a common generating process and distinct models are not that. Across-model variation nonetheless matters most to a replicator, because the model version may not survive.

# Some guidance

**Log and pin.** Logs are evidence of execution when re-running is expensive or the data cannot be shared; hashing their contents improves credibility (TRACE, <https://transparency-certified.github.io/>). Never use "latest." Record the model identifier the API returned, not only the one requested, with date, time, and any system fingerprint. Record a parameter left at a default as a default rather than omitting it, because defaults move.

**Budget.** Research was already expensive: a Stata/MP-32 license costs about \$3,295 for two users, and three years of Compustat for China \$500,000. AI work adds training, inference, and repeated runs, and those costs must be quantified for the replicator. Where full reproduction is costly, provide a cheap subsample and run it through the best open-source model too: a robustness check for you, a cheaper path for the replicator.

# Conclusion

AI is not special. The difficulties are magnified relative to the average economics paper, and that is all. For Claims 1 through 3 the tools exist and need only be applied: trusted repositories, containers, two-deposit structures, secure enclaves, precise versions. For Claim 4 the tools exist too, in statistics, and are not being applied here. That asymmetry is this article's contribution.

The rest is computational empathy. Assume your replicator has none of your hardware, licenses, API keys, or models.

# References

::: {#refs}
:::
