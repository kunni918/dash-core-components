# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import dash
from dash.dependencies import Input, Output

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
import base64
import importlib
import io
import multiprocessing
import os
import pandas as pd
import percy
import sys
import time
import unittest

from .IntegrationTests import IntegrationTests
from .utils import assert_clean_console, invincible, wait_for

# Download geckodriver: https://github.com/mozilla/geckodriver/releases
# And add to path:
# export PATH=$PATH:/Users/chriddyp/Repos/dash-stuff/dash-integration-tests
#
# Uses percy.io for automated screenshot tests
# export PERCY_PROJECT=plotly/dash-integration-tests
# export PERCY_TOKEN=...


class Tests(IntegrationTests):
    def setUp(self):
        def wait_for_element_by_id(id):
            wait_for(lambda: None is not invincible(
                lambda: self.driver.find_element_by_id(id)
            ))
            return self.driver.find_element_by_id(id)
        self.wait_for_element_by_id = wait_for_element_by_id

        def wait_for_element_by_css_selector(css_selector):
            wait_for(lambda: None is not invincible(
                lambda: self.driver.find_element_by_css_selector(css_selector)
            ))
            return self.driver.find_element_by_css_selector(css_selector)
        self.wait_for_element_by_css_selector = (
            wait_for_element_by_css_selector
        )

    def snapshot(self, name):
        if 'PERCY_PROJECT' in os.environ and 'PERCY_TOKEN' in os.environ:
            python_version = sys.version.split(' ')[0]
            print('Percy Snapshot {}'.format(python_version))
            self.percy_runner.snapshot(name=name)

    # def create_upload_component_content_types_test(self, filename):
    #     app = dash.Dash(__name__)
    #
    #     filepath = os.path.join(os.getcwd(), 'test', 'upload-assets', filename)
    #
    #     pre_style = {
    #         'whiteSpace': 'pre-wrap',
    #         'wordBreak': 'break-all'
    #     }
    #
    #     app.layout = html.Div([
    #         html.Div(filepath, id='waitfor'),
    #         html.Div(
    #             id='upload-div',
    #             children=dcc.Upload(
    #                 id='upload',
    #                 children=html.Div([
    #                     'Drag and Drop or ',
    #                     html.A('Select a File')
    #                 ]),
    #                 style={
    #                     'width': '100%',
    #                     'height': '60px',
    #                     'lineHeight': '60px',
    #                     'borderWidth': '1px',
    #                     'borderStyle': 'dashed',
    #                     'borderRadius': '5px',
    #                     'textAlign': 'center'
    #                 }
    #             )
    #         ),
    #         html.Div(id='output'),
    #         html.Div(dt.DataTable(rows=[{}]), style={'display': 'none'})
    #     ])
    #
    #     @app.callback(Output('output', 'children'),
    #                   [Input('upload', 'contents')])
    #     def update_output(contents):
    #         if contents is not None:
    #             content_type, content_string = contents.split(',')
    #             if 'csv' in filepath:
    #                 df = pd.read_csv(io.StringIO(base64.b64decode(
    #                     content_string).decode('utf-8')))
    #                 return html.Div([
    #                     dt.DataTable(rows=df.to_dict('records')),
    #                     html.Hr(),
    #                     html.Div('Raw Content'),
    #                     html.Pre(contents, style=pre_style)
    #                 ])
    #             elif 'xls' in filepath:
    #                 df = pd.read_excel(io.BytesIO(base64.b64decode(
    #                     content_string)))
    #                 return html.Div([
    #                     dt.DataTable(rows=df.to_dict('records')),
    #                     html.Hr(),
    #                     html.Div('Raw Content'),
    #                     html.Pre(contents, style=pre_style)
    #                 ])
    #             elif 'image' in content_type:
    #                 return html.Div([
    #                     html.Img(src=contents),
    #                     html.Hr(),
    #                     html.Div('Raw Content'),
    #                     html.Pre(contents, style=pre_style)
    #                 ])
    #             else:
    #                 return html.Div([
    #                     html.Hr(),
    #                     html.Div('Raw Content'),
    #                     html.Pre(contents, style=pre_style)
    #                 ])
    #
    #     self.startServer(app)
    #
    #     try:
    #         self.wait_for_element_by_id('waitfor')
    #     except Exception as e:
    #         print(self.wait_for_element_by_id(
    #             '_dash-app-content').get_attribute('innerHTML'))
    #         raise e
    #
    #     upload_div = self.wait_for_element_by_css_selector(
    #         '#upload-div input[type=file]')
    #
    #     upload_div.send_keys(filepath)
    #     time.sleep(5)
    #     self.snapshot(filename)
    #
    # def test_upload_csv(self):
    #     self.create_upload_component_content_types_test('utf8.csv')
    #
    # def test_upload_xlsx(self):
    #     self.create_upload_component_content_types_test('utf8.xlsx')
    #
    # def test_upload_png(self):
    #     self.create_upload_component_content_types_test('dash-logo-stripe.png')
    #
    # def test_upload_svg(self):
    #     self.create_upload_component_content_types_test('dash-logo-stripe.svg')
    #
    # def test_upload_gallery(self):
    #     app = dash.Dash(__name__)
    #     app.layout = html.Div([
    #         html.Div(id='waitfor'),
    #         html.Label('Empty'),
    #         dcc.Upload(),
    #
    #         html.Label('Button'),
    #         dcc.Upload(html.Button('Upload File')),
    #
    #         html.Label('Text'),
    #         dcc.Upload('Upload File'),
    #
    #         html.Label('Link'),
    #         dcc.Upload(html.A('Upload File')),
    #
    #         html.Label('Style'),
    #         dcc.Upload([
    #             'Drag and Drop or ',
    #             html.A('Select a File')
    #         ], style={
    #             'widatetimeh': '100%',
    #             'height': '60px',
    #             'lineHeight': '60px',
    #             'borderWidatetimeh': '1px',
    #             'borderStyle': 'dashed',
    #             'borderRadius': '5px',
    #             'textAlign': 'center'
    #         })
    #     ])
    #     self.startServer(app)
    #
    #     try:
    #         self.wait_for_element_by_id('waitfor')
    #     except Exception as e:
    #         print(self.wait_for_element_by_id(
    #             '_dash-app-content').get_attribute('innerHTML'))
    #         raise e
    #
    #     self.snapshot('test_upload_gallery')
    #
    # def test_gallery(self):
    #     app = dash.Dash(__name__)
    #
    #     app.layout = html.Div([
    #         html.Div(id='waitfor'),
    #         html.Label('Upload'),
    #         dcc.Upload(),
    #         html.Label('Dropdown'),
    #         dcc.Dropdown(
    #             options=[
    #                 {'label': 'New York City', 'value': 'NYC'},
    #                 {'label': u'Montréal', 'value': 'MTL'},
    #                 {'label': 'San Francisco', 'value': 'SF'},
    #                 {'label': u'北京', 'value': u'北京'}
    #             ],
    #             value='MTL',
    #             id='dropdown'
    #         ),
    #
    #         html.Label('Multi-Select Dropdown'),
    #         dcc.Dropdown(
    #             options=[
    #                 {'label': 'New York City', 'value': 'NYC'},
    #                 {'label': u'Montréal', 'value': 'MTL'},
    #                 {'label': 'San Francisco', 'value': 'SF'},
    #                 {'label': u'北京', 'value': u'北京'}
    #             ],
    #             value=['MTL', 'SF'],
    #             multi=True
    #         ),
    #
    #         html.Label('Radio Items'),
    #         dcc.RadioItems(
    #             options=[
    #                 {'label': 'New York City', 'value': 'NYC'},
    #                 {'label': u'Montréal', 'value': 'MTL'},
    #                 {'label': 'San Francisco', 'value': 'SF'},
    #                 {'label': u'北京', 'value': u'北京'}
    #             ],
    #             value='MTL'
    #         ),
    #
    #         html.Label('Checkboxes'),
    #         dcc.Checklist(
    #             options=[
    #                 {'label': 'New York City', 'value': 'NYC'},
    #                 {'label': u'Montréal', 'value': 'MTL'},
    #                 {'label': 'San Francisco', 'value': 'SF'},
    #                 {'label': u'北京', 'value': u'北京'}
    #             ],
    #             values=['MTL', 'SF']
    #         ),
    #
    #         html.Label('Text Input'),
    #         dcc.Input(value='MTL', type='text'),
    #
    #         html.Label('Slider'),
    #         dcc.Slider(
    #             min=0,
    #             max=9,
    #             marks={i: 'Label {}'.format(i) if i == 1 else str(i)
    #                    for i in range(1, 6)},
    #             value=5,
    #         ),
    #
    #         html.Label('Graph'),
    #         dcc.Graph(
    #             id='graph',
    #             figure={
    #                 'data': [{
    #                     'x': [1, 2, 3],
    #                     'y': [4, 1, 4]
    #                 }],
    #                 'layout': {
    #                     'title': u'北京'
    #                 }
    #             }
    #         ),
    #
    #         html.Label('DatePickerSingle'),
    #         dcc.DatePickerSingle(
    #             id='date-picker-single',
    #             date=datetime(1997, 5, 10)
    #         ),
    #
    #         html.Label('DatePickerRange'),
    #         dcc.DatePickerRange(
    #             id='date-picker-range',
    #             start_date=datetime(1997, 5, 3),
    #             end_date_placeholder_text='Select a date!'
    #         ),
    #
    #         html.Label('TextArea'),
    #         dcc.Textarea(
    #             placeholder='Enter a value... 北京',
    #             style={'width': '100%'}
    #         ),
    #
    #         html.Label('Markdown'),
    #         dcc.Markdown('''
    #             #### Dash and Markdown
    #
    #             Dash supports [Markdown](http://commonmark.org/help).
    #
    #             Markdown is a simple way to write and format text.
    #             It includes a syntax for things like **bold text** and *italics*,
    #             [links](http://commonmark.org/help), inline `code` snippets, lists,
    #             quotes, and more.
    #
    #             北京
    #         '''.replace('    ', ''))
    #     ])
    #     self.startServer(app)
    #
    #     try:
    #         self.wait_for_element_by_id('waitfor')
    #     except Exception as e:
    #         print(self.wait_for_element_by_id(
    #             '_dash-app-content').get_attribute('innerHTML'))
    #         raise e
    #
    #     self.snapshot('gallery')
    #
    #     self.driver.find_element_by_css_selector(
    #         '#dropdown .Select-input input'
    #     ).send_keys(u'北')
    #     self.snapshot('gallery - chinese character')

    def test_location_link(self):
        app = dash.Dash(__name__)

        app.layout = html.Div([
            html.Div(id='waitfor'),
            dcc.Location(id='test-location', refresh=False),

            dcc.Link(
                html.Button('I am a clickable button'),
                id='test-link',
                href='/test/pathname'),
            dcc.Link(
                html.Button('I am a clickable hash button'),
                id='test-link-hash',
                href='#test'),
            dcc.Link(
                html.Button('I am a clickable search button'),
                id='test-link-search',
                href='?testQuery=testValue'),
            html.Button('I am a magic button that updates pathname', id='test-button'),
            html.Div(id='test-pathname', children=[]),
            html.Div(id='test-hash', children=[]),
            html.Div(id='test-search', children=[]),
        ])

        @app.callback(
            output=Output(component_id='test-pathname', component_property='children'),
            inputs=[Input(component_id='test-location', component_property='pathname')])
        def update_location_on_page(pathname):
            if pathname is None:
                return '/'

            return pathname

        @app.callback(
            output=Output(component_id='test-hash', component_property='children'),
            inputs=[Input(component_id='test-location', component_property='hash')])
        def update_location_on_page(hash_val):
            if hash_val is None:
                return ''

            return hash_val

        @app.callback(
            output=Output(component_id='test-search', component_property='children'),
            inputs=[Input(component_id='test-location', component_property='search')])
        def update_location_on_page(search):
            if search is None:
                return ''

            return search

        @app.callback(
            output=Output(component_id='test-location', component_property='pathname'),
            inputs=[Input(component_id='test-button', component_property='n_clicks')])
        def update_pathname(n_clicks):
            if n_clicks is not None:
                return '/new/pathname'

            return '/'

        self.startServer(app=app)

        try:
            self.wait_for_element_by_id('waitfor')
        except Exception as e:
            print(self.wait_for_element_by_id(
                '_dash-app-content').get_attribute('innerHTML'))
            raise e

        # Check that link updates pathname
        self.driver.find_element_by_id('test-link').click()

        self.assertEqual(
            self.driver.current_url.replace('http://localhost:8050', ''),
            '/test/pathname')
        self.assertEqual(
            self.driver.find_element_by_id('test-pathname').text,
            '/test/pathname')

        # Check that hash is updated in the Location
        self.driver.find_element_by_id('test-link-hash').click()

        self.assertEqual(self.driver.find_element_by_id('test-pathname').text, '/test/pathname')
        self.assertEqual(self.driver.find_element_by_id('test-hash').text, '#test')

        # Check that search is updated in the Location
        self.driver.find_element_by_id('test-link-search').click()

        self.assertEqual(self.driver.find_element_by_id('test-search').text, '?testQuery=testValue')
        self.assertEqual(self.driver.find_element_by_id('test-hash').text, '')

        self.driver.find_element_by_id('test-button').click()

        self.assertEqual(self.driver.find_element_by_id('test-pathname').text, '/new/pathname')
