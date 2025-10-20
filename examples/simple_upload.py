#!/usr/bin/env python3
"""
Simple file upload example using Infrar SDK.

This example shows the most basic usage: uploading a single file to object storage.
The code will be transformed to use native cloud provider SDKs at deployment time.
"""

from infrar.storage import upload


def main():
    """Upload a file to cloud storage."""
    # Upload a report file
    upload(
        bucket="analytics-reports",
        source="monthly-report.csv",
        destination="reports/2024/october/monthly-report.csv",
    )

    print("✅ File uploaded successfully!")
    print("Location: reports/2024/october/monthly-report.csv")


if __name__ == "__main__":
    main()
