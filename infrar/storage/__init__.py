"""
Object storage operations for Infrar.

This module provides cloud-agnostic object storage operations. Functions defined here
are transformed at deployment time to use the native SDK of your target cloud provider.

Supported Providers:
    - AWS S3
    - GCP Cloud Storage
    - Azure Blob Storage (coming soon)

Operations:
    - upload: Upload a file to object storage
    - download: Download a file from object storage
    - delete: Delete an object from storage
    - list_objects: List objects in a bucket with optional prefix

Example:
    >>> from infrar.storage import upload, download, list_objects
    >>>
    >>> # Upload a file
    >>> upload(bucket='my-data', source='report.csv', destination='reports/2024/report.csv')
    >>>
    >>> # Download a file
    >>> download(bucket='my-data', source='reports/2024/report.csv', destination='local-report.csv')
    >>>
    >>> # List objects
    >>> objects = list_objects(bucket='my-data', prefix='reports/')
    >>> print(objects)

Note:
    These functions are stubs that are transformed away at deployment time.
    The actual implementation depends on your target cloud provider.
"""

from typing import List, Optional

__all__ = ["upload", "download", "delete", "list_objects"]


def upload(bucket: str, source: str, destination: str) -> None:
    """
    Upload a file to object storage.

    This function is transformed at deployment time to use the native SDK of your
    target cloud provider:
        - AWS: boto3.client('s3').upload_file()
        - GCP: storage.Client().bucket().blob().upload_from_filename()
        - Azure: BlobServiceClient().get_blob_client().upload_blob()

    Args:
        bucket: Name of the storage bucket
        source: Local file path to upload
        destination: Destination path/key in the bucket

    Returns:
        None

    Raises:
        FileNotFoundError: If source file doesn't exist (in local dev mode)
        PermissionError: If insufficient permissions (in local dev mode)

    Example:
        >>> upload(
        ...     bucket='analytics-data',
        ...     source='/tmp/report.csv',
        ...     destination='reports/2024-10/report.csv'
        ... )

    Note:
        In production, this function is completely replaced by provider-specific code.
        No runtime overhead exists.
    """
    # This is a stub that will be transformed away at deployment time
    # For local development, you can optionally implement actual cloud SDK calls
    # or use a mock implementation
    raise NotImplementedError(
        "This function is transformed at deployment time. "
        "For local development, set INFRAR_PROVIDER environment variable "
        "or install provider-specific extras: pip install infrar[aws]"
    )


def download(bucket: str, source: str, destination: str) -> None:
    """
    Download a file from object storage.

    This function is transformed at deployment time to use the native SDK of your
    target cloud provider:
        - AWS: boto3.client('s3').download_file()
        - GCP: storage.Client().bucket().blob().download_to_filename()
        - Azure: BlobServiceClient().get_blob_client().download_blob()

    Args:
        bucket: Name of the storage bucket
        source: Object key/path in the bucket to download
        destination: Local file path where the file will be saved

    Returns:
        None

    Raises:
        FileNotFoundError: If object doesn't exist (in local dev mode)
        PermissionError: If insufficient permissions (in local dev mode)

    Example:
        >>> download(
        ...     bucket='analytics-data',
        ...     source='reports/2024-10/report.csv',
        ...     destination='/tmp/downloaded-report.csv'
        ... )

    Note:
        The destination directory must exist. The function will overwrite
        existing files without warning.
    """
    raise NotImplementedError(
        "This function is transformed at deployment time. "
        "For local development, set INFRAR_PROVIDER environment variable "
        "or install provider-specific extras: pip install infrar[aws]"
    )


def delete(bucket: str, path: str) -> None:
    """
    Delete an object from storage.

    This function is transformed at deployment time to use the native SDK of your
    target cloud provider:
        - AWS: boto3.client('s3').delete_object()
        - GCP: storage.Client().bucket().blob().delete()
        - Azure: BlobServiceClient().get_blob_client().delete_blob()

    Args:
        bucket: Name of the storage bucket
        path: Object key/path to delete

    Returns:
        None

    Raises:
        PermissionError: If insufficient permissions (in local dev mode)

    Example:
        >>> delete(
        ...     bucket='temporary-data',
        ...     path='temp/processing-file.csv'
        ... )

    Note:
        This operation is idempotent - deleting a non-existent object
        typically doesn't raise an error on most cloud providers.
    """
    raise NotImplementedError(
        "This function is transformed at deployment time. "
        "For local development, set INFRAR_PROVIDER environment variable "
        "or install provider-specific extras: pip install infrar[aws]"
    )


def list_objects(bucket: str, prefix: str = "") -> List[str]:
    """
    List objects in a bucket, optionally filtered by prefix.

    This function is transformed at deployment time to use the native SDK of your
    target cloud provider:
        - AWS: boto3.client('s3').list_objects_v2()
        - GCP: storage.Client().list_blobs()
        - Azure: ContainerClient().list_blobs()

    Args:
        bucket: Name of the storage bucket
        prefix: Optional prefix to filter objects (e.g., 'reports/2024/')

    Returns:
        List of object keys/paths in the bucket

    Raises:
        PermissionError: If insufficient permissions (in local dev mode)

    Example:
        >>> # List all objects
        >>> all_objects = list_objects(bucket='my-data')
        >>> print(all_objects)
        ['file1.txt', 'reports/report1.csv', 'reports/report2.csv']
        >>>
        >>> # List objects with prefix
        >>> reports = list_objects(bucket='my-data', prefix='reports/')
        >>> print(reports)
        ['reports/report1.csv', 'reports/report2.csv']

    Note:
        Large buckets may return thousands of objects. Consider using
        pagination or more specific prefixes in production.
    """
    raise NotImplementedError(
        "This function is transformed at deployment time. "
        "For local development, set INFRAR_PROVIDER environment variable "
        "or install provider-specific extras: pip install infrar[aws]"
    )
