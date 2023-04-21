# Guess My Number Game By Pygame made by thanhdat21293@gmail.com
![Guess My Number](GAME.PNG "Guess My Number")


## How to build python to exe file
Guide: https://pythonprogramming.net/converting-pygame-executable-cx_freeze/

#### 1) Install package
```
pip install cx_Freeze
```

#### 2) Create setup.py file and include below code into file
````python
import cx_Freeze

executables = [cx_Freeze.Executable("index.py")]

cx_Freeze.setup(
    name="Guess My Number",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["GAME.PNG"]}},
    executables = executables

    )
````
#### 3) Final, Run cmd below in cmd
```
python setup.py build
```

#### 4) Result, .exe file in build/ folder