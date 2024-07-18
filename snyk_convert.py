import csv
import re
import sys
import os

def parse_findings(file_name):
    # Read the findings from the file
    with open(file_name, 'r') as file:
        findings = file.read()
        print(f"Read file '{file_name}' content:\n{findings}\n")

    # Define the regex patterns to extract the required fields
    severity_pattern = re.compile(r'✗ \[(.*?)\]')
    finding_pattern = re.compile(r'✗ \[.*?\] (.*?)\n')
    path_pattern = re.compile(r'Path: (.*?), line (\d+)')
    info_pattern = re.compile(r'Info: (.*?)\s*(?=\n✗|\Z)', re.DOTALL)

    # Parse the findings
    parsed_findings = []
    for finding in findings.strip().split('\n\n'):
        print(f"Processing finding block:\n{finding}\n")

        severity_match = severity_pattern.search(finding)
        if severity_match:
            severity = severity_match.group(1)
            print(f"Matched Severity: {severity}")
        else:
            print("Failed to match Severity")

        finding_match = finding_pattern.search(finding)
        if finding_match:
            finding_desc = finding_match.group(1).strip()
            print(f"Matched Finding: {finding_desc}")
        else:
            print("Failed to match Finding")

        path_match = path_pattern.search(finding)
        if path_match:
            path = path_match.group(1).strip()
            line = path_match.group(2).strip()
            print(f"Matched Path: {path}, Line: {line}")
        else:
            print("Failed to match Path and Line")

        info_match = info_pattern.search(finding)
        if info_match:
            info = info_match.group(1).strip()
            print(f"Matched Info: {info}")
        else:
            print("Failed to match Info")

        if severity_match and finding_match and path_match and info_match:
            parsed_findings.append([severity, finding_desc, path, line, info])
            print(f"Extracted values - Severity: {severity}, Finding: {finding_desc}, Path: {path}, Line: {line}, Info: {info}\n")
        else:
            print("Regex match failed for this block.\n")

    return parsed_findings

def write_to_csv(parsed_findings, output_file='findings.csv'):
    # Write the parsed findings to a CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Severity', 'Finding', 'Path', 'Line', 'Details'])
        writer.writerows(parsed_findings)

    print(f"CSV file '{output_file}' created successfully.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python convert_findings.py <findings_file>")
        sys.exit(1)

    findings_file = sys.argv[1]

    # Check if the file exists in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, findings_file)

    if not os.path.isfile(file_path):
        print(f"File '{findings_file}' not found in the current directory.")
        sys.exit(1)

    print(f"File '{file_path}' found. Starting processing...\n")
    parsed_findings = parse_findings(file_path)
    write_to_csv(parsed_findings)
