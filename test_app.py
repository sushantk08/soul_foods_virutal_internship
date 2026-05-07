from pink_morsel_visualizer import app
from dash.testing.application_runners import import_app


def test_header_exists(dash_duo):

    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")

    assert header is not None
    assert "Soul Foods Pink Morsel Sales Visualiser" in header.text


def test_graph_exists(dash_duo):

    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-line-chart")

    assert graph is not None


def test_region_picker_exists(dash_duo):

    dash_duo.start_server(app)

    radio_items = dash_duo.find_element("#region-filter")

    assert radio_items is not None