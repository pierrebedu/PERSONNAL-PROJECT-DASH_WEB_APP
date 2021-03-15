# pip install dash dash-renderer dash-core-components dash-html-components plotly

import datetime
import dash
import dash_core_components as dcc  # graphs, ...
import dash_html_components as html #tags,...
from dash.dependencies import Input, Output
from pandas_datareader import data

app = dash.Dash() #creates the standalone app (it's a flask app)

#sort of "html" agencement of the entire project
app.layout = html.Div(                                #html Div contains everything
    children=[   
                                     # inside a list. List of children. Each has a tag           
    html.H1('Ma première web app avec Dash :'),
    html.H2("Choisissez un nom d'action ci dessous : IBM, AAPL, MSFT, ..."),
    
    
    dcc.Input(id='input', value='IBM', type='text'),   #input is typed by user
    html.Div(id='output-graph'),                        #output is calculated and processed in the Output par of app.callback
    
    
    html.H3("Je superpose des graphs"),
    dcc.Input(id='input2', value='ne sert à rien pour ce graph ci', type='text'),   
    html.Div(id='output-graph2')
])




@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)


# ESSENTIAL PART: gets what's in callback "Input" (here auction name) returns what 's "Output" (graph)
def update_value(input_data): 
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df=data.DataReader(input_data, #enterprise name
                       start=start, 
                       end=end, 
                       data_source='yahoo')
    df.reset_index(inplace=True)
    df.set_index("Date", inplace=True)
    
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': 'evolution of '+ input_data + '  auction'
            }
        }
    )


""" deuxième graphe """

@app.callback(
    Output(component_id='output-graph2', component_property='children'),
    [Input(component_id='input2', component_property='value')]
)

def update_value2(input_data):   
    return dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Deuxième graph test sans rapport'
            }
        }
    )
    
app.run_server(debug=True, port=3003) #run a local server on this machine

