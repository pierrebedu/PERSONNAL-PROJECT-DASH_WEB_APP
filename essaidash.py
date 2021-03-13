import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime
from pandas_datareader import data

# load the dataframe

df = data.DataReader("IBM", 
                       start='2015-1-1', 
                       end='2015-12-31', 
                       data_source='yahoo')


#create the app

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Ma première web app avec Dash'),
    html.H2(children="Choisissez un nom d'action ci dessous : IBM, AAPL, MSFT, ..."),
    dcc.Input(id='input', value='IBM', type='text'),
    html.Div(id='output-graph')
    
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)



def update_value(input_data): #input data vairable is created once dash dependencies called
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df=data.DataReader(input_data, 
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
                'title': input_data
            }
        }
    )
    
    
app.run_server(debug=True, port=3003)

