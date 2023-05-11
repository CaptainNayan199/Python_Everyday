# So today we are going to observe what actually is import and how does it work
# what is the rocket science behind it?

# so whenever we want to use any libraries in python, we need to install it using pip command, and then after installing it we need to import in our code and then only we can use it.
# IMporting in oython is the process of loading code from a python module in the current code. This allows us to use the function and variables defined in the module in your current code, as well as any aditional modules that the imported module may depend on.

# How to import a module or certain package in python?
# First and foremost we need to install the required module using pip command
# pip install pandas

# now pandas have been installed in our local system, to use it we need to import its

# in our script, at the top we need to type - import module_name; so in our case import pandas
# Remember we should import it at the top of our python script


# From keyword in python - This keyword is used to import only a specified section in certain module
# Eg - pip install math - i have imported a python module named math
from math import pi # - so with the use of from keyword, i have imported a specified functions from the math package 
# so from keyword is used to import certain or specified functions or variables from a module

# Importing everything with the use of * - this is used to import all the functions inside a certain modules

from pandas import * # so here  i have imported all the contents either functions or variables from the modules named pandas. So it is how importing all the functions/variables can be imported using * keyword

# But this is not recommended because it can create confusion, as well as, the size can be bigger as we have imported all those necessary functions that we are not using, os if not in use! why to import? - this is the condition

# `as` keyword - this is used to import certain modules/ variables/ function in short from

import pandas as pan  # so here i have imported modules named pandas as pan, so whenevr i have to use pandas keyword in my program than i can simply write pan inplace of pandas. It is generally useful when we have longer modules/ variables/ function name, we can assign them in short form by the use of as keyword.

# `dir` functions - this function is basically used when we dont know what functions or variables are inside certain modules

import pandas
print(dir(pandas)) 
# so its output will be quite long but you can see...

# ['ArrowDtype', 'BooleanDtype', 'Categorical', 'CategoricalDtype', 'CategoricalIndex', 'DataFrame', 'DateOffset', 'DatetimeIndex', 'DatetimeTZDtype', 'ExcelFile', 'ExcelWriter', 'Flags', 'Float32Dtype', 'Float64Dtype', 'Grouper', 'HDFStore', 'Index', 'IndexSlice', 'Int16Dtype', 'Int32Dtype', 'Int64Dtype', 'Int8Dtype', 'Interval', 'IntervalDtype', 'IntervalIndex', 'MultiIndex', 'NA', 'NaT', 'NamedAgg', 'Period', 'PeriodDtype', 'PeriodIndex', 'RangeIndex', 'Series', 'SparseDtype', 'StringDtype', 'Timedelta', 'TimedeltaIndex', 'Timestamp', 'UInt16Dtype', 'UInt32Dtype', 'UInt64Dtype', 'UInt8Dtype', '__all__', '__builtins__', '__cached__', '__doc__', '__docformat__', '__file__', '__git_version__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_config', '_is_numpy_dev', '_libs', '_testing', '_typing', '_version', 'annotations', 'api', 'array', 'arrays', 'bdate_range', 'compat', 'concat', 'core', 'crosstab', 'cut', 'date_range', 'describe_option', 'errors', 'eval', 'factorize', 'from_dummies', 'get_dummies', 'get_option', 'infer_freq', 'interval_range', 'io', 'isna', 'isnull', 'json_normalize', 'lreshape', 'melt', 'merge', 'merge_asof', 'merge_ordered', 'notna', 'notnull', 'offsets', 'option_context', 'options', 'pandas', 'period_range', 'pivot', 'pivot_table', 'plotting', 'qcut', 'read_clipboard', 'read_csv', 'read_excel', 'read_feather', 'read_fwf', 'read_gbq', 'read_hdf', 'read_html', 'read_json', 'read_orc', 'read_parquet', 'read_pickle', 'read_sas', 'read_spss', 'read_sql', 'read_sql_query', 'read_sql_table', 'read_stata', 'read_table', 'read_xml', 'reset_option', 'set_eng_float_format', 'set_option', 'show_versions', 'test', 'testing', 'timedelta_range', 'to_datetime', 'to_numeric', 'to_pickle', 'to_timedelta', 'tseries', 'unique', 'util', 'value_counts', 'wide_to_long'], 

# so this are all the functions inside a packages named pandas
# this function will list all the different methods available inside specific modules name

#Importing code as module - we can even import our own code from the other python file as package and can use its functions and variables. So i have made a test python file in the same directory (you can see in the contents), and in there i have 2 functions name sum, and diff, and a variable named name, so i have imported them and have used them as well

from test import sum, diff, name
sum()
print(name)

# Imporiting by the use of `*` keyword

from test import *
print(sum()) # does not show anything, coz i havent returned anything in the test file
print(name)

# Importing by the use of `as` kwyword

import test as t # i have imported test as t, now i can use it aswell
print(t.name)
t.sum()

# So in this way import keyword works in python, import keyword is very important especially when working with modules and packages 
# Whether we are working for web development, or working to process a certain image using 
