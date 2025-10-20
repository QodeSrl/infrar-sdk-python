#!/usr/bin/env python3
"""
File backup example using Infrar SDK.

This example shows how to create a simple backup system that:
- Uploads multiple files to a backup bucket
- Lists existing backups
- Demonstrates deletion of old backups

Deploy this to AWS, GCP, or Azure - same code works everywhere!
"""

from datetime import datetime
from pathlib import Path
from infrar.storage import upload, delete, list_objects


def backup_files(files_to_backup: list[str], bucket: str) -> None:
    """Backup multiple files to cloud storage."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    print(f"🔄 Starting backup at {timestamp}...")

    for file_path in files_to_backup:
        file = Path(file_path)
        if not file.exists():
            print(f"⚠️  Skipping {file_path} (not found)")
            continue

        # Create timestamped backup path
        backup_path = f"backups/{timestamp}/{file.name}"

        upload(bucket=bucket, source=file_path, destination=backup_path)

        print(f"✅ Backed up: {file.name} → {backup_path}")


def list_backups(bucket: str) -> list[str]:
    """List all backup files."""
    backups = list_objects(bucket=bucket, prefix="backups/")
    return backups


def cleanup_old_backups(bucket: str, keep_latest: int = 5) -> None:
    """Delete old backups, keeping only the latest N."""
    all_backups = list_backups(bucket)

    # Group by timestamp (assuming format: backups/TIMESTAMP/file.ext)
    timestamps = set()
    for backup in all_backups:
        parts = backup.split("/")
        if len(parts) >= 2:
            timestamps.add(parts[1])

    # Sort and identify old backups to delete
    sorted_timestamps = sorted(timestamps, reverse=True)
    if len(sorted_timestamps) <= keep_latest:
        print(f"📦 Only {len(sorted_timestamps)} backup(s) exist, nothing to clean up")
        return

    old_timestamps = sorted_timestamps[keep_latest:]

    print(f"🗑️  Cleaning up {len(old_timestamps)} old backup(s)...")

    for backup in all_backups:
        for old_ts in old_timestamps:
            if f"backups/{old_ts}/" in backup:
                delete(bucket=bucket, path=backup)
                print(f"  Deleted: {backup}")


def main():
    """Run backup operations."""
    bucket = "my-backups"

    # Files to backup
    files = [
        "/etc/config.json",
        "/var/log/app.log",
        "/data/important-data.csv",
    ]

    # Perform backup
    backup_files(files, bucket)

    # List all backups
    print("\n📋 Current backups:")
    backups = list_backups(bucket)
    for backup in backups[:10]:  # Show first 10
        print(f"  - {backup}")

    if len(backups) > 10:
        print(f"  ... and {len(backups) - 10} more")

    # Cleanup old backups
    print()
    cleanup_old_backups(bucket, keep_latest=5)

    print("\n✅ Backup completed!")


if __name__ == "__main__":
    main()
