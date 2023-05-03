# so today we are going to see about virtual environment in python
# So wht is virtual environment in python ? - in simple words virtual environment in python are python environment whrere libraries, scripts are isolated from the rest of the environment or default
# virtual environment is very useful while managing different packages 
# Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects.
# python virtual environment is used to create an isolated enviroment for managing different packages.

# it is a tool used to isolate specific python env on a single machine, allowing us to work on multiple projects with different dependencies and packages without conflicts.
# they are very useful when working on projects that have conflicting package versions or packages that are not compatible with each other.

# How to install virtual environment in python?

# Cmd - python -m venv virtual_env_name

# python -m venv new_env - so here i have created a new python virtual environment with name new_env. Remember it is completely isolated from the python that is in the system. That means if any libraries is installed on my system previously, and i wanto to work on that libraries inside of this env, that it wont work, because this is a seperate new env, its like a copy of system python

# Now we have created the virtual environment, but how do we activate it?
# Cmd - source/env_name/bin/activate

# source/new_env/bin/activate - now it will activate my new_env virtual environment. Now if i want to work on amy libraries 