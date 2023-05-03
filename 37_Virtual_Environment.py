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
# Cmd - source env_name/bin/activate ( for MAC, and LINUX )
# Cmd - env_name/scripts/bin/activate.bat ( for Windows)
# Cmd - env_name/scripts/bin/activate.ps1 ( for Windows and in powershell)


# source/new_env/bin/activate - now it will activate my new_env virtual environment. Now if i want to work on amy libraries over here, then i can install it using the pip command, and work independently

# Now deactivating virtual environment  - we can deactivate the current virtual env by :
# cmd - dectivate

# SO we can install as many libraries we want in our virtual env

# but if we want to know which libraries we have installed in our env, then we can use pip freeze cmmd

# pip freeze - it will show all the libraries,packages,modules that we have installed in that particular virtual environment along with their respective version

# now if we want to store all the information of our packages in a seperate file then we can do it by the use of this command

# pip freeze > text_file_name.txt - now it will create a new txt file that will store all our packages, modules and libraries information.

# NO we have created the packages information in a seperate txt file, now what if a third person using this env wants to install all the packages  that you have installed on your env
# It can be done by a simple command.

# pip install -r text_file_name.txt - now this command will install all the packages specified in that textfile automatically.


# TIPS: What if we want to install older or rpevious libraries version
# for eg : there is an library named xyz and its current version is 3.0
# But what if i want to install previous 2.0 version?
# we can do it by a simple command

# CMD - pip install xyz==2.0 - now it will install the xyz lib with version 2.0, if there is an previous any version already installed in the system or the virtual env, then the interpreter will uninstalled that particular version and install the specified version of the libraries

# So yeah this much for today, today we leaned a very important topic in python that is virtual env, remember virtual env can be very useful when working in certain projects
# So yeah tomorrow we will be learning about PIP in python, how does it works, and all the things about PIP

# 