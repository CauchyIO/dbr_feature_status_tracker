#!/usr/bin/env python3
"""Fetch comment counts for all GitHub Discussions and write discussion-counts.json."""

import json
import subprocess
import sys


def fetch_discussions(owner, repo, category_id):
    """Fetch all discussions with comment counts using gh api graphql with pagination."""
    counts = {}
    cursor = None

    while True:
        after_clause = f', after: "{cursor}"' if cursor else ""
        query = f"""{{
          repository(owner: "{owner}", name: "{repo}") {{
            discussions(first: 100, categoryId: "{category_id}"{after_clause}) {{
              totalCount
              pageInfo {{ hasNextPage endCursor }}
              nodes {{
                title
                comments {{ totalCount }}
                reactions {{ totalCount }}
              }}
            }}
          }}
        }}"""

        result = subprocess.run(
            ["gh", "api", "graphql", "-f", f"query={query}"],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print(f"Error: {result.stderr}", file=sys.stderr)
            sys.exit(1)

        data = json.loads(result.stdout)
        discussions = data["data"]["repository"]["discussions"]

        for node in discussions["nodes"]:
            counts[node["title"]] = {
                "comments": node["comments"]["totalCount"],
                "reactions": node["reactions"]["totalCount"],
            }

        if not discussions["pageInfo"]["hasNextPage"]:
            break
        cursor = discussions["pageInfo"]["endCursor"]

    return counts


if __name__ == "__main__":
    counts = fetch_discussions(
        owner="CauchyIO",
        repo="dbr_feature_status_tracker",
        category_id="DIC_kwDORJj__s4C2FlB",
    )

    with open("discussion-counts.json", "w") as f:
        json.dump(counts, f, indent=2)

    total = sum(c["comments"] for c in counts.values())
    print(f"Wrote counts for {len(counts)} discussions ({total} total comments)")
