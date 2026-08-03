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

<!--
STRUCTURE (per handwritten outline, Hdsr-llm.pdf). Four claims, each with the
same internal pattern:

    Claim  ->  "Here" (established analogy in existing practice)
           ->  "There" (the LLM case)
           ->  What to do

  1. LLMs are code
  2. LLMs are data (training data)
  3. LLMs are used to generate data
  4. LLM-generated data is a random draw   <- the one with no good analogy

Sections 0 (setup) and 5 (guidance) are cross-cutting and sit outside the four
claims. Language is NOT fleshed out below; fragments, notation, and examples
have been moved to where the outline puts them.
-->

# Introduction

The use of  artificial intelligence in the creation of scientific articles has seen an  astonishingly rapid increase in the social sciences. Most of the discussion has been about the production of articles, and estimates suggests that the number of articles created and possibly submitted with the help of AI systems is non-trivial. Less attention has been devoted to the use of AI as part of the legitimate scientific production process. Yet use of AI methods in legitimate scientific work is also increasing. With the earlier "replication crisis" still in mind, journal editors and researchers might wonder whether and how to preserve and publish AI-supported research tools, input data, and outputs. This article will approach the topic from the perspective of a "data editor", responsible for verifying reproducibility and supporting curation of research compendia in economics. My key argument is that the challenges posed by AI-supported research are real, but they are not new. Solutions to these challenges are often the same used by traditional research, but are more frequently in a space where imperfect, but not new, compromises are used.

In the economics literature, the use of online systems as part of a scientific workflow is astonishingly small, with most analysis still occurring with local computing resources and software tools. When APIs are used, they primarily serve data acquisition and (geo-)encoding, with discrete outputs that can be curated. Many economics software tools remain proprietary, and access to and curation of proprietery software can be challenging. The key to understanding the challenges posed by AI-facilitated research is that they are not fundamentally new, but have been less widespread in the past. The use of opaque commercial software, proprietary data, very large data, and  of external APIs that are not under the control of the researcher have all been seen before, and it is not because they now become labelled "AI" or "LLM"  that the fundamental approach on how to create and preserve reproducible research in this context changes. Thus, I will focus on  similarities with problems researchers already face when working with black-box systems, commercial software, and external APIs. AI systems magnify these challenges considerably compared to traditional economic research. I address how researchers may alleviate some of these challenges, similar to those existing solutions.

<!-- ROADMAP PARAGRAPH TO BE WRITTEN: state the four claims, and that the first
three have good analogies in existing practice while the fourth does not. -->

The argument proceeds in four claims. **LLMs are code**, and are curated as software is curated. **LLMs are data**, in that they embed training data, and are curated as data are curated. **LLMs are used to generate data**, and that generated data must be preserved and shared like any other derived data. And finally, **LLM-generated data is a random draw** — the one claim for which existing social-science practice offers no ready analogy, and the one that requires researchers to take the statistical foundations of data science seriously.

<!-- May not be necessary -->
A terminological note: throughout this article, I will try to distinguish between **LLMs** (large language models) — models that are trained for a specific, possibly broad, purpose and that can in principle be downloaded and run locally — and **AI** systems — online services that use LLMs, such as GPT, Claude, or Gemini, accessed through commercial interfaces or APIs. The distinction matters for reproducibility: the former are (large) software artifacts under potential researcher control, while the latter are black-box services whose behavior may change without notice. The focus here is on computational reproducibility, though the ultimate goal remains replicability of the underlying scientific findings.

<!-- May not be necessary -->
In other work [@coqueretRandomnessLLMs2026], we examine in detail the technical sources of non-determinism in LLM output and the consequences of that non-determinism for downstream statistical inference. This article takes the existence of such variability as given and focuses instead on the curation and preservation dimension: what must be documented, deposited, and preserved so that AI-supported research remains verifiable in the future. The two perspectives are complementary, and I draw on the companion paper's findings where they bear on curation practice.

# Fundamental Reproducibility Targets

