# 8.2:  Include some useful settings.

import warnings

## Enable multiple outputs from jupyter cells
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

## disable the Pandas "setting a copy of a slice" warning
# pd.options.mode.chained_assignment = None

## set default number of DataFrame rows printed to 8
pd.set_option('display.max_rows', 8)

# suppress excel reader warning:  'extension is unsupported'
warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

