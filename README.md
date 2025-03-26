# Static Annotation Tools

This repository compares three static annotation tools for Python:

1. **mypy**  
2. **pyright**  
3. **pyanalyze**

---

# Static Annotation Tools Comparison

## 📚 Summary of Findings
- All three tools (**mypy**, **pyright**, and **pyanalyze**) successfully identified issues related to:
    - Undefined variables.
    - Type mismatches in return values.
    - Attribute errors.

---

## 🛠️ Tool Breakdown

### ✔️ MyPy
- Highly customizable using `mypy.ini` to:
    - Ignore paths.
    - Modify strictness.
- Suitable for large-scale projects with gradual typing.

---

### 🚀 Pyright
- Faster than `mypy`.
- Slightly harder to configure for complex projects but provides more accurate type inference.
- Ideal for modern Python projects.

---

### 🔥 Pyanalyze
- Catches import failures.
- Combines static and runtime analysis, making it prone to stopping on runtime errors.
- **Not ideal** for purely static analysis where runtime execution is not desired.

---

## 🏆 Final Verdict: Which Tool to Use?

### 🧠 **For Static Type Checking:**
- ✅ Prefer **mypy** for gradual typing in large projects.
- ⚡️ Use **pyright** for faster and more accurate type inference, especially for modern Python projects.

### 🔎 **For Deeper Runtime Inspection:**
- 🕵️‍♂️ Use **pyanalyze** to complement static analysis when you want to catch runtime type errors that might not be evident statically.

## 📚 Test Results

### ✅ `test_files/static_success.py` Results
```json
{
    "mypy": "Success: no issues found in 1 source file",
    "pyright": "0 errors, 0 warnings, 0 informations",
    "pyanalyze": "No issues or output detected."
}
```
### ✅ `test_files/static_failure.py` Results
```json
{
    "mypy": [
        {
            "file": "test_files\\static_failure.py",
            "line": 11,
            "error": "Name \"unknown_variable\" is not defined",
            "code": "name-defined",
            "snippet": "print(unknown_variable)  #"
        },
        {
            "file": "test_files\\static_failure.py",
            "line": 15,
            "error": "Incompatible return value type (got \"str\", expected \"int\")",
            "code": "return-value",
            "snippet": "return \"Hello, world!\"  #"
        },
        {
            "file": "test_files\\static_failure.py",
            "line": 30,
            "error": "\"Sample\" has no attribute \"age\"",
            "code": "attr-defined",
            "snippet": "print(obj.age)  # age is not defined  #"
        }
    ],
    "pyright": [
        {
            "file": "c:\\Users\\bhamahad\\PycharmProjects\\annotator2\\test_files\\static_failure.py",
            "line": 11,
            "column": 7,
            "error": "\"unknown_variable\" is not defined",
            "code": "reportUndefinedVariable"
        },
        {
            "file": "c:\\Users\\bhamahad\\PycharmProjects\\annotator2\\test_files\\static_failure.py",
            "line": 15,
            "column": 12,
            "error": "Type \"Literal['Hello, world!']\" is not assignable to return type \"int\"",
            "code": "reportReturnType"
        },
        {
            "file": "c:\\Users\\bhamahad\\PycharmProjects\\annotator2\\test_files\\static_failure.py",
            "line": 30,
            "column": 11,
            "error": "Cannot access attribute \"age\" for class \"Sample\"",
            "code": "reportAttributeAccessIssue"
        }
    ],
    "pyanalyze": {
        "error": "Failed to import .\\test_files\\static_failure.py due to TypeError('can only concatenate str (not \"int\") to str')",
        "details": {
            "file": ".\\test_files\\static_failure.py",
            "line": 3,
            "snippet": [
                "1: # sample_test.py",
                "2: ",
                "3: def add_numbers(a, b):",
                "4:     return a + b",
                "5: ",
                "6: "
            ],
            "traceback": [
                "Traceback (most recent call last):",
                "  File \"C:\\Users\\bhamahad\\PycharmProjects\\annotator2\\.venv\\lib\\site-packages\\pyanalyze\\name_check_visitor.py\", line 1314, in _load_module",
                "    return importer.load_module_from_file(",
                "  File \"C:\\Users\\bhamahad\\PycharmProjects\\annotator2\\.venv\\lib\\site-packages\\pyanalyze\\importer.py\", line 102, in load_module_from_file",
                "    return import_module(str(abspath), abspath), False",
                "  File \"C:\\Users\\bhamahad\\PycharmProjects\\annotator2\\.venv\\lib\\site-packages\\pyanalyze\\importer.py\", line 110, in import_module",
                "    spec.loader.exec_module(module)",
                "  File \"<frozen importlib._bootstrap_external>\", line 790, in exec_module",
                "  File \"<frozen importlib._bootstrap>\", line 228, in _call_with_frames_removed",
                "  File \"C:\\Users\\bhamahad\\PycharmProjects\\annotator2\\test_files\\static_failure.py\", line 8, in <module>",
                "    result: int = add_numbers(\"5\", 10)",
                "  File \"C:\\Users\\bhamahad\\PycharmProjects\\annotator2\\test_files\\static_failure.py\", line 4, in add_numbers",
                "    return a + b",
                "TypeError: can only concatenate str (not \"int\") to str"
            ]
        }
    }
}
```

