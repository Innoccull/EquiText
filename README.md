# Detecting and Addressing Bias in Job Advertisements


# Introduction
Ethics is critically important for data scientists because the data science solutions they develop can have wide-ranging implications for society, individuals, and businesses. Ethics provides a framework for data scientists to ensure that the work they do and the solutions they produce are responsible, transparent, and socially acceptable.

The goal of this assignment is to design a solution that addresses an ethical concern with an existing data science product. In doing so, we demonstrate how data science solutions can be developed to better align with desired ethical outcomes. 

This assignment is structured in three parts:
1. **Identify the ethical concern:** we identify the ethical concern this assignment seeks to address and propose a response to address this ethical concern
2. **Develop a data science response:** we develop a data science model that supports addressing the ethical concern 
3. **Ethical response assessment:** we evaluate how well the data science response addresses the ethical concern, propose an overall response that attempts to fully address the ethical concern and discuss possible avenues for future development of an overall response


# Ethical concern
First we identify the ethical concern and proposed data science response that will be developed to support addressing the concern.

## Discriminatory language in job advertisements
Research has found that gendered language in job advertisements can affect who applies [Gautier 2011](https://ideas.wharton.upenn.edu/wp-content/uploads/2018/07/Gaucher-Friesen-Kay-2011.pdf). This research showed that gendered language in job advertisements causes prospective applicants to have a decreased sense of belongingness in relation to the job advertised. This decreased sense of belongingness in turn decreases the appeal of the job to potential applicants, making them less likely to apply. In particular, this research found that masculine gendered language can create a decreased sense of belongingness for females while males do not appear to be impacted by feminine language.

This impacts on both individuals and employers. For individuals, it limits the perceived opportunities available for members of groups that will feel a lesser sense of belongingness in response to the language used. In effect this limits their future earning and career prospects.

For employers, producing job applications that can exclude some applicants can lead to a less diverse and talented pool of applicants to choose from in the selection process. It can also create regulatory risk where there are relevant anti-discrimination regulations and/or laws in place. Finally, it can also lead to overall negative brand perception if an organisation is perceived as biased towards/against specific genders through its use of language.

## Response
To address this concern, we would want a response that enables the production of job advertisements that do not include gendered language that reduces an applicant's sense of belongingness in relation to an advertised position.

This assignment develops a named entity recognition (NER) model to detect gendered language in job advertisements and assign a 'gender target' score indicating whether the tone of the advertisement is more masculine, feminine, or neutral. However, this model alone is not enough to create the change in real-world action required to address the ethical concern. This assignement therefore will also therefore consider further interventions beyond that can be made alongside the model to create a complete system that addresses the ethical concern identified.


# Data Science Response

In this section we outline how a named entity recognition model was developed to identify gendered language in job advertisements.

## Gendered language
The research on gendered language in job advertisements referenced defined a list of masculine and feminine terms in their study. These lists were re-used for training the NER model.

The list of masculine terms used can be found [here](https://github.com/Innoccull/DATA417/blob/main/data/masculine.csv).

The list of feminine terms used can be found [here](https://github.com/Innoccull/DATA417/blob/main/data/feminine.csv).

## Dataset
To train an NER model, a dataset of job descriptions is required. For this project we chose to use the Indeed Job Posting dataset. 

This dataset was created by [PromptCloud](www.promptcloud.com) and [DataStock](datastock.shop). It contains around 30,000 records of job postings made to the U.S based website indeed.com from Aug - Oct 2019. 

The dataset was downloaded from [Kaggle](https://www.kaggle.com/datasets/promptcloud/indeed-job-posting-dataset).

## Creating model training data
To create the training data for the NER model, we took a random selection of 1000 job advertisements from the Indeed Job Posting dataset. This amount was chosen due to processing power constraints.

The job descriptions for the advertisements chosen were pre-processed to clean the data. This included removing HTML tags, pushing all text to lower case and removing URLs.

The resulting clean job description data were labelled for masculine and feminine terms in a gazetteer style approach. A python script was created to identify masculine and feminine words in the job descriptions based on the masculine and feminine terms lists linked above. 

The auto-labelled job descriptions were loaded to [doccano](https://github.com/doccano/doccano), an open-source data labelling tool. In doccano, there was a manual inspection of several job descriptions to check for accuracy of labelling. No inaccuracies were identified so the auto-annotations were accepted for training.

Of the 1000 jobs randmly selected, 700 of these were used for training while 300 of these were used for test.


## Model training and performance
A custom NER model was trained using [spaCy](https://spacy.io/).

The model was trained to recognise masculine and feminine terms as labelled in the training data. A summary of the model performance is provided below.

|           | Masculine | Feminine | Overall |
|-----------|-----------|----------|---------|
| Precision | 0.99      | 0.99     | 0.99    |
| Recall    | 0.98      | 0.99     | 0.98    |
| F-Score   | 0.99      | 0.99     | 0.99    |

We can see that the model performs extremely well at identifying the gendered language in job advertisements based on the training and test data provided.

## Scoring advertisements
Several gender scoring statistics were calculated for each job advertisement based on the gendered terms identified. These include:
- the total masculine terms identified in the advertisement
- the total feminine terms identified in the advertisement
- the percentage of words in the job description that are masculine
- the percentage of words in the job description that are feminine
- a gender target score

These statistics enable more complete assessment of the gender tone of each advertisement. Advertisements with a higher percentage of masculine terms or with gender target scores that indicate a more masculine advertisement would be in greater need of intervention to address the ethical concern.



# Ethical Assessment
In this final section we perform an assessment of how we can address the original ethical concern. This is done in three parts:
1. Evaluate the performance of the data science model developed for addressing the ethical concern
2. Define an overall system for response to the ethical concern identified
3. Identify limitations of the overall system defined and potential future improvements


## Evalute solution performance
The original ethical concern is that individuals are discouraged from applying for jobsdue to gendered language used in the advertisement. Specifically this is the case with females being dissuaded by masculine language in job advertisements. The data science solution developed addresses this by enabling identification of this gendered language through an NER model so that it could be corrected prior to advertising the job. 

To properly assess whether this intervention addresses the original ethical concern, it would be best to test whether advertisements modified based on the gendered language identified by the model led to a higher likelihood for the target audience to apply. This is the approach taken in several other pieces of research.

A design to do this evaluation would be to:
1. Select a sample of job advertisements
2. Apply the NER model to identify gendered terms and score accordingly
3. Select the most masculine job advertisements
4. Create separate masculine, feminine and neutral versions of these job advertisements
5. Present these to individuals and survey their sense of belongingness and willingness to apply to these advertisements

From this assessment, we would test whether individuals are more likely to apply for the neutral and feminine versions of the job descriptions as opposed to the masculine version. Unfortunately step 5 is beyond the scope of this assignment as it would require sourcing participants to evaluate the advertisements. A separate approach for evaluating the solution is therefore taken in this assignment.

<br/>

As an alternative approach, we can instead measure how effective the NER model is at identifying gendered language. On this approach we do not understand if we have made the advertisements less likely to discourage applicants, but we do understand the extent to which it would be possible to produce improved advertisements based on modifying the language identified. If the NER model identifies, for example, too many masculine terms or the wrong masculine terms - the alternative advertisements produced based on it may not be effective.

There are three ways in which we will do this evaluation of the effectiveness of the solution for identifying gendered language:
1. Benchmark against previous studies
2. Manually inspect predictions
3. Apply the model to job descriptions produced by generative AI


#### Benchmark against previous studies
First we can benchmark overall peformance against what previous studies have found in terms for the prevalence of gendered language. In this benchmarking we can see if we are identifying masculine and feminine language at similar levels, if we are then we can infer that the model developed here is identifying gendered language at rates generally accepted.

We will benchmark our model against previous studies according to the metrics already defined for each advertisement in the 'Scoring advertisements above' section. Below are the results of applying the NER model to a random selection of 1000 job advertisements from the Indeed Jobs dataset:
- NNNN (97%) were found to have masculine words
- NNNN (100%) were found to have feminine words
- NNNN (X%) were found to have more masculine words than feminine words
- The average proportion of words in an advertisement that are masculine is 1.3%
- The average proportion of words in an advertisement that are feminine is 1.2%
- The average gender target score is 0.38.

The study completed by Gaucher et. al. 2011 examined the prevalence of gendered language in job advertisements and its impact on prospective applicants. Their study found that the average proportion of words in a job advertisement that are masculine is approximately 1.0%. For feminine words this is 0.6%. In comparison to this, the model developed for this assignment predicts somewhat in line with the expected average percentage for masculine words (1.0%). However, the model performs differently for feminine words where it predicts at twice the rate (1.2%), suggesting it is potentially over identifying feminine language in job advertisements.

The gender target score is a generalized metric used in two researched studies (Bohm et. al. and Tang et. al.). It measures gender bias using a 'push-pull' score, where masculine terms are push words (discouraging) and feminine words are pull words (attracting) for applicants. The score is calculated by neutralizing feminine and masculine words, applying a sigmoid function, and producing a range of 0 to 1. A score of 0.5 indicates a neutral description, while higher scores reflect more femininity and lower scores reflect more masculinity in the advertisement.

For the referenced studies, there was an average score of 0.38 (Bohm) and an average of 0.48 (Tang). Both these scores show a more masculine lean for the language used in job advertisements. The algorithm produced for this assignment produced an average score of 0.506 which suggests an overall average neutral tone for job advertisements. This logically follows from the previous assessment where feminine words appear to being more commonly identified which could be pulling the model average to be more neutral overall.

In addition, the study by Bohm et. al also examined the most common masculine and feminine key words in advertisement, which provides a final benchmark to assess against. The table below is reported in the study referenced and shows the most common masculine and feminine words and the proportion of identified words they make up out of all words identified.

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

We see that there is overlap in the use of the term 'ability' however remaining words do not appear to overlap.

 
### Manually inspect predictions

A manual inspection of several job advertisements will give us a better sense of the performance of the NER model. To do this, we inspect the top ?masculine and feminine advertisements in terms of the gender target score and draw conclusions on model performance based on observations of these.

<br/>

![](assets/displacy_images/masc_1.svg)
**Masculine**
There are several observations we can make about the job advertisements.

There appears to be what could be considered many false positives in terms of gendered language. For example, the most masculine advertisements identifies the term 'Logic' repeatedly as a masculine term. While this is gendered language, in context it is in the name of the organisation. The presence of this language may affect the sense of belongingness in the organisation (since the name represents what the organisation is about), this assumption should be tested. 

It appears there could be confusion when there is a difference in descriving the attributes of the person versus nouns. For example, the second example shows the use of the word 'lead' is used in two senses. First it describes attributes of the applicant as needing to lead. However it is also used to describe 'lead generation'. It seems like the former will be more relevant for a sense of belongingness as opposed to the latter.

There are extremely common terms that appear necessary and almost unavoidable in job advertisements. For example, 'ability'. 

Other common terms while unavoidable, could be discouraging. For example, use of the term data may make the position appear more technical. However, this perhaps should be presented as it is a requirement for ability to do the job and may not discourage females who do have a more technical bent. Could more technical skills that relate to aptitude should not change (though personal attributes/styles could be open).


**Feminine**
The top feminine jobs interestingly show a complete absence of masculine words which maximises the gender target to be completely feminine. 


Overall, there would need to be refinement. This primarily relates to understanding when terms are used to describe the applicant or their duties versus the name of something. 


### Generative AI examples
Finally, to test model performance we use generative AI (Chat-GPT) to create masculine, feminine and neutral versions of job advertisements for three different professions (real estate, mechanic and early childhood teacher). These professions were chosen specifically as they represent largely gender neutral (real estate agent), masculine  (mechanic) and feminine (early childhood teacher) professions. We will use the gender score defined above to determine if the model is correctly scoring advertisements in line with what we expect.

The table below presents the results.

| Job Type                | Language Type | Gender target Score |
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



### Conclusion on model performance

Overall, this benchmarking assessment shows that for masculine terms the NER model developed performs in line with expectations set in previous studies. It identifies these terms at a similar rate to previous studies and there is overlap in the most commonly identified term and the proportion it makes up of all identified terms. However, this assessment also indicates that the model is potentially over-identifying feminine terms. We can see that the rate at which feminine terms is being identified is higher and the gender target score leans more feminine. In practice, this may mean that the model might falsely show that an advertisement is not going to discourage applicants when it might do so, due to the fact that it may be identifying terms as feminine leaning when it shouldn't. A manual inspection of the most masculine and feminine advertisements may shed some light on this.

## Overall Ethical Response
While the model developed assists with identifying gendered language, it alone isn't enough as a system to address the original ethical concern. Defining an overall response requires that we identify what further would need to be put in place around the model to fully address the ethical concern identified. This acknowledges that data science solutions alone are often not enough to create the change in the world we want to see, but rather are supporting tools that need to be complemented with other interventions that form a whole system of intervention.

In this design, we ensure to take account of and follow the responsible AI design principles of transparency, fairness, accountability and privacy.

<br/>

Bias and discrimination in the recruitment process manifests in different ways. Typically the process involves: 
- an advertising phase where an employer will prepare an advertisement for a role, advertise it in their chosen medium and applicants will apply
- a selection phase where an employer will review applicants, interview a select amount and then make a final selection of who to employ

### Advertising phase
The model developed here targets the advertising phase by identifying language that can discourage applicants. However, identifying the language in itself is not enough in this page. The model also should recommend alternative wording to enable those crafting job advertisements to be able to create improved wording. To create the achange in action, it is not enough to tell people what is wrong we should also make it as easy as possible to take corrective action by providing these suggestions. In addition to this, it would be ideal if the solution provided some rationale or explanation as to the effect of the specific language identified. Providing a rationale may make it more likely for individuals to take action if they understand the 'why' behind the suggested change. This will also assist with educating users so that they would be better equipped to identify this language themselves in the future, putting them in a position to prevent its entry into job advertisements in the future. Finally, we would want to integrate use of the model into the tools that individuals use to craft job advertisements. This could in practice, for example, involve integrating its use into a product like Microsoft Word so that users can receive instant feedback. This would remove another barrier of having to potentially run advertisements through a separate tool, which would create an extra step in the process for users and could discourage them from checking.

Outside of enhancing the model to make it more likely gendered language will be corrected, consideration during this phase should be given to where the job advertisements are posted. While the data science solution will improve the wording of the advertisement, it will need to be read by those who are targeted. Consideration should therefore be given to advertising in a location and for a duration that is likely to reach a wide pool of diverse candidates.



### Selection phase
There are a number of other measures that can be taken to create a holistic solution to mitigate bias during the selection phase. Such interventions include:
- anonymising the application process so that unconscious biases cannot creep into decision making 
- increasing the use of more objective interview techniques (e.g. competence based interviews) so that assessments of suitability are made as objectively as possible on competence as opposed to identity
- undertake unconscious bias training for those who are involved in the hiring process so that these biases around the identity of applicants have a lower likelihood of being part of the decision making

</br>

### Unanticipated consequences
The application of a model in practice can look different. Responsible AI design requires that we should try to anticipate the consequences/impacts of applying the model in practice and try to miigate any undesirable impacts in our design. 

How do we make sure that the application of the model is ethical? There are standard problems that emerge when implementing data science solutions that undermine their performance, we should consider how to address these.
- Making sure people don't blindly follow the model
- Measuring whether the model is actually increasing the pool of diverse applicants
- How can we prevent people trying to cheat the model by providing a sanitised job description but not caring about the remainder of the process?


## Limitations
There are several limitations with the solution outlined above in addressing the ethical concern identified for this project. It is important that we identify and acknowledge these, as they can inform how the solution might be applied in practice and can also identify avenues for further development of the solution.

First and most notable is that research has found that one of the primary drivers in underlying bias about which types of jobs are more sutied for men versus women. When assessing whether or not to apply for a job, one of the strongest drivers is existing biases and perceptions about the gender that the profession is primarily associated with. While wording may help to soften the image of a job, the underlying biases in the individual applicants is likely enough to discourage applicants regardless.

Another limitation in addressing the overall ethical concern is that there are other types of discrimination (e.g. age). It would be best if future iterations of this approach to improving job advertisements took into account and mitigated these other types of discrimination that can emerge in job advertisement language.

Finally there are several model specific limitations that should be considered:
- The model as developed is only punitive in the sense that it identifies the gendered langugage but does not provide suggested improvement. Future iterations shold provide advice on which gendered language to replace and what to replace it with.
- The model is not fully sensitive to the context in which terms are used. Sometimes gendered terms are used in a neutral or positive way that may not impact on perceptions of belongingness (e.g. listing equal opportunity attributes which are actually positive mentions). The training of the model could be refined to not identify these terms as needing corrective action.
- Gender bias can be built into word embeddings (how does this affect my solution).
- There is other potentially gendered language that is not included here. This includes specifically conditional superlatives. it also includes effort based assessments.

Finally, we do need to consider if some jobs simply do require a gendered description to accurately describe the requirements of the job and if moving away from the gendered language identified would undermine the advertisers ability to accurately describe the demands of the job. For example, the term 'data' is described as a masculine term so is identified as such in job advertisements. This, however, leads to many jobs being scored as heavily masculine when they are describing reasonable expectations for the role which, if removed, would inhibit the advertiser's ability to properly represent the role. There will need to be at the very least a human in the loop to make an assessment of if the suggested changes undermine the integrity of the lanaguage. However, ideally the model itself could be sensitive to this so that these suggestions were not made in the first place. This approach would be preferred so that confidence was maintained in the model. A model that makes suggestions which humans need to correct will not engender trust and confidence, undermining its potential use in the future.

## Conclusion
Gendered language in job advertisements can impact on both individuals and employers in a negative way. This assignment has leveraged natural language processing to identify gendered terms and suggested design for an overall system that utilises this model to address the original ethical concern. 

The model identifies gendered language in advertisement 

There is room for future improvement of the model, including:
- Providing recommendations for alternative wording
- Being more sensitive to the context in which masculine and feminine terms are used
- Taking into account a wider range of terms
= Weighting terms
- Further?

Finally, there are limitations to note. These are them. But remember, this is indicative of technology solutions are no the be all and end all. 