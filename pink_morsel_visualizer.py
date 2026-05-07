import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df=pd.read_csv("formatted_sales_data.csv")

df["Date"]=pd.to_datetime(df["Date"])

df=df.sort_values("Date")

sales_by_date=df.groupby("Date")["Sales"].sum().reset_index()



fig=px.line(
    sales_by_date,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales",
    template="plotly_white"
)

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    
    # Header
    html.H1(
        "Soul Foods Pink Morsel Sales Visualiser",
        style={"textAlign": "center"}
    ),

    # Line Chart
    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )

])

# Run server
if __name__ == "__main__":
    app.run(debug=True)