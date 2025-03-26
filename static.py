import subprocess
import json
import sys


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
        # Capture both stdout and stderr for errors or warnings
        output = result.stdout.strip() or result.stderr.strip()
        return {"pyanalyze": output if output else "No issues or output detected."}
    except Exception as e:
        return {"pyanalyze": f"Error: {str(e)}"}


def analyze_file(file_path):
    analysis_results = {}
    analysis_results.update(run_mypy(file_path))
    analysis_results.update(run_pyright(file_path))
    analysis_results.update(run_pyanalyze(file_path))

    # Save results to static_results.json
    with open("static_results.json", "w") as f:
        json.dump(analysis_results, f, indent=4)

    print("Results saved in static_results.json")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python annotator_analysis.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_file(file_path)

