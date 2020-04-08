""" exampleArray = ["String", "Asset", "Other Nonsense"]
for x in exampleArray:
    print(x)
"""
import plotly.graph_objects as go

testFig = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
                cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                    ])

testFig.show()

