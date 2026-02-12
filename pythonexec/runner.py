import json
from pyexecutor import run_python_file  
def load_test_cases(json_file):
    with open(json_file, "r") as f:
        return json.load(f)

def compare_outputs(actual, expected):
    return actual.strip() == expected.strip()

def main():
    test_cases = load_test_cases("test_cases.json")
    passed, failed = 0, 0

    for i, case in enumerate(test_cases, 1):
        print(f"\n🧪 Running Test Case #{i}")
        input_vars = case["input"]
        expected_output = case["expected_output"]

        result = run_python_file("sample_script.py", input_vars)

        if result["returncode"] != 0:
            print(f"  ❌ Error running script: {result['stderr']}")
            failed += 1
            continue

        actual_output = result["stdout"]

        if compare_outputs(actual_output, expected_output):
            print(f"  ✅ Passed")
            passed += 1
        else:
            print(f"  ❌ Failed")
            print(f"     Expected: {repr(expected_output)}")
            print(f"     Got:      {repr(actual_output)}")
            failed += 1

    print(f"\n📊 Summary: ✅ {passed} Passed, ❌ {failed} Failed")

if __name__ == "__main__":
    main()
