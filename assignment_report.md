# Detecting and Addressing Biased Language in Job Advertisements


# Introduction
The goal of this assignment is to design a solution that addresses an ethical concern with an existing data science product. In doing so, we demonstrate how data science solutions can be developed to better align with desired ethical outcomes. 

This assignment is structured in three parts:
1. **Identify the ethical concern:** we identify the ethical concern this assignment seeks to address and propose a response to address this ethical concern
2. **Develop a data science response:** we develop a data science model that supports addressing the ethical concern 
3. **Ethical response assessment:** we evaluate how well the data science response addresses the ethical concern, propose an overall response that attempts to fully address the ethical concern and discuss possible avenues for future development of an overall response


# 1. Ethical concern
First we identify the ethical concern and proposed data science response that will be developed to support addressing the concern.

## Gendered language in job advertisements
Research has found that gendered language in job advertisements can affect who applies [Gaucher et. al. 2011](https://ideas.wharton.upenn.edu/wp-content/uploads/2018/07/Gaucher-Friesen-Kay-2011.pdf). This research showed that gendered language in job advertisements causes prospective applicants to have a decreased sense of belongingness in relation to the job advertised. This decreased sense of belongingness in turn decreases the appeal of the job to potential applicants, making them less likely to apply. In particular, this research found that masculine gendered language can create a decreased sense of belongingness for females while males do not appear to be impacted by feminine language.

This impacts on both individuals and employers. For individuals, it limits the perceived opportunities available for members of groups that will feel a lesser sense of belongingness in response to the language used. In effect this limits their future earning and career prospects.

For employers, producing job applications that can exclude some applicants can lead to a less diverse and talented pool of applicants to choose from in the selection process. It can also create regulatory risk where there are relevant anti-discrimination regulations and/or laws in place. Finally, it can also lead to overall negative brand perception if an organisation is perceived as biased towards/against specific genders through its use of language.

## Response
To address this concern, we would want a response that enables the production of job advertisements that do not include gendered language that reduces an applicant's sense of belongingness in relation to an advertised position.

This assignment develops a NER model to detect gendered language in job advertisements and assign a 'gender target' score indicating whether the tone is masculine, feminine, or neutral. In addition, the assignment suggests complementary interventions to create a complete system that addresses the ethical concern.


# 2. Data Science Response

In this section we outline how a NER model was developed to identify gendered language in job advertisements.

All code relating to this assignment can be found in the jupyter notebook located [here](https://github.com/Innoccull/DATA417/blob/main/job_discrimination_NER.ipynb).

## Gendered language
The research on gendered language in job advertisements referenced above defined a list of masculine and feminine terms in their study. These lists were re-used as the gendered language to identify by the NER model.

The list of masculine terms used can be found [here](https://github.com/Innoccull/DATA417/blob/main/data/masculine.csv).

The list of feminine terms used can be found [here](https://github.com/Innoccull/DATA417/blob/main/data/feminine.csv).

## Dataset
To train the proposed NER model, a dataset of job descriptions is required. For this project we chose to use the Indeed Job Posting dataset. 

This dataset was created by [PromptCloud](www.promptcloud.com) and [DataStock](datastock.shop). It contains around 30,000 records of job postings made to the U.S based website indeed.com from Aug - Oct 2019. 

The dataset was downloaded from [Kaggle](https://www.kaggle.com/datasets/promptcloud/indeed-job-posting-dataset).

## Creating model training data
To create the training data for the NER model, we took a random selection of 1000 job advertisements from the Indeed Job Posting dataset. This amount was chosen due to processing power constraints.

The job descriptions for the advertisements chosen were pre-processed to clean the data. This included removing HTML tags and pushing all text to lower case.

The resulting clean job description data were labelled for masculine and feminine terms in a gazetteer style approach. A python script was created to identify masculine and feminine words in the job descriptions based on the masculine and feminine terms lists linked above. 

The auto-labelled job descriptions were loaded to [doccano](https://github.com/doccano/doccano), an open-source data labelling tool. In doccano, there was a manual inspection of several job descriptions to check for accuracy of labelling. No inaccuracies were identified so the auto-annotations were accepted for training.

Of the 1000 jobs randomly selected and processed, 700 of these were used for training while 300 of these were used for test.


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

The gender target score is a generalized metric used in two researched studies ([Bohm et. al. 2020](https://kersting-internet.de/pdf/Boehm_Lynnik_Kohl_Weber_Teetz_Bandurka_Kesting_in_Druck_ACM_SIGMIS_GenderBias.pdf) and [Tang et. al. 2017](https://people.cs.uchicago.edu/~ravenben/publications/pdf/gender-cscw18.pdf)). It measures gender bias using a 'push-pull' score, where masculine terms are push words (discouraging) and feminine words are pull words (attracting) for applicants. The score is calculated by neutralizing feminine and masculine words, applying a sigmoid function, and producing a range of 0 to 1. A score of 0.5 indicates a neutral description, while higher scores reflect more femininity and lower scores reflect more masculinity in the advertisement.

These statistics enable more complete assessment of the gender tone of each advertisement. Advertisements with a higher percentage of masculine terms or with gender target scores that indicate a more masculine advertisement would be in greater need of intervention to address the ethical concern.



# Ethical Assessment
In this final section we perform an assessment of how we can address the original ethical concern. This is done in three parts:
1. Evaluate the performance of the NER model developed for addressing the ethical concern
2. Define an overall system for response to the ethical concern identified
3. Identify limitations of the overall system defined and potential future improvements


## Evalute solution performance
The original ethical concern is that individuals are discouraged from applying for jobs due to gendered language used in advertisements. Specifically this is the case with females being dissuaded by masculine language. The NER model developed addresses this by enabling identification of this gendered language so that it could be corrected prior to advertising the job. 

To properly assess whether this intervention addresses the original ethical concern, it would be best to test whether advertisements modified based on the gendered language identified by the model led to a higher likelihood for the target audience to apply.

A design to do this evaluation would be to:
1. Select a random sample of job advertisements.
2. Apply the NER model to identify gendered terms and score the advertisements.
3. For each advertisement, create separate masculine, feminine and neutral versions accordingly. For example, if an advertisement was scored by the model as masculine we would create separate feminine and neutral versions of it.
5. Present the masculine, feminine and neutral version of each advertisement to individuals and survey their sense of belongingness and willingness to apply for the job based on these advertisements. 

From this assessment, we would test whether females are more likely to apply for the neutral and feminine versions of the job descriptions as opposed to the masculine version. Unfortunately undertaking this assessment is beyond the scope of this assignment as it would require a large amount of effort to produce separate versions of advertisements and in sourcing participants to evaluate the advertisements. A separate approach for evaluating the solution is therefore taken in this assignment.

<br/>

As an alternative approach, we can instead evaluate how effective the NER model is at identifying gendered language. On this approach we do not understand if we have made the advertisements less likely to discourage applicants, but we do understand the extent to which it would be possible to produce improved advertisements based on modifying the language identified. If the NER model identifies, for example, too many masculine terms or the wrong masculine terms - the alternative advertisements produced based on it may not be effective. Hence understanding this aspect of the model's performance is useful.

There are three ways in which we will do this evaluation of the effectiveness of the solution for identifying gendered language:
1. Benchmark against previous studies
2. Apply the model to masculine, feminine and neutral job descriptions produced by generative AI
3. Manually inspect predictions


### Benchmark against previous studies
Benchmarking against previous studies can help assess the model's performance in identifying masculine and feminine language. If the model's identification rates are similar to rates that previous studies identified gendered language at in job advertisements, it indicates its effectiveness in detecting gendered language.

We will benchmark according to the metrics already defined for each advertisement in the [Scoring advertisements](#Scoring advertisements) section above. Below are the results of applying the NER model to a random selection of 1000 job advertisements from the Indeed Jobs dataset:
- 997 (97%) were found to have masculine words
- 996 (96%) were found to have feminine words
- The average proportion of words in an advertisement that are masculine is 2.0%
- The average proportion of words in an advertisement that are feminine is 1.5%
- The average gender target score is 0.47.

The study completed by [Gaucher et. al. 2011](https://ideas.wharton.upenn.edu/wp-content/uploads/2018/07/Gaucher-Friesen-Kay-2011.pdf) examined the prevalence of gendered language in job advertisements and its impact on prospective applicants. Their study found that the average proportion of words in a job advertisement that are masculine is approximately 1.0%. For feminine words this is 0.6%. In comparison to this, the model developed for this assignment predicts at approximately double the rate for both masculine and feminine words, suggesting that it is over-identifying the prevalence of gendered language for both masculine and feminine terms.

With regard to gender target score in previous studies, there was an average of 0.38 (Bohm) and 0.48 (Tang) found in the advertisements examined. Both these scores show a more masculine lean for the language used in job advertisements. The NER model produced for this assignment produced an average score of 0.47 which suggests an overall average neutral tone for job advertisements with a slightly masculine leaning. On this particular metric, the NER model's performance is in line with what previous studies found.

### Generative AI examples
A second way to test model performance is to use generative AI (Chat-GPT in this instance) to create masculine, feminine and neutral versions of job advertisements for three different professions (real estate, mechanic and early childhood teacher). These professions were chosen specifically as they represent largely gender neutral (real estate agent), masculine  (mechanic) and feminine (early childhood teacher) professions. We will use the gender score defined above to determine if the model is correctly scoring advertisements in line with what we expect.

The table below presents the results.

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

Within each profession the results are as expected as the masculine language gender target score is lower (i.e. more masculine) than the feminine language gender target score. However, there are a few results that are unanticipated:
- The neutral score for real estate agent is more masculine than masculine 
- The neutral score for early childhood teacher is just as masculine as masculine
- The neutral score for mechanic is more feminine than the feminine score

 
### Manually inspect predictions
Finally, we perform a manual inspection of several job advertisements as a qualitative assessment of the performance of the NER model. To do this, we inspect four job advertisements, this includes the advertisements:
- With the highest masculine and feminine percentage of words (ordered by masculine percentage then feminine percentage)
- With the highest feminine and masculine percentage of words (ordered by feminine percentage then masculine percentage)

The visualisations of these advertisements and the gendered terms identified in them can be found (to be confirmed where these will be displayed - at the moment they are in the jupyter notebook). There are a few observations we can make about the job advertisements .

</br>

There appears to be what could be considered many false positives in terms of gendered language identified. For example, the most feminine advertisement identifies the term 'service' repeatedly as a feminine term. While this is gendered language, in context it is in the name of the department the individual would be working in. While the presence of this language may still affect the sense of belongingness in the organisation, this assumption should be tested since the term refers to the department and not specifically attributes of the potential applicants or skills required for the role. 

Another example of this is where the word 'lead' is used in two senses. First it describes attributes of the applicant as needing to lead. However it is also used to describe 'lead generation'. It seems like the former where it is used to describe the desired attribute will be more relevant for a sense of belongingness as opposed to the latter where it is used to .

A second observation is that sometimes the gendered terms are used in a positive light. (To include exmaple).

From these observations, it is clear that there could be further attention paid to the context in which the gendered terms are being used in an advertisement. The model could be refined so that when a term is used in positive light or is used as a noun to describe a concept or inanimate 'thing' (as opposed to describing desirable attributes of the applicant), it is not predicted as gendered language that could affect the sense of belonginginess.

### Conclusion on model performance

Overall the model performs reasonably well in identifying gendered language. The scores at which it identifies gendered language is within what is generally observed, in addition to this the model predicted largely in line with what would be expected for the advertisements created through generative AI. It is evident though that some fine-tuning of the model predictions will be required to be more precise in the language that is identified as gendered. 

The need to fine tune is evident in the fact that some of the rates of identifying masculine and feminine language is higher and the fact that there appears to be several exmaples of false positives. The model should be enhanced to be more sensitive to the context in which masculine and feminine terms are used so that they are not labeled as gendered when they are used in a positive sense or when they are describing the name of some 'thing' (as opposed to attributes of the applicant).


## Overall Ethical Response
While the model developed assists with identifying gendered language, it alone isn't enough as a system to address the original ethical concern. Defining an overall response requires that we identify what further would need to be put in place around the model to fully address the ethical concern identified. This acknowledges that data science solutions are more than just the model. Instead they are supporting tools that need to be understood as one part of an overall system and must therefore be complemented with other interventions.

In this section, we put forward an overall system design for addressing gendered language in job advertisements. In this design we design not only to efficiently address the ethical concern but also ensure to take into account the responsible AI design principles transparency, fairness, accountability and privacy.

<br/>

Typically the recruitment process involves: 
- an **advertising phase** where an employer will prepare an advertisement for a role, advertise it in their chosen medium and applicants will apply
- a **selection phase** where an employer will review applicantions, interview a select amount and then make a final decision of who to employ

Bias and discrimination against groups can manifest in different ways throughout the process. We therefore consider a design 

### Advertising phase
The model developed here targets the advertising phase by identifying language that can discourage applicants. However, identifying the language in itself is not enough. The model should also recommend alternative wording to enable those crafting job advertisements to be able to create improved wording. To create the desired change in action it is not enough to tell people what is wrong, we should also make it as easy as possible to take corrective action by providing these suggestions. 

In addition to this, it would be ideal if the solution provided some rationale or explanation as to the effect of the specific language identified. Providing a rationale may make it more likely for individuals to take action if they understand the 'why' behind the suggested change. This will also assist with educating users so that they would be better equipped to identify this language themselves in the future, putting them in a position to prevent its entry into job advertisements in the future. 

Finally, we would want to integrate use of the model into existing tools that individuals use to craft job advertisements. This could in practice, for example, involve integrating its use into a product like Microsoft Word so that users can receive instant feedback. Alternatively it could involve exposing the model via an API (Application Programming Interface) so existing products could choose to leverage its capabilities within existing workflows. This would remove another barrier to addressing the ethical concern. Requiring users to run advertisements through a separate tool would create an extra step in their process and could discourage them from checking.

Outside of enhancing the model to make it more usable, consideration during the advertising phase should be given to where the job advertisements are posted. While the data science solution will improve the wording of the advertisement, it will need to be read by those who are targeted. Consideration should therefore be given to advertising in media and for durations that are likely to reach a wide pool of diverse candidates.


### Selection phase
There are a number of other measures that can be taken to create a holistic solution to mitigate bias during the selection phase. This is important for an overall solution as while our model will support encouraging a more diverse pool of applicants through the advertising phase, we must make sure downstream actions in the slection phase do not undermine this. Interventions that can be made at this stage include:
- anonymising the application process so that unconscious biases cannot creep into decision making
- increasing the use of more objective interview techniques (e.g. competence based interviews) so that assessments of suitability are made as objectively as possible on competence as opposed to identity
- undertake unconscious bias training for those who are involved in the hiring process so that these biases around the identity of applicants have a lower likelihood of being part of the decision making



### Responsible AI
Responsible AI design requires that we should design models that are transparent, fair, accountable, and respect prviacy/security. Here we incldue some additional design features to ensure that the proposed system aligns with these responsible AI principles. 

**A human in the loop**
It is often advisable that there is a 'human in the loop' in the use of an AI system. This ensures firstly that there is a check on the model's recommendations, there can be a human sanity check on what the model is producing as opposed to blindly following recommendations. In addition to this it provides an element of accountability in the design whereby a human is ultimately making the decision on language used in the advertisement. 

Within our system, we can include that a human would review and correct gendered language in advertisements based on the information presented to them. We would also ideally be able to present to the human reviewer the gendered language, why that language was identified and a suggested replacement. The human could decide what to update and what not to update based on the model's recommendations.

**Explaining model predictions**
To promote transparency, we will want to be able to clearly explain model predictions. In the context of this assignment, this will involve clearly explaining why language has been identified as gendered and how that gendered language would impact on individuals. 

This can be achieved in two ways. Firstly a library such as SHAP or LIME could be used to generate explanations for predictions. These libraries will provide an overview of the important features and their relative weighting for predictions made. In the context of NER, this will show which of the surrounding words influenced the prediction and their relative weights.

In addition to this, it may be possible to produce a knowledge base that allows for explanation of the way in which a gendered term can impact on job advertisements. For example, some words might impact through reinforcing underlying gender stereotypes for professions and be accompanied with such an explanation when identified as gendered.

**Model monitoring**
Finally we will want to include monitoring of the model to help promote transparency and continued improvement of the model's prediction through feedback. Monitoring of the model could include:
- Measure the amount of times that a user takes the advice of the model and rejects the advice of the model so that we can understand whether the advice presented is useful to users
- Measure the gender target score before and after user updates based on model advice so that we can see that the model is producing improved advertisements
- Measure the profile of applicants according to the gender target score so that we can understand if more feminine gender target scores 

### Overall solution design
The image below provides an overall view of the solution design, taking into account all the design considerations above.

![](/assets/overall_solution.jpg)

#### Web Application
A web application proof of concept was developed to demonstrate the model. This web application can be accessed at the link below.
http://databa.pythonanywhere.com/

The web application presents the user with the ability to enter the text for a job advertisement.

![](/assets/web_app.jpg)

Upon selecting 'Run Model', the user is presented with the masculine and feminine entities identified in the text provided and some core statistics relating to the advertisement.

![](/assets/web_app_example_entry.jpg)



## Limitations
There are several limitations with the solution outlined above iwhen it comes to addressing the ethical concern identified for this project. It is important that we identify and acknowledge these, as they can inform how the solution might be applied in practice and can also identify avenues for further development of the solution.

First and most notable is that research has acknowledged that when assessing whether or not to apply for a job, one of the strongest drivers is existing biases and perceptions about the gender that the profession is primarily associated with. While wording may help to soften the image of a job, the underlying biases in the individual applicants is likely enough to discourage applicants regardless of how wording is improved.

Another limitation in addressing the overall ethical concern is that there are other types of language in advertisements that may discourage applicants in a discriinatory way (e.g. age, disability). It would be best if future iterations of this approach to improving job advertisements took into account and mitigated these other types of discrimination that can emerge in job advertisement language.

There are also several model specific limitations that should be considered (and which were already touched on above):
- The model as developed is only punitive in the sense that it identifies the gendered language but does not provide suggested improvements. Future iterations should provide advice on which gendered language to replace and what to replace it with.
- The model is not fully sensitive to the context in which terms are used. Sometimes gendered terms are used in a neutral or positive way that may not impact on perceptions of belongingness (e.g. listing equal opportunity attributes which are actually positive mentions). The training of the model could be refined to not identify these terms as needing corrective action.
- Gender bias can be built into the word embeddings used in the model.
- There is other potentially gendered language that is not included here that could be included in the model (for example, the use of conditional superlatives)  

Finally, an important limitation is whether it is the case that some jobs simply do require gendered language to accurately describe the requirements of the job. For example, the term 'data' is described as a masculine term so is identified as such in job advertisements. This, however, leads to many jobs being scored as heavily masculine when they are describing reasonable expectations for the role which, if removed, would inhibit the advertiser's ability to properly represent the role. If we accept that gendered language is necessary for some job descriptions to be accurate, then this places a hard constraint on what it can achieve as some language cannot be changed (even when identified).

To manage this, there will need to be at the very least a human in the loop to make an assessment of if the suggested changes undermine one of the core purpose of the job advertisement, accurately describe the role. However, ideally the model itself could be sensitive to this so that these suggestions were not made in the first place. This approach would be preferred so that confidence was maintained in the model. A model that makes suggestions which humans need to correct will not engender trust and confidence, undermining its potential use in the future.


## Conclusion
Gendered language in job advertisements can impact on both individuals and employers in a negative way. This assignment has created an NER model to identify gendered terms and proposed a design for an overall system that utilises this model to address the original ethical concern. This overall system proposes improvements to the model and non-technology interventions in the recruitment process to mitigate bias. The design also incorporates responsible AI design features. Some of the key features of this overall solution are: 
- Enhancing model predictions to be more sensitive to the context in which masculine and feminine terms are used
- Enhancing the model to provide recommendations for alternative wording
- Incorporating the model recommendations into existing workflows for creating job advertisements
- Providing model explanations so that users are more likely to understand and accept recommendations
- Placing the improved advertisements in appropriate media for reaching a diverse audience
- Removing bias in the selection phase through blind selection, competency based interviews and unconscious bias training
- On-going model monitoring to understand its overall performance and acceptance by end users


Finally, in this assignment we considered several limitations of the model. Many of these relate to model enhancements already considered (i.e. making recommendations), however two of the limitations do place a hard limit on what the proposed solution can achieve. The first of these is that the strongest factor influencing a sense of belongingness (and therefore likelihood to apply) are gender stereotypes about which types of roles are suited to which genders. The second of these is that some gendered language may be necessary for accurately advertising the position, and that changing this gendered language may create misleading/inaccurate job advertisements. While these limitations do not prevent the solution from making a difference, they are factors that we should take into account to be realistic about what the solution can achieve.

</br>

Overall, there is potential through a data science solution to address the discrimination that can be embedded in job advertisements through gendered language. While there are some hard limitations on what can be achieved, it would be possible through an improved model and process to make a difference.
