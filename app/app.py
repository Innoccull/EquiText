# import libraries
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html

import spacy
from spacy import displacy
import pandas as pd
import math
import os

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)


dirname = os.path.dirname(__file__)
model_path = os.path.join(dirname, 'ner_model/ner_model')

# Load model
nlp = spacy.load(model_path)

# Settings for producing displacy images
colors = {"MAS": "linear-gradient(120deg, #a1c4fd, #a1c4fd)", "FEM": "linear-gradient(120deg, #fdcbf1, #fdcbf1)"}
options = {"ents": ["MAS", "FEM"], "colors": colors}

# Function to get spacy doc summary stats
def get_doc_stats(doc):

    total_tokens = doc.__len__()

    total_masculine = len([ent.text for ent in doc.ents if ent.label_ == "MAS"])
    total_feminine = len([ent.text for ent in doc.ents if ent.label_ == "FEM"])

    n = total_feminine + total_masculine

    if (n == 0):
        gt_score = 0.5
    else:
        x = (1/n)*(total_feminine - total_masculine)
        gt_score = 1/(1+math.exp(-x))


    result = {
        'Total words': total_tokens,
        'Total masculine words': total_masculine,
        'Total feminine words': total_feminine,
        'Percentage masculine words': round(total_masculine/total_tokens, 4),
        'Percentage feminine words': round(total_feminine/total_tokens, 4),
        'Masculine words': [ent.text + ", " for ent in doc.ents if ent.label_ == "MAS"],
        'Feminine words' : [ent.text + ", " for ent in doc.ents if ent.label_ == "FEM"],
        'Gender Target Score' : gt_score
    }

    return result

app.layout = dbc.Container(
    [
    dbc.Navbar(
        children=
        [
            dbc.NavbarBrand("EquiText", class_name="lg-1"),
            dbc.Col(dbc.Button("About", id="btn-about", color="white", n_clicks=0, style={'float' : 'right'}))
        ],
        color="white",
        style={'width' : '100%'}
        )
    ,
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("About EquiText")),
            dbc.ModalBody(
                children =[
                    html.P("Research shows that gendered language in job advertisements can discourage applicants from applying, reducing the pool of talent that employers will attract."),
                    html.P("EquiText uses Natural Language Processing to identify gendered text in advertised and provide an overall 'gender targer score' for advertisements."),
                    html.P("This enables employers to identify where their job advertisements might impact the applicants who apply, and make the choice as to whether they should adapt their advertisements before posting."),
                    html.Br(),
                    html.P("Contact: chrisrodgersba@gmail.com")
                ]
                ),
            dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="modal-close", className="ms-auto", n_clicks=0
                    )
                )
        ],
        id="modal-about",
        size="lg",
        is_open=False,
    ),
    html.Div(
        children=[
            dbc.Textarea(id="job_description", size="lg", placeholder="Enter a job description here", style={'margin' : '50px 0px 10px 0px', 'font-family' : 'sans-serif', 'height' : '200px'})
            ],
        style={}
        ),
    dbc.Button("Run EquiText", id="run_model", color="light", className="me-1", style={}),
    html.Hr(),
    dbc.NavbarSimple(
        children=
        [
            dbc.Button("Show/Hide", id="btn-output", color="white", n_clicks=0)
        ],
        brand="Language Identified",
        color="white",
        style={'width' : '100%'}
        ),
    dbc.Collapse(
        html.Div(id='displacy-image'),
        id="collapse-output",
        is_open=False
        ),
    dbc.NavbarSimple(
        children=
        [
            dbc.Button("Show/Hide", id="btn-stats", color="white", n_clicks=0)
        ],
        brand="EquiText Results",
        color="white",
        style={'width' : '100%'}
        ),
    dbc.Collapse(children=
        [
            html.Div(id='table')
        ],
        id="collapse-stats",
        is_open=True
        ),
    dbc.Button("What do these results mean?", id="btn-results", color="white", n_clicks=0, style={'float' : 'right'}),
    dbc.Modal(
        [
            dbc.ModalHeader(dbc.ModalTitle("About EquiText Results")),
            dbc.ModalBody(
                children =[
                    html.P("EquiText results inform you of gendered language present in the text provided."),
                    html.P("In addition to the actual gendered terms identified in the text, EquiText provides you with a Gender Target Score."),
                    html.P("The Gender Target Score is a representation of the overall gender 'balance' of the text provided. A score of 0.5 means that the text is balanced between masculine and feminine, a score close to 0 is more masculine and a score closer to 1 is more feminine."),
                    html.Br(),
                    html.P("The EquiText results can be used to refine your job advertisement to change how it might be perceived by propsective applicants. Gendered terms (masculine or feminine) can be removed or added to tweak the overall Gender Target Score and subsequently how effective the article might be at attracting specific applicants."),
                    html.P("It is important that you consider what balance and overall language will be most important in your context. There is no 'right' answer to what the Gender Target Score or terms used should be. The EquiText results presented here can help you to better achieve the goals you have defined for yourself as relevant to your particular context.")
                ]
                ),
            dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="result-close", className="ms-auto", n_clicks=0
                    )
                )
        ],
        id="modal-results",
        size="lg",
        is_open=False,
    ),
    ]
)

#open and close 'about' modal
@app.callback(
    Output("modal-about", "is_open"),
    [Input("btn-about", "n_clicks"), Input('modal-close', 'n_clicks')],
    State("modal-about", "is_open"),
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("collapse-output", "is_open"),
    [Input("btn-output", "n_clicks")],
    [State("collapse-output", "is_open")],
)
def toggle_collapse_output(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("collapse-stats", "is_open"),
    [Input("btn-stats", "n_clicks")],
    [State("collapse-stats", "is_open")],
)
def toggle_collapse_stats(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(Output('displacy-image', 'children'),
              Input('run_model', 'n_clicks'),
              State('job_description', 'value'))
def update_displacy(n_clicks, value):
    if n_clicks is not None:

        # Create doc object
        text = value

        text = text.replace('\n', ' ')

        doc = nlp(text)

        # Create displacy visualisation
        html_doc = displacy.render(doc, style="ent", options=options)

        disp = dcc.Markdown([html_doc], dangerously_allow_html=True)

        return (disp)

@app.callback(Output('table', 'children'),
              [Input('run_model', 'n_clicks'),
              State('job_description', 'value')])
def update_table(n_clicks, value):

    if n_clicks is not None:

        # Create doc object
        text = str(value)

        doc = nlp(text)

        data=get_doc_stats(doc)

        df = pd.json_normalize(data)
        df = df.transpose()
        df = df.reset_index()
        df.columns = ["Result", "Value"]

        return (dbc.Table.from_dataframe(df))

#open and close 'results' modal
@app.callback(
    Output("modal-results", "is_open"),
    [Input("btn-results", "n_clicks"), Input('result-close', 'n_clicks')],
    State("modal-results", "is_open"),
)
def toggle_results_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server()