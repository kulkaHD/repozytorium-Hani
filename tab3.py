from dash import html, dcc
import plotly.graph_objects as go

def render_tab(df):

    layout = html.Div([html.H1('Kanały sprzedaży a dni tygodnia',style={'text-align':'center'}),

                        
                        html.Div([dcc.Dropdown(id='store_dropdown',
                                    options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    dcc.Graph(id='pie-store-type')],style={'width':'50%'}),
                                    html.Div(id='temp-out'),
                        html.Div([dcc.Dropdown(id='dzien_dropdown',
                                    options=[{'label':dzień,'value':dzień} for dzień in df['tran_date_nazwa_dnia'].unique()],
                                    value=df['tran_date_nazwa_dnia'].unique()[0]),
                                    dcc.Graph(id='pie-dzien')],style={'width':'50%'}),
                                    html.Div(id='temp-out')
                        ])




    return layout