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
html_logo = ('https://camo.githubusercontent.com/50cf39121274b3db22bf1bd72cbe25af9078e037441cb5b5bdef1cc9dc5eb2f7/68747470733a2f2f63646e2e7261776769742e636f6d2f73696e647265736f726875732f617765736f6d652f643733303566333864323966656437386661383536353265336136336531353464643865383832392f6d656469612f62616467652e737667')
html_favicon = ('data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🎯</text></svg>')
html_static_path = ['_static']

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