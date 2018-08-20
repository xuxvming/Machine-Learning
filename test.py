
import dash
import dash_core_components as dcc
import dash_html_components as html
import rf_model
from statistics import mean, variance, mode,median
import pandas as pd
import helper


#from rf_model import df, y_pred,X_train, X_test, y_train, y_test,feature_importances,length,accuracy
import plotly.graph_objs as go

app = dash.Dash(__name__)

df = pd.read_csv('data.csv')

data =      {
            'course': 'course',
            'school':'school',
            'students gender':'gender',
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





def make_dash_table(df):
    ''' Return a dash definitio of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://www.ellucian.com/img/ellucian-logo.png', height='100', width='200')
        ], className="ten columns padded"),
        
       
    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5('Student Success Analytics')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}
    
app.layout = html.Div([
    
        
        html.Div([
       
        get_logo(),
        get_header(),
     #   make_dash_table(df.head()),
        
        html.Div([
                
# feature selection             
        html.Div([
         dcc.Dropdown(
         id='my-dropdown',
         options = [{'label': i, 'value':i} for i in data.keys()],
         value = 'course',
         #multi = True
                 ),
        dcc.RadioItems(
                id='display_type',
                options=[{'label': i, 'value': i} for i in ['Mean', 'Mode','Variance','Max','Min','Median']],
                value='Mean',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '49%', 'display': 'inline-block'}),
        
        html.Div([
         dcc.Dropdown(
         id='my-another-dropdown',
         
           ),
         html.Div(id = 'text')
         
        
         ],style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),

    ] ,style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),
       

        


       html.Div([
         dcc.Graph(
           id ='y_pred',
           
                 
                 
                 )
       ],style={'width': '49%','display': 'inline-block', 'padding': '0 20'}),
         
         
         html.Div([
                 dcc.Graph(id = 'detail',
                    )
                 ],style={'display': 'inline-block', 'width': '49%'}),

        html.Div([
                
             
                       
                       
                
                dcc.Graph(id='rf_result',
                  figure ={
                          'data' :[go.Scatter(
                                   x = list (range(len(rf_model.y_pred))),
                                   y = rf_model.y_pred,
                                    mode='markers',
                                    marker={
                                            'color': 'rgb(72,47,135)',
                                            'size': 15,
                                            'opacity': 0.5,
                                            'line': {'width': 0.5, 'color': 'white'}
                                            },
                                    
                                  )],
                            'layout': {
                                    'title' :'Predeicted Results',
                                    'height': 225,
                                    'margin': {'l': 20, 'b': 30, 'r': 10, 't': 40},
                                    'annotations': [{
                                    'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                                    'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                                    'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                                    'text': 'predicted results'
                                    }]
                               }
                          
                          }),
            dcc.Graph(id='rf_actual',
                  
                  figure ={
                          'data' :[go.Scatter(
                                   x = list (range(len(rf_model.y_pred))),
                                   y = rf_model.y_test,
                                    mode='markers',
                                    marker={
                                            'color': 'rgb(72,47,135)',
                                            'size': 15,
                                            'opacity': 0.5,
                                            'line': {'width': 0.5, 'color': 'white'}
                                            },
                                    
                                  )],
                            'layout': {
                                    'title':'Actual Results' ,
                                    'height': 200,
                                    'margin': {'l': 20, 'b': 30, 'r': 10, 't': 40},
                                    'annotations': [{
                                    'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                                    'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                                    'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                                    'text': 'actual results'
                                    }]
                               }
                          
                          }),
    
                       
    ], style={'display': 'inline-block', 'width': '49%','padding': '0 20'}),

     html.Div([
             dcc.Graph( id ='important_featrues',
           
                 figure ={
                          'data' :[go.Bar(
                                   x = list(dict(rf_model.feature_importances).keys()),
                                   y = list(dict(rf_model.feature_importances).values()),
                                    
                                    marker={
                                            'color': 'rgb(72,47,135)',
                                            
                                            'opacity': 0.5,
                                            'line': {'width': 0.5, 'color': 'white'}
                                            },
                                    
                                  )],
                          'layout':{
                                  'title' : 'Factors That Impact Students Grade',
                                  'margin': {'l': 20, 'b': 30, 'r': 10, 't': 40},
                                   'height' : 425
                                  }
                            
                          
                          })
       ],style={'width': '49%', 'display': 'inline-block',}),
         
          ]),
    
    
    ])
        
         
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
    
    trace_G3 ={}
    trace_G2 ={}
    trace_G1 ={}
    
    
    
    for row in range(df.shape[0]):
        
        trace_G3 = do_index(df.loc[row][x_column_name],df.loc[row]['third period grade'],trace_G3)
        trace_G2 = do_index(df.loc[row][x_column_name],df.loc[row]['second period grade'],trace_G2)
        trace_G1 = do_index(df.loc[row][x_column_name],df.loc[row]['first period grade'],trace_G1)
    print(list(trace_G3.keys()))
    
    result_G3 = []
    result_G1 = []
    result_G2 = []
    if display_type == 'Mean' :
         for i in range(len(list(trace_G3.values()))):
             result_G3.append (mean(list(trace_G3.values())[i]))
             
         for i in range(len(list(trace_G2.values()))):
             result_G2.append (mean(list(trace_G2.values())[i]))
        
         for i in range(len(list(trace_G1.values()))):
             result_G1.append (mean(list(trace_G1.values())[i]))
        
    
    if display_type == 'Mode' :
         for i in range(len(list(trace_G3.values()))):
             result_G3.append (mode(list(trace_G3.values())[i]))
             
         for i in range(len(list(trace_G2.values()))):
             result_G2.append (mode(list(trace_G2.values())[i]))
             
         for i in range(len(list(trace_G1.values()))):
             result_G1.append (mode(list(trace_G1.values())[i]))
             
    if display_type == 'Variance' :
         for i in range(len(list(trace_G3.values()))):
             result_G3.append (variance(list(trace_G3.values())[i]))
         
         for i in range(len(list(trace_G2.values()))):
             result_G2.append (variance(list(trace_G2.values())[i]))
             
         for i in range(len(list(trace_G1.values()))):
             result_G1.append (variance(list(trace_G1.values())[i]))
            
    if display_type == 'min' :
         for i in range(len(list(trace_G3.values()))):
             result_G3.append (min(list(trace_G3.values())[i]))
             
         for i in range(len(list(trace_G2.values()))):
             result_G2.append (min(list(trace_G2.values())[i]))
        
         for i in range(len(list(trace_G1.values()))):
             result_G1.append (min(list(trace_G1.values())[i]))
    
    if display_type == 'Max' :
         for i in range(len(list(trace_G3.values()))):
           result_G3.append (max(list(trace_G3.values())[i]))
           
         for i in range(len(list(trace_G2.values()))):
           result_G2.append (max(list(trace_G2.values())[i]))
           
         for i in range(len(list(trace_G1.values()))):
           result_G1.append (max(list(trace_G1.values())[i]))
    
    if display_type == 'median' :
         for i in range(len(list(trace_G3.values()))):
             result_G3.append (median(list(trace_G3.values())[i]))
         
         for i in range(len(list(trace_G2.values()))):
             result_G2.append (median(list(trace_G2.values())[i]))
             
         for i in range(len(list(trace_G1.values()))):
             result_G1.append (median(list(trace_G1.values())[i]))
             
    # for loop to get the avarage value of each column
    
        
    print(result_G1)
    
    
    graph_3 = []
    
    graph_3.append(go.Bar(
            x = list(trace_G3.keys()),
            y = result_G3,
            
            opacity=0.7,
            name = 'Thrid Year Results',
            marker={
                 'color' :'rgb(5,246,155)',
                 
            }
            ))
    
    graph_3.append(go.Bar(
            x = list(trace_G3.keys()),
            y = result_G2,
            
            opacity=0.7,
            name = 'Second Year Results',
            marker={
                 'color' :'rgb(72,47,135)',
                 
            }
            ))
    graph_3.append(go.Bar(
            x = list(trace_G3.keys()),
            y = result_G1,
            name = 'First Year Results',
            opacity=0.7,
            marker={
                 'color' :'rgb(65,64,66 )',
                 
            }
            ))
            
        
    
    
    return {
            'data': graph_3,
            'layout': go.Layout(
            xaxis={
                'title': 'selected features',
                
            },
            yaxis={
                'title': 'Students Grades',
                
            },
            #margin={'l': 40, 'b': 30, 't': 0, 'r': 10},
            height=450,
            
            hovermode='closest')
            
            
            
            }
            
@app.callback(
    dash.dependencies.Output('text', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value'),
     dash.dependencies.Input('my-another-dropdown','value')])

def update_text(selected_feature, selected_value):
    
   
   
    df_temp = df.loc[df[selected_feature] == selected_value]
   
    df_temp2 = df_temp.drop([selected_feature, 'first period grade','second period grade','third period grade'], axis = 1)
    df_temp2 = helper.handle_non_numerical_data(df_temp2)
    
    df_temp2 = helper.normalize(df_temp2)
    return 'Total number of students "{}"'.format(df_temp2.shape[0])




@app.callback(
    dash.dependencies.Output('my-another-dropdown', 'options'),
   
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_dropdown(x_column_name):
    trace ={}
    
    t = []
    
    for row in range(df.shape[0]):
        
        trace = do_index(df.loc[row][x_column_name],df.loc[row]['third period grade'],trace)
 
    print('this function')
    
    #t = list(trace.keys())
    #trace.clear()
    
    return [{'label': i, 'value' :i } for i in list(trace.keys())]

@app.callback(
    dash.dependencies.Output('detail', 'figure'),
    [dash.dependencies.Input('my-dropdown', 'value'),
     dash.dependencies.Input('my-another-dropdown','value')])

def update_details(selected_feature, selected_value):
    
    trace = []
   
    df_temp = df.loc[df[selected_feature] == selected_value]
   
    df_temp2 = df_temp.drop([selected_feature, 'first period grade','second period grade','third period grade'], axis = 1)
    df_temp2 = helper.handle_non_numerical_data(df_temp2)
    
    df_temp2 = helper.normalize(df_temp2)
   
    
    for column in df_temp2.columns:
        trace.append(df_temp2[column].mean())
    
    print(df_temp2.columns)
    print(trace)
        
    graph = []
    
    graph.append(
            go.Bar(
            x = df_temp2.columns,
            y = trace,
            name = 'First Year Results',
            opacity=0.7,
            marker={
                 'color' :'rgb(65,64,66 )',
                 
            }
                    
                    )

            )
    return {
            'data': graph,
            'layout': go.Layout(
            xaxis={
                'title': 'Features',
                
            },
            yaxis={
                'title': 'Average value of each feature',
                
            },
            #margin={'l': 40, 'b': 30, 't': 0, 'r': 10},
            height=450,
            
            hovermode='closest')
            
            
            
            }
        

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "https://fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/xuxvming/pen/mjxrzB.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server()