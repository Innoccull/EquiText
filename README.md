# Detecting Bias in Job Advertisements


# Introduction
The goal of this project is to design a system that improves job advertisements so that they are more inclusive.


## Ethical concern
There is evidence that gendered language in job advertisements affects who applies. The affect of this gendered language on applicants is to create a decreased sense of belongingness with regard to the job which in turn decreases the appeal of the job to potential applicants.

There are several impacts of this. Firstly, for potential candidates it can limit the opportunities available to them. This is caused by the use of language that may make a job opportunity appear to them as something that they don't belong in. This limits the perceived opportunities available to individuals, in effect limiting their future earning and career prospects.

A second impact is on employers themselves. Producing job applications that can exclude some applicnts can lead to a less diverse pool of applicants to choose from in the selection process. 

## Response
The key ethical concern is that the use of certain language in job advertisements can reduce opportunities for individuals and limit the pool of applicants for employers. To address this concern, we would want a response that enables the production of job advertisements that do not include language that reduces an applicant's sense of belongingness with a position. The change in action we are trying to create is to change the wording of published job advertisements.

To do this, this projects creates a named entity recognition model that detects language in job advertisements that can discourage applicants. This data science approach alone is not sufficient though to create the desired change in action. We therefore look beyond this model itself to understand how it can be applied in practice along with other interventions, to create the desired change in behaviour that addresses the ethical concern identified.

## Evaluating performance
How do we measure if the ethical concern has been addressed?

# Methodology

How the data science solution was developed.

## Gender bias in job advertisements
There is existing research that shows that gender biased language in job advertisements can impact who applies [References]. 

There are several key leesons from this research:
- Masculine gendered language can create a decreased sense of belongingness for females. 
- A decreased sense of belongingness is associated with a decreased appeal of the job advertisements and therefore a lower likelihood to apply.
- Men are not impacted by the use of feminine language in advertisements. They do not experience a decreased sense of belongingness and are not discouraged from applying.

Lists of masculine and feminine terms were obtained from the research. These formed the basis of the named entity recognition model.

## Dataset
The indeed.com job advertisement data set was used. Sourced from kaggle.com [Reference]. This is a repository of 30,000 job advertisements posted on the US jobs website indeed.com between August 2019 and October 2019.

## Creating training data
The job advertisements from the indeed data set were first pre-processed to clean the data. This included removing HTML tags, pushing all text to lower case and removing URLs.

The resulting clean job description data was labelled in a gazetteer style approach. A python script was created to identify masculine and feminine words based on the lists obtained from research. The result was loaded to doccano, an open-source training data labelling tool [Reference]. In doccano, there was a manual inspection of several job descriptions to check for accuracy of labelling. 

A total of 1000 job advertisements from the 30,000 were randomly selected and annotated. 700 of these were used for training while 300 of these were sued for test.


## Model training and performance
A custom named entity recognition model was trained using spaCy [Reference]. spaCy is an open source NLP library that supports many NLP functions, including the ability to train custom named entity recognition.

A summary of the model performance is provided below.

|           | Masculine | Feminine | Overall |
|-----------|-----------|----------|---------|
| Precision | 0.99      | 0.99     | 0.99    |
| Recall    | 0.98      | 0.99     | 0.98    |
| F-Score   | 0.99      | 0.99     | 0.99    |

We can see that the model performs extremely well at identifying the gendered language in the job advertisements.


## An improved data product

As a data product, the model itself identifies language but does not provide something in itself actionable. To make this usable within the hiring process, we would at least need to expose an API that allowed external systems to query. Thsi API could accept the text for a job description 

# Ethical Assessment

In this final section we discuss how the original ethical concern identified can be addressed with the alternative solution developed. This is done in three parts:
- Evaluate the performance of the model developed for addressing the ethical concern
- Define an overall ethical response system
- Identify limitations of the system defined and potential future improvements


## Evalute solution performance
The original ethical concern is that individuals are discouraged from applying for jobs because of the language used. Specifically this is the case with females being put off by masculine language.

We cannot measure whether the solution makes job ads more appealing to females. We can observe general statistics on language identified and view some specific examples.

To do this a selection of [1000] job advertisements were selected from the indeed.com dataset. The trained model was applied to identify in each advertisement:
- the total masculine words/phrases
- the total feminine words/phrases
- pct of words in description that are masculine
- pct of words in description that are feminine

On this interpretation, we would make a difference by applying the model if the amount of masculine words were reduced. A total of NNNN jobs included masculine words, indicating that we could make NN% many jobs more appealing. 

While this overall assessment indicates the potential for improvement, it is not certain that removal or replacement of masculine terms will result in improvement. To get a sense of this, we can inspect a few results.

We look at the top 3 masculine.
