# Model card for "add model name here"

Sections and prompts from the [model cards paper](https://arxiv.org/abs/1810.03993), v2.

Jump to section:

- [Model details](#model-details)
- [Intended use](#intended-use)
- [Factors](#factors)
- [Metrics](#metrics)
- [Evaluation data](#evaluation-data)
- [Training data](#training-data)
- [Quantitative analyses](#quantitative-analyses)
- [Ethical considerations](#ethical-considerations)
- [Caveats and recommendations](#caveats-and-recommendations)

## Model details

_Basic information about the model._

- This model was developed by Chris Rodgers (supervised by Giulio Dalla Riva) for an assignment completed as part of DATA 417 - The Ethical data scientist
- Natural Language Model trained using spaCy to identify named entities in job advertisements as either masculine or feminine
- Assigns a gender target score to identify whether the job advertisement overall is more masucline, feminine or blanced
- Contact chrisrodgersba@gmail.com for any queries

## Intended use

- Intended to support authors of job advertisements to write their advertisements in a way that does not discourage specific applicants based on gender identity
- Should be used to advice only to writers on how their job advertisements may be received, authors should not automatically replace wprds identified as masculine or feminine.
- Should not be used in contexts outside of job advertisements (e.g. general advertising text, online forum comments)

## Factors

_Factors could include demographic or phenotypic groups, environmental conditions, technical
attributes, or others listed in Section 4.3._

- Gender identity (binary male and female) was taken into consideration for identifying gendered langauge.

## Metrics

_The appropriate metrics to feature in a model card depend on the type of model that is being tested.
For example, classification systems in which the primary output is a class label differ significantly
from systems whose primary output is a score. In all cases, the reported metrics should be determined
based on the model’s structure and intended use._

### Model performance measures

### Decision thresholds

### Approaches to uncertainty and variability

## Evaluation data

_All referenced datasets would ideally point to any set of documents that provide visibility into the
source and composition of the dataset. Evaluation datasets should include datasets that are publicly
available for third-party use. These could be existing datasets or new ones provided alongside the model
card analyses to enable further benchmarking._

Review section 4.5 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Datasets

### Motivation

### Preprocessing

## Training data

Review section 4.6 of the [model cards paper](https://arxiv.org/abs/1810.03993).

## Quantitative analyses

_Quantitative analyses should be disaggregated, that is, broken down by the chosen factors. Quantitative
analyses should provide the results of evaluating the model according to the chosen metrics, providing
confidence interval values when possible._

Review section 4.7 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Unitary results

### Intersectional result

## Ethical considerations

_This section is intended to demonstrate the ethical considerations that went into model development,
surfacing ethical challenges and solutions to stakeholders. Ethical analysis does not always lead to
precise solutions, but the process of ethical contemplation is worthwhile to inform on responsible
practices and next steps in future work._

Review section 4.8 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Data

### Human life

### Mitigations

### Risks and harms

### Use cases

## Caveats and recommendations

_This section should list additional concerns that were not covered in the previous sections._

Review section 4.9 of the [model cards paper](https://arxiv.org/abs/1810.03993).
