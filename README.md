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
- Evaluate the performance of the data science model developed for addressing the ethical concern
- Define an overall system for response to the ethical concern identified
- Identify limitations of the system defined and potential future improvements


## Evalute solution performance
The original ethical concern is that individuals are discouraged from applying for jobs because of the language used in the advertisement. Specifically this is the case with females being dissuaded by masculine language in job advertisements.

The data science solution developed addresses this by enabling identification of this language so that it could be corrected prior to advertising the job. 

To properly assess whether this intervention addresses the original ethical concern, it would be best to test whether modified advertisements led to higher appeal to females to apply. Unfortunately this is not something we can measure. 

We can measure instead though how effective the solution is at identifying gendered language. This can be done in two ways. First we can benchmark overall peformance against what previous studies have found in terms for the prevalence of gendered language. We can find if we are identifying at higher or lower rates. Second we can benchmark against existing bias identification tools. This will help us assess performance of the solution on individual ads.

In addition to this, we can also perform a manual inspection of several job advertisements and the gendered language identified in them. While this does not systematically show the likely response, it will give the reader a sense of how effective the solution is at identifying language that is likely to influence readers of job advertisements.



### Effectiveness of identifying gendered language
To assess the effecriveness of the model developed for identifying gendered language, we will first benchmark against existing efforts to identify gendered language.

To do this [1000] job advertisements were randomly selected from the indeed.com dataset. The NER model trained was applied to identify the masculine and feminine terms in each advertisement. Following this, the below summary statistics were calculated for each job advertisement.
- the total masculine words/phrases
- the total feminine words/phrases
- the percentage of words in the job description that are masculine
- the percentage of words in the job description that are feminine


#### Benchmarking against existing research/Effectiveness of identifying language
From this we calculauted the prevalence of gendered language across the entire corpus. Out of 1000 jobs:
- NNNN (XX%) were found to have masculine words
- NNNN (XX%) were found to have more masculine words than feminine words

Previous research has inspected the prevalence of gendered bias in job advertisements. In particular [this study] found that around XX% of job advertisements contained gendered language.

[This study] found that XX% of job advertisements contained gendered language.

In comparison, we can see that the solution developed here identifies language at a [higher/lower/same] rate.

 
### Effectiveness of identified language
While the above tells us that the rate at which the model is identifying gendered language is in line with what previous studies have found in terms of the prevalence of gendered language, we cannot conclude that the model is identifying the correct language.

To perform a qualitative assesssment we can inspect the results the model produces for individual ads to see if the results align with what we might expect. Further to this, we can also benchmark the performance of this model against existing tools for identifying gendered language in advertisements. 


A more comprehensive assessment with subject matter experts would be desired here, but I am just one person!


## Overall Ethical Response
While the model developed assists with identifying gendered language, it isn't enough as an entire system to address the original ethical concern. We are seeking to bring about changes in action, just wording changes is not going 

What we will also want in the overall system:
- Recommendations for alternative wording in advetisements
- Identification of attempts to cheat the wording
- Can't just remove masculine terms, sometimes these will be necessary




## Limitations
There are several limitations:
- Underlying bias in perceptions about job advertisements
- Sensitivity to industry needs to be included