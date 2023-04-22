# Detecting and Addressing Bias in Job Advertisements


# Introduction
Ethics is critically important for data scientists because the data science solutions they develop can have wide-ranging implications for society, individuals, and businesses. Ethics provides a framework for data scientists to ensure that their work is conducted in a responsible, transparent, and socially acceptable manner.


The goal of this project is to design a solution that addresses an ethical concern with an existing data science product. In doing so, we demonstrate how data science solutions can be developed to better align with desired ethical outcomes. 

This project is executed in three parts:
1. **Identify the ethical concern:** we identify the ethical concern this project seeks to address and the proposed data science response
2. **Develop a data science response:** we develop a data science model that supports addressing the ethical concern 
3. **Ethical response assessment:** we evaluate how well the data science response addresses the ethical concern, propose an overall response that attempts to fully address the ethical concern and discuss possible avenues for future development of an overall response


# Ethical concern
First we identify the ethical concern and proposed data science response that will be developed as part of this assignment.

## Discriminatory language in job advertisements
There is research which has found that gendered language in job advertisements affects who applies [Gautier 2011](https://ideas.wharton.upenn.edu/wp-content/uploads/2018/07/Gaucher-Friesen-Kay-2011.pdf). This research showed that gendered language in job advertisements causes prospective applicants to have a decreased sense of belongingness in relation to the job advertised. This decreased sense of belongingness in turn decreases the appeal of the job to potential applicants, making them less likely to apply.

There are several key leesons from this research:
- Masculine gendered language can create a decreased sense of belongingness for females. 
- A decreased sense of belongingness is associated with a decreased appeal of the job advertisements and therefore a lower likelihood to apply.
- Men are not impacted by the use of feminine language in advertisements. They do not experience a decreased sense of belongingness and are not discouraged from applying.

This impacts on both individuals and employers. For individuals, it limits the perceived opportunities available for members of groups that will feel a lesser sense of belongingness in response to the language used. In effect this limits their future earning and career prospects.

For employers, producing job applications that can exclude some applicants can lead to a less diverse and talented pool of applicants to choose from in the selection process. It can also create regulatory risk where there are relevant anti-discrimination regulations and/or laws in place. Finally, it can also lead to overall negative brand perception if an organisation is perceived as biased towards/against specific genders through its use of language.

## Response
To address this concern, we would want a response that enables the production of job advertisements that do not include gendered language which reduces an applicant's sense of belongingness in relation to an advertised position.

This project develops a named entity recognition (NER) model to detect gendered language in job ads and assign a 'gender target' score indicating masculine, feminine, or neutral tones for the advertisement. The development of this model is covered in the Data Science Response section below. However, the data science solution alone is not enough to create the change in real-world action required to address the ethical concern. The project therefore also considers further interventions that can be made to create a complete system that addresses the ethical concern.


# Data Science Response

In this section we outline how a data science model was developed to address the ethical concern identified.

## Gendered language
The research referenced above used a list of common masculine and feminine terms in their study. These lists were re-used for training the named entity recognition model.

The list of masculine terms used can be found [here](https://github.com/Innoccull/DATA417/blob/main/data/masculine.csv).

The list of feminine terms used can be found [here](https://github.com/Innoccull/DATA417/blob/main/data/feminine.csv).

## Dataset
To train an NER model, a dataset of job descriptions is required. For this project we chose to use the Indeed Job Posting dataset. 

This dataset was created by [PromptCloud](www.promptcloud.com) and [DataStock](datastock.shop). It contains around 30,000 records of job pastings made to indeed.com from Aug - Oct 2019. 

The dataset was downloaded from [Kaggle](https://www.kaggle.com/datasets/promptcloud/indeed-job-posting-dataset).

## Creating training data
To create the training data for the NER model, we took a random selection of 1000 jobs from the Indeed Jobs dataset. This amount was chosen due to processing power constraints.

The job descriptions for the advertisements chosen were pre-processed to clean the data. This included removing HTML tags, pushing all text to lower case and removing URLs.

The resulting clean job description data were labelled in a gazetteer style approach. A python script was created to identify masculine and feminine words in the job descriptions based on the masculine and feminine terms lists linked above. 

The auto-labelled job descriptions were loaded to [doccano](https://github.com/doccano/doccano), an open-source training data labelling tool. In doccano, there was a manual inspection of several job descriptions to check for accuracy of labelling. No inaccuracies were identified so the auto-annotations were accepted for training.

Of the 1000 jobs randmly selected, 700 of these were used for training while 300 of these were used for test.


## Model training and performance
A custom named entity recognition model was trained using [spaCy](https://spacy.io/). spaCy is an open source NLP library that supports many NLP functions, including the ability to train custom named entity recognition. 

The named entity recognition model was trained to recognise masculine and feminine terms. A summary of the model performance is provided below.

|           | Masculine | Feminine | Overall |
|-----------|-----------|----------|---------|
| Precision | 0.99      | 0.99     | 0.99    |
| Recall    | 0.98      | 0.99     | 0.98    |
| F-Score   | 0.99      | 0.99     | 0.99    |

We can see that the model performs extremely well at identifying the gendered language in the job advertisements based on the training and test data provided.

## Scoring advertisements
Finally, several 'gender scoring' statistics were calculated for each job advertisement based on the gendered terms identified. These statistics included:
- the total masculine terms identified in the advertisement
- the total feminine terms identified in the advertisement
- the percentage of words in the job description that are masculine
- the percentage of words in the job description that are feminine
- a gender target score

These statistics enable more precise assessment of which advertisements require intervention. Based on the research, advertisements with a higher percentage of masculine terms or with gender target scores that indicate a more masculine advertisement would be in greater need of intervention.


# Ethical Assessment

In this final section we perform an assessment of how we address the original ethical concern. This is done in three parts:
- Evaluate the performance of the data science model developed for addressing the ethical concern
- Define an overall system for response to the ethical concern identified
- Identify limitations of the overall system defined and potential future improvements


## Evalute solution performance
The original ethical concern is that individuals are discouraged from applying for jobs because of gendered language used in the advertisement. Specifically this is the case with females being dissuaded by masculine language in job advertisements. The data science solution developed addresses this by enabling identification of this language through an NER model so that it could be corrected prior to advertising the job. 

To properly assess whether this intervention addresses the original ethical concern, it would be best to test whether advertisements modified based on the gendered language identified led to a higher likelihood for the target audience to apply. This is the approach taken in several other pieces of research.

A design to do this evaluation would be to:
1. Select a sample of job advertisements
2. Apply the NER model to identify gendered terms and score accordingly
3. Select the most masculine and feminine job advertisements
4. Create separate masculine, feminine and neutral versions of thesejob advertisements
5. Present these to individuals and survey their sense of belongingness and willingness to apply to these advertisements

Unfortunately step 5 is beyond the scope of this assignment as it would require sourcing participants to evaluate the advertisements so we must take an alternative approach to evaluating the solution.

<br/>

As an alternative approach, we can instead measure how effective the NER model is at identifying gendered language. On this approach we do not understand if we have made the advertisements less likely to discourage applicants, but we do understand the extent to which it would be possible to produce improved advertisements based on modifying the language identified. If the NER model identifies, for example, too many masculine terms or the wrong masculine terms - the alternative advertisements produced based on it may not be effective.


There are three ways in which we will do this evaluation of the effectiveness of the solution for identifying gendered language:
1. Benchmark against previous studies
2. Manually inspect predictions 
3. Assess job descriptions produced by generative AI


#### Benchmark against previous studies
First we can benchmark overall peformance against what previous studies have found in terms for the prevalence of gendered language. Through this we can see if we are identifying masculine and feminine language at similar levels, if we are then we can infer that the model developed here is identifying gendered language at rates generally accepted.

The metrics we will benchmark our model against previous studies are those already defined for each advertisement in 'Scoring advertisements above'.

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

 
### Manually inspect predictions

In addition to this, we can also perform a manual inspection of several job advertisements and the gendered language identified in them. While this does not systematically show the likely response, it will give the reader a sense of how effective the solution is at identifying language that is likely to influence readers of job advertisements.

While the above tells us how effective the model is at identifying gendered language as benchmarked against previous research, we will also benefit from an inspection of some examples of the predictions made to get a better sense of the model's performance. To do this, we inspect the top 3 masculine and feminine advertisements in terms of the gender target score.

![](assets/displacy_images/masc_1.svg)

There are several observations we can make about the job advertisements.

There appears to be what could be considered many false positives in terms of gendered language. For example, the most masculine advertisements identifies the term 'Logic' repeatedly as a masculine term. While this is gendered language, in context it is in the name of the organisation. The presence of this language may affect the sense of belongingness in the organisation (since the name represents what the organisation is about), this assumption should be tested. 

It appears there could be confusion when there is a difference in descriving the attributes of the person versus nouns. For example, the second example shows the use of the word 'lead' is used in two senses. First it describes attributes of the applicant as needing to lead. However it is also used to describe 'lead generation'. It seems like the former will be more relevant for a sense of belongingness as opposed to the latter.

There are extremely common terms that appear necessary and almost unavoidable in job advertisements. For example, 'ability'. 

Other common terms while unavoidable, could be discouraging. For example, use of the term data may make the position appear more technical. However, this perhaps should be presented as it is a requirement for ability to do the job and may not discourage females who do have a more technical bent. Could more technical skills that relate to aptitude should not change (though personal attributes/styles could be open).

The top feminine jobs interestingly show a complete absence of masculine words which maximises the gender target to be completely feminine. 


Overall, there would need to be refinement. This primarily relates to understanding when terms are used to describe the applicant or their duties versus the name of something. 


### Generative AI examples



## Overall Ethical Response
While the model developed assists with identifying gendered language, it alone isn't enough as a system to address the original ethical concern. Defining an overall ethical response identifies what further would need to be put in place to fully address the ethical concern identified.

Bias and discrimination in the recruitment process manifests in different ways. Typically the process involves: 
- an advertising phase where an employer will prepare an advertisement for a role, advertise it in their chosen medium and applicants will apply
- a selection phase where an employer will review applicants, interview a select amount and then make a final selection of who to employ

The model developed here targets the first part of the process by identifying language that can discourage applicants, however the evaluation above shows that in order to change action this would need to be supplemented in several ways.

First the solution would need to recommend alternative wording to enable those crafting job advertisements to be able to create improved wording. In addition to this, it would be ideal if the solution provided some rationale or explanation as to the effect of the specific language identified to assist with educating users so that they would be better equipped to identify this language themselves in the future.

Secondly we will need to the solution to consider not just removing masculine terms. This might result in some incomplete ads as noted above some terms are necessary.

There are a number of other measures that can be taken to create a holistic solution to mitigate bias. This includes anonymising the application process, advertise in media targeted for all audiences, increasing the use of more objective interview techniques (e.g. competence based interviews) or undertaking unconscious bias training for those who are involved in the hiring process.

## Limitations
There are a number of limitations with the solution outlines above in addressing the ethical concern identified in this discussion.

Research has found that one of the primary drivers in underlying bias about which types of jobs are more sutied for men versus women. While wording may help to soften the image of a job, the underlying biases in the individual applicants is likely enough to discourage applicants.

The analysis here does not take into account industry.

There are other types of discrimination. 

This is only punitive. It is telling people what not to say but does not help with what to say.

As noted above, it is not fully sensitive to the context in which terms are used. Sometimes the terms are used in a neutral or positive way that may no impact on belongingness (e.g. listing equal opportunity attributes which are actually positive mentions).

Gender bias can be built into word embeddings (how does this affect my solution).

There is other potentially gendered language that is not included here. This includes specifically conditional superlatives. it also includes effort based assessments.

Finally, we should consider if some jobs are gendered.

## Conclusion
To be completed.