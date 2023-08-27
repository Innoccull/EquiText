# EquiText

Research shows that gendered language in job advertisements can discourage individuals from applying, reducing the pool of talent available to advertisers. EquiText is a Natural Language Processing model that identifies gendered terms in job advertisemetns and assigns an overall gender target score to the advertisement based on the terms identified. 

EquiText enables employers to understand how their job advertisements could be perceived by applicants and choose whether or not to adapt the language used in their advertisement accordingly, thereby increasing the likelihood of a larger and more diverse talent pool to choose from when advertising.

EquiText can be used [here](http://databa.pythonanywhere.com/).

</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>
</br>

---

**Background**

EquiText was developed as an assignment for the course DAT417 - The Trustworthy Data Scientist, completed as part of a Master of Applied Data Science at the University of Canterbury, New Zealand.

The assignment called for addressing an ethical concern with the use of a data science solution. The solution developed was a named entity recognition model that detects and highlights gendered lamguage in job advertisements so that they can potentially be adjusted. Previous research has shown that gendered language in job advertisements can discourage applicants from applying, leading to a less diverse candidate pool for employers to choose from and missed opportunities for individual applicants.

The solution developed includes:
- a named entity recognition model developed with spaCy that identifies if a term is masculine or feminine in the context of job advertisements
- a plotly Dash web application that allows users to enter text and be presented a visualisation and statistics about the text (e.g. number of masculine/femining words, an overall gender target score)


assignment_report.md provides a full account of the development and evaluation of the solution for the assignment, including:
- a summary of the research on the effect gendered language in job advertisements has
- the approach taken for developing the solution
- how the effectiveness of the solution was assessed
- consideration of what beyond the named entity recognition should be implemented to address the ethical concern

The model card for EquiText can be viewed [here](https://github.com/Innoccull/identifying_gendered_language/blob/main/model_card.md).
