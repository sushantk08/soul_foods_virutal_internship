import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load formatted data
df = pd.read_csv("formatted_Sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Create Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div([

    # Header
    html.H1(
        "Soul Foods Pink Morsel Sales Visualiser",
        style={
            "textAlign": "center",
            "color": "#2c3e50",
            "padding": "20px"
        }
    ),

    # Radio Buttons
    html.Div([

        html.Label(
            "Select Region:",
            style={
                "fontSize": "20px",
                "fontWeight": "bold",
                "marginRight": "15px"
            }
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"fontSize": "18px"}
        )

    ],
    style={
        "padding": "15px",
        "backgroundColor": "#ecf0f1",
        "borderRadius": "10px",
        "marginBottom": "20px"
    }),

    # Line Chart
    dcc.Graph(id="sales-line-chart")

],
style={
    "backgroundColor": "#f8f9fa",
    "padding": "30px",
    "fontFamily": "Arial"
})

# Callback to update chart
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    # Filter data
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    # Group sales by date
    sales_by_date = (
        filtered_df.groupby("Date")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Date")
    )

    # Create line chart
    fig = px.line(
        sales_by_date,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.title()})",
        markers=True
    )

    # Update chart styling
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales",
        template="plotly_white",
        title_x=0.5
    )

    return fig

# Run server
if __name__ == "__main__":
    app.run(debug=True)