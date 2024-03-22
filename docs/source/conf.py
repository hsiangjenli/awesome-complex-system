import datetime
import os.path as osp
import sys

import pyg_sphinx_theme as my_sphinx_theme

author = 'Hsiang-Jen Li'

copyright = f'{datetime.datetime.now().year}, {author}'

if datetime.datetime.now().year != 2024:
    copyright = "2024 ~ " + copyright


sys.path.append(osp.join(osp.dirname(my_sphinx_theme.__file__), 'extension'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'nbsphinx',
]

html_theme = 'pyg_sphinx_theme'
html_title = ''
html_logo = ('https://hsiangjenli.github.io/static/image/ico.svg')
html_favicon = ('https://hsiangjenli.github.io/static/image/ico.svg')
html_static_path = ['_static']
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }

add_module_names = False
autodoc_member_order = 'bysource'

suppress_warnings = ['autodoc.import_object']

intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy', None),
    'pandas': ('http://pandas.pydata.org/pandas-docs/dev', None),
    'torch': ('https://pytorch.org/docs/master', None),
}

simplepdf_vars = {
    'primary': '#333333',
    'links': '#FF3333',
}

def setup(app):
    def rst_jinja_render(app, _, source):
        rst_context = {}
        source[0] = app.builder.templates.render_string(source[0], rst_context)

    # app.connect('source-read', rst_jinja_render)
    app.add_js_file('js/version_alert.js')