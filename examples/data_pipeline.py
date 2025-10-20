#!/usr/bin/env python3
"""
Data pipeline example using Infrar SDK.

This example demonstrates a realistic data processing pipeline:
1. Download raw data from storage
2. Process the data
3. Upload processed results
4. List all result files

This code will work on AWS, GCP, or Azure depending on where you deploy it.
"""

import csv
from pathlib import Path
from infrar.storage import upload, download, list_objects


def process_data(input_file: str, output_file: str) -> None:
    """Process CSV data - example transformation."""
    # Read input
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # Process (example: calculate summary)
    processed = {
        "total_records": len(data),
        "summary": "Data processed successfully",
    }

    # Write output
    with open(output_file, "w") as f:
        f.write(f"Total Records: {processed['total_records']}\n")
        f.write(f"Status: {processed['summary']}\n")


def main():
    """Run the data processing pipeline."""
    bucket = "data-processing"

    # Step 1: Download raw data
    print("📥 Downloading raw data...")
    download(
        bucket=bucket, source="raw/input-data.csv", destination="/tmp/input-data.csv"
    )

    # Step 2: Process the data
    print("⚙️  Processing data...")
    process_data("/tmp/input-data.csv", "/tmp/processed-results.txt")

    # Step 3: Upload results
    print("📤 Uploading results...")
    upload(
        bucket=bucket,
        source="/tmp/processed-results.txt",
        destination="processed/results.txt",
    )

    # Step 4: List all processed files
    print("📋 Listing all processed files...")
    files = list_objects(bucket=bucket, prefix="processed/")
    print(f"Found {len(files)} processed files:")
    for file in files:
        print(f"  - {file}")

    print("\n✅ Pipeline completed successfully!")


if __name__ == "__main__":
    main()
