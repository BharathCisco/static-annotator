import subprocess
import json
import sys
import os


def run_mypy(file_path):
    try:
        result = subprocess.run(
            ["mypy", file_path, "--pretty", "--ignore-missing-imports"],
            capture_output=True,
            text=True
        )
        return {"mypy": result.stdout.strip() or result.stderr.strip()}
    except Exception as e:
        return {"mypy": f"Error: {str(e)}"}


def run_pyright(file_path):
    try:
        result = subprocess.run(
            ["pyright", file_path],
            capture_output=True,
            text=True
        )
        return {"pyright": result.stdout.strip() or result.stderr.strip()}
    except Exception as e:
        return {"pyright": f"Error: {str(e)}"}


def run_pyanalyze(file_path):
    try:
        result = subprocess.run(
            ["pyanalyze", file_path],
            capture_output=True,
            text=True
        )
        output = result.stdout.strip() or result.stderr.strip()
        return {"pyanalyze": output if output else "No issues or output detected."}
    except Exception as e:
        return {"pyanalyze": f"Error: {str(e)}"}


def analyze_file(file_path):
    analysis_results = {}
    analysis_results[file_path] = {
        **run_mypy(file_path),
        **run_pyright(file_path),
        **run_pyanalyze(file_path)
    }
    return analysis_results


def analyze_folder(folder_path):
    all_results = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                all_results.update(analyze_file(file_path))

    # Save results to static_results.json
    with open("task_manager_results.json", "w") as f:
        json.dump(all_results, f, indent=4)

    print(f"Results saved in static_results.json for all Python files in '{folder_path}'.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python annotator_analysis.py <file_or_folder_path>")
        sys.exit(1)

    path = sys.argv[1]

    if os.path.isdir(path):
        analyze_folder(path)
    elif os.path.isfile(path):
        analyze_folder(os.path.dirname(path))
    else:
        print("Invalid path. Please provide a valid file or folder.")
        sys.exit(1)
