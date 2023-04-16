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
To assess the effectiveness of the model developed for identifying gendered language, we first benchmark against previous efforts to identify gendered language in job advertisements. Specificall

To do this [1000] job advertisements were randomly selected from the indeed.com dataset. The NER model trained was applied to identify masculine and feminine terms in each advertisement. Following this, the below metrics were calculated for each job advertisement.
- the total masculine terms identified in the advertisement
- the total feminine terms identified in the advertisement
- the percentage of words in the job description that are masculine
- the percentage of words in the job description that are feminine
- a gender target score

These metrics are used in several studies examining gendered language

#### Effectiveness of identifying gendered language
From the above, we calculauted the prevalence of gendered language across the entire corpus of job advertisements. Out of 1000 job advertisements:
- NNNN (97%) were found to have masculine words
- NNNN (100%) were found to have feminine words
- NNNN (X%) were found to have more masculine words than feminine words
- The average proportion of words in an advertisement that are masculine is 1.3%
- The average proportion of words in an advertisement that are feminine is 1.2%
- The average gender target score is 0.38.

The study completed by Gaucher et. al. 2011 examined the prevalence of gendered language in job advertisements and its impact on prospective applicants. Their study found that the average proportion of words in a job advertisement that are masculine is approximately 1.0%. For feminine words this is 0.6%. In comparison to this, the model developed for this assignment predicts somewhat in line with the expected average percentage for masculine words (1.0%). However, the model performs differently for feminine words where it predicts at twice the rate (1.2%), suggesting it is potentially over identifying feminine language in job advertisements.

A gender target score provides a more generalised metric. This metric has been applied in two pieces of research examined (Bohm et. al. and Tang et. al.) for this assignment. This approach measures gender bias according to a gender 'push-pull' score. This scoring approach defines maschuline terms as push words (i.e. would discourage applicants) and feminine words as pull words (i.e. would attract applicants). For the gender target score, feminine and masculine words cancel each other out with a final count being in surplus of masculine or feminine words. A sigmoid function is applied to the remaining words to produce a number in the range of 0 to 1. A neutral descriptions would receive a score of 0.5. The higher the score the more feminine the advertisement was with lower scores representing more masculine advertisements. 

The studies in question For the job advertisements assessed in this, there was an average score of 0.38 in the Bohm study and an average of 0.475 for the Tang study. Both these scores show a more masculine lean to the language in the job advertisements examined. The algorithm produced for this assignment produced an average score of 0.506. This logically follows from the previous assessment where feminine words appear to being more commonly identified.

In addition, this study also examined the most common key words in advertisement which gives another benchmark to assess against. The table below shows the most common masculine and feminine words and the proportion of identified words they make up.

| Masculine   | Prop | Feminine      | Prop |
|-------------|------|---------------|------|
| Ability     | 35%  | Involvement   | 32%  |
| Analysis    | 15%  | Creativity    | 24%  |
| Flexibility | 9%   | Communication | 12%  |

In comparison the mode for this assignment produced the result below in terms of most common terms.

| Masculine   | Prop | Feminine      | Prop |
|-------------|------|---------------|------|
| Ability     | 34%  | Work          | 28%  |
| Data        | 8%   | Service       | 19%  |
| Able        | 6%   | Support       | 9%  |

 
### Effectiveness of identified language
While the above tells us how effective the model is at identifying gendered language as benchmarked against previous research, we will also benefit from an inspection of some examples of the predictions made to get a better sense of the model's performance. To do this, we inspect the top 3 masculine and feminine advertisements in terms of the gender target score.

![image info](./masc_1.svg)
<img src="./masc_1.svg">

There are several observations we can make about the job ad



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
- Effort based assessments?
- Conditional superlatives?