import dash
import dash_core_components as dcc
import dash_html_components as html
import analyze
from dash.dependencies import Input, Output

number_labels = {'Sampling Frequency in Hz': 'fs_hz',
                 'Number of Coefficients': 'number_coeffs',
                 'Low Cutoff in Hz': 'f_low_hz',
                 'High Cutoff in Hz': 'f_high_hz'}

types = [{'label': 'Bandpass', 'value': 'bandpass'},
         {'label': 'Lowpass', 'value': 'lowpass'},
         {'label': 'Highpass', 'value': 'highpass'},
         {'label': 'Bandstop', 'value': 'bandstop'}]

designs = [{'label': 'Butterworth', 'value': 'butter'},
           {'label': 'Chebyshev I', 'value': 'cheby1'},
           {'label': 'Chebyshev II', 'value': 'cheby2'},
           {'label': 'Cauer/elliptic', 'value': 'ellip'},
           {'label': 'Bessel/Thomson', 'value': 'bessel'},
           {'label': 'RBJ/ADI', 'value': 'rbjadi'}]

default = {'Type': 'bandpass',
           'Design': 'butter'}

dropdown_options = {'Type': types,
                    'Design': designs}

dropdown_labels = {'Type': 'f_type',
                   'Design': 'design'}

filt_def = {'fs_hz': None,
            'number_coeffs': None,
            'f_low_hz': None,
            'f_high_hz': None,
            'f_type': None,
            'design': None}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

inputs = [[html.Label(label), dcc.Input(id=number_labels[label], type="number")] for label in number_labels]
dropdowns = [[html.Label(dl), dcc.Dropdown(id=dropdown_labels[dl], options=dropdown_options[dl], value=default[dl])] for dl in dropdown_labels]
inputs += dropdowns

width = str(100/len(filt_def)) + '%'
children = [html.Div(children=i, style={'width': width, 'display': 'inline-block'}) for i in inputs]

#html.Div(children=dcc.Graph(id='mag'))]))

app.layout = html.Div(children=children, style={'width': '100%', 'height': '10%', 'display': 'inline-block'})


'''
@app.callback(
    Output('mag', 'figure'),
    [Input('design-dropdown', 'value')])
def update_mag(design):
    traces = [dict(
             x=[100, 20e3],
             y=[0, 0],
             name='magnitude',
             text=design,
             mode='markers',
             marker={'size': 10,
                     'color': 'firebrick'},
             opacity=0.5)]

    return {
        'data': traces,
        'layout': dict(
            xaxis={'type': 'log',
                   'title': design,
                   # 'range': np.log10([100, 20e3])
                   },
            yaxis={'title': 'Ampitude in dB',
                   'range': [-45, 45]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest',
            transition={'duration': 500},
        )
    }
    '''


if __name__ == '__main__':
    app.run_server(debug=True)