Effective reproducibility verification requires not only conducting the re-analysis of data via provided code, but also establishing that research materials can be accessed by others, in the future, within reasonable timeframes. To this end, the standard solution is to use trusted repositories to create partial research compendia, comprised of all code and any shareable data. When data cannot be openly shared, the access mechanism itself must be described to ensure that, at least in the short term, such data can be obtained by others. Reproducibility editor like myself verify data provenance, and test reproducibility of both data access and computations.  In economics, established tools and standards guide this process, including the [Template README](https://social-science-data-editors.github.io/template_README/) framework [@vilhuberTemplateREADME2022] that structures the description of data provenance and access conditions for all raw data, requires documentation of all data transformations beginning with raw data, and requires provision of complete code including processing scripts for non-shareable data.

Restrictions on data access are not an exception in economics: They are the norm. Of  384 papers assessed by my team at the American Economic Association in 2025, only 38% used data with no access restrictions; the remaining 62% used data subject to some form of access restriction [@vilhuberReportAEA2026]. Yet this is a solvable problem: the Data Editor's team privately obtained access to the restricted data for 45% of those restricted-data papers,  even though the data could not be included in the public replication packages. The largest category of data we were not able to access are those in secure data enclaves, which around the world are accessible, albeit with hurdles, to 1000s of researchers. Inaccessibility of inputs, in other words, does not preclude verification.

## Notation

It is useful to fix notation at this point. Let $\mathcal{M}^0$ denote a pre-trained model, $D^t$ any data used to fine-tune it, $\mathcal{M}^t$ the resulting tuned model, $D^*$ the researcher's raw data, and $\widetilde{D}$ the analysis data that the model produces from it. The generic social-science workflow is then

$$\mathcal{M}^0 \; \longrightarrow \; \mathcal{M}^t \; \longrightarrow \; \widetilde{D},$$

where each arrow is a computation that consumes data:

$$\mathcal{M}^t = f(D^t, \mathcal{M}^0), \qquad \widetilde{D} = g(\mathcal{M}^t, D^*).$$

In the zero-shot case, no fine-tuning occurs, $\mathcal{M}^t = \mathcal{M}^0$, and only the second step applies. This notation makes the curation question precise: a reproducible research compendium must account for each of $\mathcal{M}^0$, $D^t$, $\mathcal{M}^t$, $D^*$, and $\widetilde{D}$, and these five objects differ sharply in size, licensing, privacy exposure, and the plausibility of long-term preservation.

<!-- The notation maps onto the four claims as follows; consider stating this
explicitly here, since it is what ties the sections together:

  Claim 1 (code)          -> the models themselves, M^0 and M^t
  Claim 2 (data)          -> the training data, D^t (and the corpus behind M^0)
  Claim 3 (generate data) -> the analysis data, D-tilde, and the map g()
  Claim 4 (random draw)   -> g() is stochastic; D-tilde is one draw

The outline annotates the examples with (P) and (L) markers -- restore those
here once their meaning is settled (preservable? licensed? large?).
-->

In the social sciences, the typical workflow starts with pre-trained  LLMs, which may be fine-tuned with specific data to create customized models, or used as-is for direct (zero-shot) inference. The curation of the raw training data, and often of the weights generated by such processes, is relegated to data and computer sciences [@hardingesWeMustFix2023]. Social scientists then use such models for inference or data generation, for subsequent quantitative analysis.

# Claim 1: LLMs are code

The question of whether large language models constitute data or software becomes particularly relevant. While this analysis treats models as software, their data-like characteristics in terms of size and access patterns create preservation challenges more similar to large datasets than traditional code repositories.

## Here: online systems

<!-- ANALOGY 1 -- TO BE WRITTEN: online systems as part of the workflow.
Leading example from the outline: geocoding via an online mapping service
(Maps). The researcher calls a remote system they do not control, whose
behavior can change silently between the time of research and the time of
replication. Same structure as an LLM API call. Cross-reference the geocoded
*output* in Claim 3. TODO: citation for a geocoding-in-economics example. -->

## Here: commercial software

Currently, most economists utilize commercial software with relatively standardized access, and sometimes rely on commercially collected data, with subscriptions costing many thousands of dollars.

<!-- ANALOGY 2 -- TO BE WRITTEN: the spectrum of preservability of commercial
software, from the outline:

  - Stata    -- mostly good  (old versions runnable, licenses transferable)
  - MATLAB   -- pretty good
  - SAS      -- not possible
  - others

The point is that "proprietary" is not a binary: commercial software already
spans a range from near-fully preservable to not preservable at all, and
LLMs sit on that same spectrum rather than off it. TODO: verify and document
the version/licensing facts behind each of the three rankings. -->

Because most researchers use the same few commercial packages, access is not as constraining as it might seem at first blush, though commercial software can go away and licenses expire. Open-source software is, in principle, more robustly archived: Every older R version and package remains available on CRAN. But open-source software is not immune to failure points in the  distribution infrastructure. Readers might remember the 2016 "left-pad" incident, in which the removal of an 11-line package briefly broke thousands of software builds [@theregisterLeftPad2016].

The solution in the traditional case is containerization: the data editors' Docker Hub archive <https://hub.docker.com/u/dataeditors> preserves runnable images of specific versions of commercial statistical software, so that a replication package remains executable after the license, the vendor, or the operating system has moved on.

## There: open-weight models

One possible solution to this is to use downloadable models, whether openly licensed or those subject to restrictive licenses. Specialized platforms do exist, such as Hugging Face, which provide some level of model preservation, but their commitment to long-term preservation is weak, and their focus is on sharing models, not necessarily preserving them.[^hugpreserve]  The transition of organizations from non-profit to commercial status, as seen with OpenAI's evolution from releasing GPT-2 openly in 2019 [@OpenaicommunityGpt2Hugging] to restricting access to GPT-3, illustrates how access to specific model versions may become limited over time. Openly licensed models are only partially immune to this concern: Meta's Llama models, for instance, are downloadable from Hugging Face but carry no DOI, and could in principle be withdrawn at the provider's discretion.

[^hugpreserve]:  While Hugging Face assigns DOIs to some models and provides presumptions of preservation, no formal guarantees exist.

Furthermore, researchers are drawn to the "latest and greatest" models, which may not be available for download. Most downloadable models may lag in performance and quality. Researchers wishing to improve reproducibility face a tradeoff between said reproducibility and the quality of their inference.

<!-- The parallel to make explicit: Docker Hub is to Stata as Hugging Face is
to an open-weight model -- except that the preservation guarantee is weaker
and the artifact is orders of magnitude larger. -->

Both the tuned model $\mathcal{M}^t$ and the resulting analysis data $\widetilde{D}$ should ideally be preserved. This presents significant challenges. The size of these datasets usually exceeds the typical project-level storage capabilities of general-purpose and social-science focused repositories.

## Code is more than the model: environment and dependencies

The most fundamental test of reproducibility requires that code execute completely from beginning to end without error and ideally without user intervention. This should recreate all figures, tables, and numerical results included in research publications. Inadequate software version control and missing dependencies (libraries, packages) are frequent causes of failure to reproduce. Many open source packages evolve rapidly, and cascading dependency trees can make precise reproduction challenging.

AI research is no different, except that it may still be evolving more rapidly than the average open source toolkit. Simply put, the dependencies used in AI-based research may be evolving more rapidly than the average open source package, and are thus more likely to break. The solutions, however, are the same. Correct version control of libraries, clearly and fully specified calls to such libraries can mitigate the likelihood of code breakages. Rapidly evolving APIs create reproducibility barriers independent of the quality of the research methodology.

The computational environment presents another critical dimension for reproducibility. Documentation must describe both the hardware and software configurations used by researchers, including relevant hardware specifications, memory requirements, storage needs, and necessary software with specific library versions. This is even more relevant for research using LLMs, which evolve rapidly, and proper environment preservation becomes essential.  LLM applications often require stricter operating conditions than typical economic research, potentially necessitating specialized hardware configurations such as specific and expensive graphics cards (GPUs), which must be purchased or rented.

Local execution of open-weight models makes exact reproduction *achievable*, but does not by itself guarantee it: the guarantee attaches to the entire serving stack, not to the weights alone. Identical weights loaded on different machines, or served through different cloud providers, do not always agree, because the inference library, numerical precision, driver versions, batch size, and processor all participate in the computation [@coqueretRandomnessLLMs2026]. Determinism is attainable when that whole environment is fixed, documented, and preserved — which is precisely the environment-management problem discussed below, now extended to hardware.

# Claim 2: LLMs are data

Most social scientists do not train de-novo foundation models. They nevertheless inherit the curation problem attached to the data those models were trained on, and they create a new one whenever they fine-tune.

## Here: raw sources and their transcription

Consider a more traditional example that includes relative large-scale preservation of raw data.  In their study of the Mexican Bracero exclusion, @clemensImmigrationRestrictions2018 preserved both the raw scanned PDFs of primary sources on workers, wages, and crops [@clemensRawScans2017] and the processed replication data [@clemensReplicationData2018], each as separate, citable deposits on Harvard Dataverse. The work to convert the raw data into a quantitative format is typically not repeated — it is expensive, and in the Clemens case was done by hand — but transparent science requires that it be possible to do so. In the Clemens case, it is.

<!-- The two-deposit structure is the template: raw corpus and derived product
are preserved separately, each citable, each with its own size and license
profile. In the notation, the raw scans are the corpus and the transcribed
data is the derived object -- the same relation that holds between a training
corpus and the model derived from it. -->

## There: training corpora and the models derived from them

In the LLM case the same two-deposit structure applies to $D^t$ and $\mathcal{M}^t$: the corpus and the artifact derived from it. Dell's "American Stories" dataset [@dell_research_harvard_2023], a large-scale corpus extracted from historical newspapers using language models, is preserved and documented on Hugging Face with an assigned DOI — the raw corpus. The foundation model trained on such a corpus is the derived object, and is subject to the preservation constraints of Claim 1.

<!-- Note the recursion worth flagging: American Stories is itself LLM-generated
data (Claim 3) that then serves as a training corpus (Claim 2). -->

## Privacy: when the training data cannot be released

Fine-tuning on confidential data creates a model that may not be releasable at all.

The CAREER model [@vafaCAREERFoundationModel2024] is fit to 24 million job sequences drawn from proprietary online resume data and then fine-tuned on longitudinal survey data; @vafaEstimatingWageDisparities2025 apply the resulting foundation model to gender wage gap estimation using the Panel Study of Income Dynamics, and @atheyLABORLLMLanguageBasedOccupational2026 extend the approach by fine-tuning general-purpose LLMs on career histories rendered as text.

<!-- EXAMPLE TO BE FLESHED OUT (Athey et al., cited above): the tuned model
$\mathcal{M}^t$ cannot be made public because the underlying $D^t$ is
confidential or licensed -- and the model may itself leak the data it
memorized, which is a stronger constraint than merely withholding $D^t$.
Note both layers here: the resume corpus is *proprietary*, the survey data
are *restricted*, and the fine-tuned model inherits both.

The counter-example from the outline: the LEHD, and statistical agencies more
generally, already operate the pattern where the input data are permanently
confidential but the derived research output is verifiable through a secure
enclave. That machinery exists and can be pointed at models. -->

In addition, for LLM-specific applications, researchers must consider whether tuned models can be released given privacy constraints, and what license should apply to them.

# Claim 3: LLMs are used to generate data

Research involving AI systems typically encounters three distinct types of data: training data used to develop models, analysis data used for research purposes, and output data generated by algorithms. Each category presents unique challenges for reproducibility. The fundamental questions surrounding data provenance become more complex in AI contexts: determining the origins of training and analysis data, establishing whether data can be shared with others, assessing continued accessibility, and evaluating preservation capabilities. The generated data $\widetilde{D}$ should be preserved and shared.

## Here: geocoded data

<!-- ANALOGY -- TO BE WRITTEN: geocoded data are the output of a call to a
geocoding service. Established practice already treats the geocoded output as
a data object to be deposited, precisely because the service cannot be relied
on to return the same answer later. This is the closest existing analogue to
depositing raw LLM output. Ties back to the geocoding example in Claim 1:
same system, viewed once as code and once as a data generator. -->

## Here: data obtained via APIs

<!-- ANALOGY -- TO BE WRITTEN, two cases from the outline:
  - public APIs (e.g. statistical agency APIs): output is depositable, though
    the series may be revised.
  - commercial APIs: Bureau van Dijk, Refinitiv, Bloomberg Terminal. Output is
    licensed, often non-redistributable, and the vendor may revise history
    silently. Researchers already handle this by depositing an extract where
    permitted and documenting the access path where not.
The LLM API is the same object with the same solutions. -->

The use of LLMs via commercial providers or running on rented cloud resources is simply an extension of that practice. While these are real impediments to greater accessibility, and thus possibly to "open science", these impediments are not new.

## There: preserving generated data

When the generated data serve multiple purposes beyond a single article, separate preservation may be more appropriate. A traditional example is the [Census Linking Project](https://censuslinkingproject.org/), which  distributes record linkages used across many studies.

In the notation above, Clemens preserved both $D^*$, the scanned primary sources, and $\widetilde{D}$, the quantitative dataset derived from them. In the context of AI, the parallel is to preserve $D^*$ and $\widetilde{D}$ wherever possible, and, where a model was fine-tuned, $D^t$ and $\mathcal{M}^t$ as well.

This has a direct implication for what belongs in a replication package. Where licensing, confidentiality, and privacy constraints permit — and those constraints are real — the raw model inputs and outputs of every run should be deposited, before any parsing, cleaning, or manual correction. Such a deposit is the most durable item in an AI-supported replication package, because it is the only one that survives the model itself changing, becoming prohibitively expensive to re-run, or disappearing entirely. It permits a verifier to bypass the generation step and confirm that the deposited outputs do in fact produce the published tables, which is a meaningful reproducibility check even when regenerating the outputs is impossible. It also allows future researchers to apply alternative parsing or validation rules to the same raw material [@coqueretRandomnessLLMs2026]. A well-constructed package should support both routes: full regeneration from prompts, with an estimate of the expected cost and runtime, and the shortcut that treats the deposited output as given.

# Claim 4: LLM-generated data is a random draw

The generating function $g(\mathcal{M}^t, D^*)$ is not deterministic. This is frequently ignored, in the social sciences and in computer science alike.

## Why the draw is random

A second and more fundamental source of irreproducibility is the model itself. Early LLMs were frankly probabilistic: they offered no way to fix a seed for the underlying pseudo-random number generator, and were updated on the fly, so that both the software and the data it produced changed over time in uncontrolled fashion. It would be comforting to report that this situation has improved. It has not, and in some respects it has deteriorated. Setting a model's "temperature" parameter to zero removes deliberate token sampling, but does not yield deterministic output when the model is accessed through a commercial API: variation persists through silent model updates behind unchanged model names, through floating-point rounding whose order of operations depends on server load, batching, and the particular hardware assigned to a request, and through expert routing in mixture-of-experts architectures, where a request's treatment can depend on which other users' requests happen to be processed alongside it [@coqueretRandomnessLLMs2026]. Seeds, where providers expose them, improve reproducibility only when the prompt, model, decoding settings, sampling implementation, and serving environment all remain unchanged — conditions that hosted APIs do not guarantee. Most consequentially for researchers, several frontier reasoning models released by major providers have *removed* user-settable temperature altogether, replacing it with a reasoning-effort setting while the provider manages the sampling configuration. A researcher using such a model through an API cannot suppress deliberate sampling at all. The trajectory of the commercial frontier is therefore away from researcher control, not toward it, and reproducibility guidance should be written accordingly.

Beyond the software engineering concerns, the persistent variability described above raises a statistical question: is a result based on LLM-generated data robust to the variability of that generation process? The question is not academic. @coqueretRandomnessLLMs2026 repeat a single sentiment-classification task over corporate filings two hundred times with an unchanged prompt and model, and show that the resulting distribution of downstream regression test statistics is wide enough that a non-trivial share of runs cross conventional significance thresholds while others do not. A researcher who queries the model once and reports the result has drawn a single realization from that distribution.

## Here: no good analogy

<!-- KEY STRUCTURAL POINT from the outline. Claims 1-3 each had a clean
analogy in existing practice. This one does not: social scientists routinely
consume the *output* of stochastic generating processes as though it were
fixed. Two examples where the same error is made, and where the statistical
literature has already supplied the fix:

  - probabilistic record linkage: linkages are draws, but downstream analysis
    almost always conditions on one linkage as if it were certain. TODO cite;
    the Census Linking Project (Claim 3) is the obvious hook.
  - imputation for missing data in surveys and administrative data: here the
    discipline *does* get it right, because multiply-imputed products ship
    with combining rules and users are told to use them.

This is where to make the broader point (margin note in the outline): the
statistical foundations of data science matter, and this is a case where the
field has the tools and is simply not applying them. -->

## There: multiple draws and multiple-imputation inference

Rather than treating this variability as a nuisance to be minimized and then ignored, researchers can treat it formally, drawing on a well-established literature in statistics: the analysis data generated by an LLM can be viewed as a multiple imputation problem. @rubin1993 is credited with one of the first formalizations of multiple imputation, often used for privacy protection as well as for missing data; @reiter2004 and @ReiterJ.Stat.Plan.Inference2005 provide the corresponding inference rules for synthetic data.

The recommendation follows directly. Rather than generating the analysis data once, run the LLM query $m$ times — ten, say — holding the prompt, model, and settings fixed, and retain each of the resulting datasets $\widetilde{D}_i = g(\mathcal{M}^t, D^*)$, $i = 1, \ldots, m$. Run the downstream analysis separately on each, obtaining from each a point estimate $q_i$ of the quantity of interest and its estimated variance $v_i$. Following @reiter2004, combine them as

$$\bar{q}_m = \sum_{i=1}^{m} q_i / m, \qquad b_m = \sum_{i=1}^{m} (q_i - \bar{q}_m)^2 / (m-1), \qquad \bar{v}_m = \sum_{i=1}^{m} v_i / m,$$

and report $\bar{q}_m$ as the estimate of the quantity of interest, with variance

$$T_p = b_m/m + \bar{v}_m .$$

The decomposition is the point of the exercise. The term $\bar{v}_m$ captures the sampling variability inherent in the underlying data $D^*$ — the variability a researcher would face even with a perfectly deterministic measurement instrument — while $b_m$ captures the variability contributed by the LLM itself. Reporting both separates the uncertainty the researcher has always had to acknowledge from the uncertainty the model has added, and makes the latter visible rather than silently absorbed into the point estimate. Note that these are the combining rules for *partially* synthetic data: the raw data $D^*$ are real, and only the derived variable is model-generated. The fully synthetic rules of @ReiterJ.Stat.Plan.Inference2005 would apply if the model were generating the analysis dataset outright.

<!-- EXTENSION TO BE WRITTEN, from the outline: draw from multiple *models*,
not only multiple runs of one model. The three-part recommendation is:
  (i)   draw from multiple models;
  (ii)  provide all draws in the replication package;
  (iii) use all draws in the analysis, via the combining rules above.
Across-model variation is arguably the more relevant uncertainty for a
replicator, since the specific model version may not survive. Note the
tension: the combining rules assume draws from a common process, which
multiple models are not. Connects to the open-source-model comparison
suggested under Cost, below. -->

A useful by-product is that $b_m$ is itself a reproducibility diagnostic. A large $b_m$ relative to $\bar{v}_m$ signals that the published result rests substantially on which draw the author happened to obtain, which is precisely the situation in which a replicator should not expect to recover the original numbers, and in which the deposited raw outputs discussed above become indispensable. Researchers should be precise about all parameters of the generation process, and document the observed variability for future replicators.

# Some Guidance

## Logging and Documentation Practices

Comprehensive logging can serve as crucial evidence of code execution, particularly important for computationally expensive operations or when working with data that cannot be shared. This is true even before considering LLMs. Most statistical software provides mechanisms for creating execution records, though some require explicit instruction to generate verbose output or command-line options for log file creation. For Python applications, custom wrapper functions can track function calls with timestamps, arguments, and return values. These approaches provide documentation that code has executed while capturing relevant metadata about the computational process. Decorators can automatically log function calls with parameters and timing.

These logs serve dual purposes: documenting successful execution for researchers and providing evidence of reproducibility for journals and reviewers. In cases where replication requires expensive computational resources or access to restricted data, log files may provide the only feasible method for demonstrating code functionality. The credibility of such log files, which are not impervious to manipulation, can be enhanced by using tools that generate cryptographic hashes of log contents, ensuring integrity and authenticity. The TRACE project <https://transparency-certified.github.io/> provides one approach, adaptable to certain circumstances.

## Environmental Management and Dependency Specification

Most AI-based research in the social sciences uses Python, so I will focus this discussion to that programming language, but similar methods exist for Julia and R, among the programming languages in use by social scientists. Python environments are a potential solution for many reproducibility challenges, but their implementation can present particular challenges for reproducibility. While "pip freeze" is recommended for documentation, it may not generate robust reproducible environments due to platform-specific dependencies. The solution involves identifying minimal package requirements corresponding to explicit imports in code, then pruning requirements files to essential components. The goal involves creating environments that capture necessary dependencies while allowing package managers to resolve secondary dependencies appropriately.

In the context of AI research, the environment must also account for ubitiquous use of API keys. Secure programming methods are not well established in the social sciences, and many researchers have very manual methods, if at all, of managing API keys. Furthermore, most Python libraries do not allow to pin the LLM used within. This is relegated to the user-generated code, which must be careful to document and use the specific model versions used. The use of "default" values or simply using the "latest" model is strongly discouraged, as it is detrimental to even short-term reproducibility. This parallels API data access issues, where "latest" data may be revised between research and publication.

Recording the model version one *requested* is necessary but not sufficient. Because providers may alter the model served behind an unchanged public name, researchers should log, for every call, the model identifier the API actually *returned*, along with the date and time of execution and any system fingerprint the provider supplies. These records cannot prevent a silent substitution, but they make an otherwise invisible change detectable after the fact — and a change detected during data collection, when observations processed on different dates may no longer be comparable, is considerably more useful than one discovered by a replicator years later. The same logic applies to generation parameters: a parameter left at a provider default should be recorded as having been left at its default, rather than omitted, since defaults themselves are not stable across model versions.

## Cost Considerations and Resource Planning

AI research involves significant computational costs that must be documented and planned. Traditional economic research might require expenditures for software licenses, data access, or travel for restricted data. Consider on-site or controlled access to data enclaves. The Federal Statistical Research Data Centers provide access to researchers physically present in the United States, and in many cases, only via physical secure rooms. Much European data is only available either on-site or from researchers physically present in Europe. For researchers, this can create considerable travel costs, which must be covered by research funds or grants. Some concrete orders of magnitude from traditional economic research: a Stata/MP-32 license costs about \$3,295 for two users; three years of access to Compustat for China can cost \$500,000; three weeks in Norway for in-person access to linked employer-employee data might run \$3,000; and a computation using 20,000 core-hours on a large cloud instance (128 CPUs with 4TB of memory) costs on the order of \$4,168. AI applications also may have substantial costs for model training, inference operations, and repeated executions for variability assessment. These costs must be quantified for future researchers wishing to replicate results, even if such costs may be declining rapidly over time for access via commercial providers. Arguably, these costs  exceed "traditional" economic research by orders of magnitude, when such traditional research uses relatively small public-use datasets that can be analyzed by students on cheap laptops. Training models in cloud environments, running models on datasets multiple times, and assessing result variability can each cost thousands of dollars. These expenses make replication economically challenging and may limit reproducibility testing to well-funded research groups. Creating scientific output costs money, and the use of LLMs does not change that. It may not even cost more than research produced by other methods.

When full-scale reproduction costs a lot, researchers can mitigate the burden. One strategy is to provide a subsample of the data that is cheaper and faster to reproduce, and to use that subsample themselves to probe robustness: how do results change when using different models, and how do they change when, just before submitting the package, the analysis is run once more on the same model (or what is believed to be the same model)? A complementary strategy addresses whether reproduction needs to be expensive at all: run the analysis through the best available open-source model and compare the output. Is the result robust to the change of model? Is the commercial model's output measurably "better" — and by what metric? Documenting these comparisons gives replicators a cheaper path to verification while also serving as a robustness check for the research itself.

## Summary of Best Practices

Effective reproducibility in AI research requires implementation of several key practices. The principles below are deliberately stated at the level of what researchers should aim for; @coqueretRandomnessLLMs2026 develop a corresponding itemized reporting standard that distinguishes what belongs in the paper from what belongs in the replication package, and separates the items that are essentially costless to provide from those that require additional work. Environmental management from project inception ensures consistent computational conditions. Comprehensive logging provides evidence of execution, particularly valuable when repetition is expensive. Version precision applies to input data, software dependencies, and critically, model versions used - avoiding references to "latest" models that may change over time. Complete code inclusion encompasses prompts, intermediate responses, and processing scripts, even when underlying data cannot be shared. In AI contexts, the code itself, including specific prompts used with models, constitutes crucial methodological information that affects result interpretation. Metadata documentation should specify random seeds where possible, hyperparameters, "temperature" settings, and other configuration details. Prompts themselves should be considered metadata requiring preservation, as slight variations in prompt formulation can substantially affect model outputs.

Data preservation strategies must consider licensing constraints and storage requirements. Industry repositories may serve adequately for sharing purposes, while academic repositories like Zenodo and Dataverse provide formal preservation commitments. The toolkit for preserving large datasets exceeding 200GB remains underdeveloped, presenting ongoing challenges for AI research that routinely generates datasets of this scale.

# Conclusion

While AI and LLMs are not fundamentally different from other computational approaches regarding reproducibility principles, they may appear to magnify existing difficulties  compared to "typical" economic research practices. The solutions involve maintaining reproducible practices from project initiation, exercising computational empathy by considering others' technical constraints, ensuring precision in version specification, and utilizing existing resources like the [Template README](https://social-science-data-editors.github.io/template_README/) [@vilhuberTemplateREADME2022] and [self-checking reproducibility guidance](https://larsvilhuber.github.io/self-checking-reproducibility/).

<!-- The conclusion should now close the four-claim loop: for Claims 1-3 the
tools exist and the task is to apply them; for Claim 4 the tools exist in
statistics but are not being applied in this domain. That asymmetry is the
paper's contribution and should be stated here. -->

The field continues evolving rapidly, requiring researchers to adapt traditional reproducibility practices to accommodate new technological constraints while maintaining scientific rigor. Success depends on recognition that reproducibility challenges, while amplified in AI contexts, remain addressable through careful attention to documentation, environmental management, and transparent reporting practices. The fundamental goal remains unchanged: ensuring that scientific findings can be verified, understood, and built upon by other researchers, thereby maintaining the integrity and advancement of scientific knowledge in an (increasingly?) AI-dependent research landscape.

# References

::: {#refs}
:::
