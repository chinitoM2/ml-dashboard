import plotly.graph_objects as pgo

def pie(df, values, names, hole, hovertemplate):
  fig = pgo.Figure(pgo.Pie(
    values=df[values],
    labels=df[names],
    hole=hole,
    textinfo='label+percent',
    hovertemplate=hovertemplate
  ))
  return fig