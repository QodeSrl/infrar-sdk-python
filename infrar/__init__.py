"""
Infrar Python SDK - Write cloud-agnostic infrastructure code.

This SDK provides provider-agnostic APIs for cloud infrastructure operations.
At deployment time, your code is transformed to use native cloud provider SDKs
(boto3 for AWS, google-cloud-storage for GCP, azure-storage-blob for Azure).

Example:
    >>> from infrar.storage import upload
    >>> upload(bucket='my-bucket', source='data.csv', destination='backup/data.csv')

The above code will be transformed to:
    - AWS: boto3.client('s3').upload_file(...)
    - GCP: storage.Client().bucket(...).blob(...).upload_from_filename(...)
    - Azure: BlobServiceClient(...).get_blob_client(...).upload_blob(...)
"""

__version__ = "0.1.0"
__author__ = "Infrar Team"
__email__ = "support@infrar.io"
__license__ = "Apache License 2.0"

# Re-export commonly used modules
from infrar import storage

__all__ = ["storage", "__version__"]
