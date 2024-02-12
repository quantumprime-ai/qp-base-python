
# Introduction to the QuantumPrime formula

You can import the files located in the src folder into [Jupyter Notebooks](https://jupyter.org/try-jupyter/lab/index.html)

Additionally, you can execute them in Visual Studio Code (VS Code) by ensuring that sympy is correctly installed and configured in your Python environment.

## Step 1: Install Sympy

You must install the `sympy` library in your Python environment. Follow these steps to install `sympy` using the integrated terminal in VS Code:

1. Open VS Code.
2. Open the Terminal in VS Code by going to the top menu and selecting `Terminal -> New Terminal`.
3. To ensure successful use of `sympy` in Visual Studio Code (VS Code) with Python 3.10, follow these steps:
4. 
- Make sure you are using the correct version of Python by running `python3 --version` or `python3.10 --version`. If not, you might need to adjust your environment variables or use a virtual environment for Python 3.10.x.
- Install `sympy` for Python 3.10.x with the command:
  ```
  python3 -m pip install sympy
  ```
  or if you have a specific alias for Python 3.10, you might need to use something like:
  ```
  python3.10 -m pip install sympy
  ```


## Step 2: Select the Correct Python Interpreter

After installing `sympy`, make sure that VS Code is using the Python interpreter where `sympy` is installed:

1. Open the Command Palette in VS Code by pressing `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS).
2. Type `Python: Select Interpreter` and select it by pressing `Enter`.
3. Choose the Python interpreter that you used to install `sympy`. If you installed it in a virtual environment, select the interpreter located inside your project's `venv` folder.

## Step 3: Run Your Code

With `sympy` installed and the correct interpreter selected, you should now be able to run your Python code in VS Code without encountering the import error for `sympy`.

## Troubleshooting

If you continue to experience issues, consider these troubleshooting steps:

- **Check Installation**: Verify that `sympy` is installed correctly by running `pip show sympy` in the terminal. This command should display information about the installed `sympy` package.
- **Python Environment**: Ensure you're working in the correct Python environment, especially if using virtual environments. Each environment has its own set of installed packages.
- **Restart VS Code**: Sometimes, VS Code needs to be restarted for changes in the environment or installed packages to be recognized.

Follow these steps to ensure `sympy` is correctly set up in your VS Code environment, allowing for successful code execution.
