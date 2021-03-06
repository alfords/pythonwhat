from pythonwhat.check_funcs import check_part, check_part_index, check_node, has_equal_part
from pythonwhat import check_funcs, check_object
from pythonwhat.check_function import check_function
from pythonwhat.check_has_context import has_context
from pythonwhat.test_funcs.test_data_frame import check_df
from pythonwhat.test_funcs.test_dictionary import check_dict
from pythonwhat import test_funcs
from functools import partial
import inspect
#from jinja2 import Template

__PART_WRAPPERS__ = {
        'iter': 'iterable part',
        'body': 'body',
        'key' : 'key part',
        'value': 'value part',
        'orelse': 'else part',
        'test': 'condition' 
        }

__PART_INDEX_WRAPPERS__ = {
        'ifs': '{ordinal} if',
        'handlers': '{index} `except` block',
        'context': '{ordinal} context'
        }

__NODE_WRAPPERS__ = {
        'list_comp': '{ordinal} list comprehension',
        'generator_exp': '{ordinal} generator expression',
        'dict_comp': '{ordinal} dictionary comprehension',
        'for_loop': '{ordinal} for statement',
        'function_def': 'definition of `{index}()`',
        'if_exp': '{ordinal} if expression',
        'if_else': '{ordinal} if statement',
        'lambda_function': '{ordinal} lambda function',
        'try_except': '{ordinal} try statement',
        'while': '{ordinal} `while` loop',
        'with': '{ordinal} `with` statement'
        }

scts = {}

# make has_equal_part wrappers

scts['has_equal_name'] = partial(has_equal_part, 'name', msg='Make sure to use the correct {name}, was expecting {sol_part[name]}, instead got {stu_part[name]}.')
scts['is_default'] = partial(has_equal_part, 'is_default', msg="__JINJA__:Make sure it {{ 'has' if sol_part.is_default else 'does not have'}} a default argument.")

# include rest of wrappers
for k, v in __PART_WRAPPERS__.items():
    scts['check_'+k] = partial(check_part, k, v)

for k, v in __PART_INDEX_WRAPPERS__.items(): 
    scts['check_'+k] = partial(check_part_index, k, part_msg=v)


for k, v in __NODE_WRAPPERS__.items():
    scts['check_'+k] = partial(check_node, k+'s', typestr=v)
scts['check_function'] = check_function

for k in ['set_context', 
          'has_equal_value', 'has_equal_output', 'has_equal_error', 'has_equal_ast', 'call',
          'extend', 'multi', 'test_not', 'fail', 'quiet', 'override',
          'with_context',
          'check_args',
          'has_equal_part']:
    scts[k] = getattr(check_funcs, k)

# include check_object and friends ------
for k in ['check_object', 'is_instance', 'has_equal_key', 'has_key']:
    scts[k] = getattr(check_object, k)

scts['check_df'] = check_df
scts['check_dict'] = check_dict
scts['has_context'] = has_context
