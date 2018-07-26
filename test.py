import json
from textwrap import dedent as d

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from statistics import mean, variance, mode,stdev,median
import pandas as pd
import numpy as np
#from rf_model import df, y_pred,X_train, X_test, y_train, y_test,feature_importances,length,accuracy
import plotly.graph_objs as go

app = dash.Dash(__name__)

df = pd.read_csv('data.csv')

data =      {
            'course': 'course',
            'school':'school',
            'students sex':'sex',
            'students age' : 'age',
            'students home address': 'address',
            'family size': 'famsize',
            'parents cohabitation status': 'Pstatus',
            'mothers education': 'Medu',
            'fathers education': 'Fedu',
            'mothers job': 'Mjob',
            'fathers job': 'Fjob',
            'reason to choose this school': 'reason',
            'students guardian': 'guardian',
            'home to school travel time': 'traveltime',
            'weekly study time': 'studytime',
            'failures': 'number of past class failures',
            'family educational support': 'famsup',
            'extra educational support':'schoolsup',
            'extra paid classes within the course subject': 'paid',
            'extra-curricular activities': 'activities',
            'wants to take higher education': 'higher',
            'Internet access at home': 'internet',
            'with a romantic relationship': 'romantic',
            'quality of family relationships': 'famrel',
            'free time after school': 'freetime',
            'going out with friends': 'goout',
            'workday alcohol consumption': 'Dalc',
            'weekend alcohol consumption': 'Walc',
            'current health status': 'health',
            'number of school absences': 'absences',
            'first period grade' :'G1',
            'second period grade' :'G2',
            'third period grade' :'G3',
            }
df.columns = list(data.keys())

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}
    
app.layout = html.Div([
        
        html.Div([
                
# feature selection             
        html.Div([
         dcc.Dropdown(
         id='my-dropdown',
         options = [{'label': i, 'values':i} for i in data.keys()],
         value = 'course',
         multi = True
                 ),
        dcc.RadioItems(
                id='display_type',
                options=[{'label': i, 'value': i} for i in ['Mean', 'Mode','Variance']],
                value='Mean',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),



#y-pred graph
       html.Div([
         dcc.Graph(
           id ='y_pred'
                 
                 
                 )
       ],style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
'''
#y_test graph
       html.Div([
         dcc.Graph()
       ]),

#feature importance graph
       html.Div([
         dcc.Graph()
         ])
               
'''               
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                ])
        
        # ])
def do_index(keyword, pagenumber, page_index):
    """
    if keyword exists add pagenumber to that particular list
    otherwise make new entry to index dictionary
    """
    page_index.setdefault(keyword, []).append(pagenumber)
    return page_index


    

@app.callback(
    dash.dependencies.Output('y_pred', 'figure'),
    [dash.dependencies.Input('my-dropdown', 'value'),
     dash.dependencies.Input('display_type','value')])
def update_main_graph(x_column_name,display_type):
    
    
    
    trace_G3 = {}
    for row in range(df.shape[0]):
        
        trace_G3 = do_index(df.loc[row][x_column_name],df.loc[row]['third period grade'],trace_G3)
        
    print(list(trace_G3.keys()))
    
    result = []
    if display_type == 'Mean' :
         for i in range(len(list(trace_G3.values()))):
             result.append (mean(list(trace_G3.values())[i]))
             
    
    if display_type == 'Mode' :
         for i in range(len(list(trace_G3.values()))):
             result.append (mode(list(trace_G3.values())[i]))
             
             
    if display_type == 'Variance' :
         for i in range(len(list(trace_G3.values()))):
             result.append (variance(list(trace_G3.values())[i]))
            
     
    '''        
    if display_type == 'Standard Deviation' :
         for i in range(len(list(trace_G3.values()))):
             result.append (stdev(list(trace_G3.values())[i]))
             print(result[i])
     '''        
    if display_type == 'median' :
         for i in range(len(list(trace_G3.values()))):
             result.append (median(list(trace_G3.values())[i]))
             
    # for loop to get the avarage value of each column
    
        
    print(result)
    
    
    
    return {
            'data':[go.Bar(
                    
                    x = list(trace_G3.keys()),
                    y = result,
                    
                    marker={
                        
                        'color': 'rgb(8,48,107)',
                        
                        'opacity': 0.5,
                        'line': {'width': 0.5, 'color': 'rgb(8,48,107)'}
                    }               
                    )],
            'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
            
            
            }



if __name__ == '__main__':
    app.run_server()