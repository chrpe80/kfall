from dash import Dash, html, dcc
import plotly
import plotly.express as px
from dash import dash_table

from prepare_df_F01 import data

about = """
The aim of KFall dataset is to contribute technology development for elderly fall detection and injury prevention. 
It was acquired by 32 young subjects with 21 types of activities of daily living (ADLs) and 15 types of falls 
from an inertial sensor attached on low back. 
In total, it contains 5075 motion files with 2729 ADL motions and 2346 fall motions. 
In addition, for each fall motion, ready-to-use fall labels (fall initialization and fall impact moment) based
on synchronized video references were also included.
(Yu X, Jang J, and Xiong S. (2021). Overall of KFall. Source. URL)
"""

dataset = """
Task F01, First trial, all subjects. 
With the fall onset and fall impact frames i created three categories [before fall, during fall, after fall].
"""

app = Dash(__name__)

fig1 = px.imshow(img=data.corr(), width=750, height=750, aspect="auto", color_continuous_scale="inferno", title="Feature correlation")
fig2 = px.histogram(data_frame=data, x="Class", color="Class", color_discrete_sequence=plotly.colors.qualitative.Plotly, title="Balance of classes")

app.layout = html.Div(
    children=[html.H1(children='KFall'),
              html.H2(children='About'),
              html.P(children=about),
              html.H2(children='Dataset'),
              html.P(children=dataset),
              dash_table.DataTable(data.head().to_dict('records'), [{"name": i, "id": i} for i in data.columns]),
              dcc.Graph(id='heat',figure=fig1),
              dcc.Graph(id='balance',figure=fig2),
              ],

)

if __name__ == '__main__':
    app.run(debug=True)
