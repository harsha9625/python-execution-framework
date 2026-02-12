import sys
from io import StringIO

def run_python_file(file_path, variables: dict):
    try:
        with open(file_path, "r") as f:
            code = f.read()

        exec_globals = dict(variables)

        old_stdout = sys.stdout
        sys.stdout = StringIO()

        exec(code, exec_globals)  
        
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout

        return {
            "returncode": 0,
            "stdout": output,
            "stderr": ""
        }

    except Exception as e:
        return {
            "returncode": -1,
            "stdout": "",
            "stderr": str(e)
        }
