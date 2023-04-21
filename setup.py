import cx_Freeze

executables = [cx_Freeze.Executable("index.py")]

cx_Freeze.setup(
    name="Guess My Number",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["GAME.PNG"]}},
    executables = executables

    )