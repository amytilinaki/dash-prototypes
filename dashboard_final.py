from dash import Dash,html,dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from directory_scanner import Run_Directory_Scanner
import settings2
from loading import data
import sys
import glob

entries = settings2.data_path

app2 = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
app2.layout = html.Div(children=[
    html.H1(children=f'The {entries} Directory'),

    dbc.Label("Choose the run file"),

    dcc.Dropdown(id='run-dropdown',options=[{'label': k, 'value': k} for k in (range(1,4))],
        value='A'),

    dbc.Label("Choose the TR"),
    dcc.Dropdown(id='tr-dropdown'),
    html.Div(id='textarea-output')

])

@app2.callback(Output('tr-dropdown',"options"),Input("run-dropdown", "value"))

def create_drop2(run_value):
    
    if run_value:
        list=[]
        path1=(f"{data()}/*")
        path=f"{path1}run{run_value}*"
       
        for filename in (glob.glob(path)):

            with open(filename, 'r') as f:
                for line in f:
                    list.append(int(line))

        list.sort()
        return list

@app2.callback(Output("textarea-output", "children"),[Input("run-dropdown", "value"),Input("tr-dropdown", "value")])

def choose_file(run_value,tr_value):

    if run_value and tr_value:
        a=Run_Directory_Scanner
        if f"run {run_value}"  in a.create() and f"tr {tr_value}" in a.create()[f"run {run_value}"]:
            return a.create()[f"run {run_value}"][f"tr {tr_value}"]
        else:
           
            return "This file does not exist"

  
if __name__ == '__main__':

    print(sys.argv)
    settings2.data_path = sys.argv[1]
    
    app2.run_server(debug=True, port=8030)