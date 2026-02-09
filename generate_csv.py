#!/usr/bin/env python3
"""Parse README.md and generate features.csv with Category column from section headers."""

import csv
import re

def parse_readme(readme_path):
    with open(readme_path, "r") as f:
        lines = f.readlines()

    rows = []
    current_category = None

    for line in lines:
        line = line.rstrip("\n")

        # Detect ## headers as category
        header_match = re.match(r"^## (.+)$", line)
        if header_match:
            current_category = header_match.group(1).strip()
            continue

        # Skip table header and separator rows
        if line.startswith("|") and ("Feature" in line and "Description" in line):
            continue
        if line.startswith("|") and re.match(r"^\|[-| ]+\|$", line):
            continue

        # Parse table data rows
        if line.startswith("|") and current_category:
            cells = [c.strip() for c in line.split("|")]
            # split("|") gives empty strings at start/end
            cells = [c for c in cells if c != "" or cells.index(c) not in (0, len(cells) - 1)]
            # More robust: just strip the leading/trailing pipes and split
            inner = line.strip("|")
            cells = [c.strip() for c in inner.split("|")]

            if len(cells) < 6:
                continue

            feature_raw = cells[0]
            description = cells[1]
            status = cells[2]
            risk_human = cells[3]
            risk_ai = cells[4]
            source = cells[5]
            last_checked = cells[6] if len(cells) > 6 else ""

            # Parse feature name and URL from markdown link
            link_match = re.match(r"\[(.+?)\]\((.+?)\)", feature_raw)
            if link_match:
                feature_name = link_match.group(1)
                feature_url = link_match.group(2)
            else:
                feature_name = feature_raw
                feature_url = ""

            rows.append({
                "Category": current_category,
                "Feature": feature_name,
                "URL": feature_url,
                "Description": description,
                "Status (Azure)": status,
                "Risk Assessment (Human)": risk_human,
                "Risk Assessment (AI)": risk_ai,
                "Source": source,
                "Last Checked": last_checked,
            })

    return rows


def write_csv(rows, output_path):
    fieldnames = [
        "Category",
        "Feature",
        "URL",
        "Description",
        "Status (Azure)",
        "Risk Assessment (Human)",
        "Risk Assessment (AI)",
        "Source",
        "Last Checked",
    ]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    rows = parse_readme("README.md")
    write_csv(rows, "features.csv")
    print(f"Wrote {len(rows)} features to features.csv")
