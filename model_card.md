# Model card for EquiText

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
- The model performed well at identifying gendered terms.

|           | Masculine | Feminine | Overall |
|-----------|-----------|----------|---------|
| Precision | 0.99      | 0.99     | 0.99    |
| Recall    | 0.98      | 0.99     | 0.98    |
| F-Score   | 0.99      | 0.99     | 0.99    |

### Measure against generative AI examples

- Generative AI was used to generate masculine, feminine and neutral job advertisements. The model was used on these to identify masculine and feminine terms and generate a gender target score.

| Job Type                | Language Type | Gender Target Score |
|-------------------------|---------------|---------------------|
| Real estate agent       | masculine     | 0.44                |
| Real estate agent       | feminine      | 0.50                |
| Real estate agent       | neutral       | 0.43                |
| Mechanic                | masculine     | 0.48                |
| Mechanic                | feminine      | 0.52                |
| Mechanic                | neutral       | 0.56                |
| Early childhood teacher | masculine     | 0.55                |
| Early childhood teacher | feminine      | 0.56                |
| Early childhood teacher | neutral       | 0.55                |

Within each profession the results are as expected as the masculine language gender target score is lower (i.e. more masculine) than the feminine language gender target score. 



## Evaluation data

_All referenced datasets would ideally point to any set of documents that provide visibility into the
source and composition of the dataset. Evaluation datasets should include datasets that are publicly
available for third-party use. These could be existing datasets or new ones provided alongside the model
card analyses to enable further benchmarking._

Review section 4.5 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Datasets
- The [Indeed Job Posting](https://www.kaggle.com/datasets/promptcloud/indeed-job-posting-dataset) data was used for training and evaluating model performance.
- A random subset of 1000 job advertisements were selected from the dataset for use (due to processing power constraints).
- 700 advertisements were used for training, 300 used for testing.

### Preprocessing
- HTML tags were removed and all text was pushed to lower case.
- Masculine and feminine terms were labelled in the advertisements were automatically labeled according to existing lists of gendered terms as identified in existing research.


## Ethical considerations

_This section is intended to demonstrate the ethical considerations that went into model development,
surfacing ethical challenges and solutions to stakeholders. Ethical analysis does not always lead to
precise solutions, but the process of ethical contemplation is worthwhile to inform on responsible
practices and next steps in future work._

- Only one source of potential bias in job advertisements was examined (gender) it is also possible that other sensitive features should also be included (e.g. age).
- This was only applied in the domain of job advertisements as that is where existing research supports the existence of bias through language, this does not necessarily apply in other domains (e.g. advertising rental properties).



## Caveats and recommendations
_This section should list additional concerns that were not covered in the previous sections._

- Does not take into account other types of biased language that could impact job advertisements
- Biased language does not automatically mean the advertisement is 'wrong' - human authors should use this information as to whether it is appropriate to modify their job advertisement
- Further work may ne required to test across a wider range of genders (however existing research on the impact of gendered language only applies to binary gender)

