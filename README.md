# Infrar Python SDK

**Write cloud-agnostic infrastructure code that transforms to AWS, GCP, or Azure at deployment time**

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-alpha-yellow)](https://github.com/QodeSrl/infrar-sdk-python)

## 🚀 What is Infrar?

Infrar lets you write cloud infrastructure code once and deploy it to any cloud provider (AWS, GCP, Azure). At deployment time, your code is **transformed** to use native cloud provider SDKs, giving you:

- ✅ **Zero runtime overhead** - Transformed code is pure boto3/google-cloud-storage/azure-storage-blob
- ✅ **True portability** - Same source code, any cloud provider
- ✅ **Full provider features** - No limitations from abstraction
- ✅ **Simple debugging** - Native stack traces, no proxy layers

##  Quick Start

### Installation

```bash
pip install infrar
```

### Write Provider-Agnostic Code

```python
from infrar.storage import upload, download, list_objects

# Upload a file
upload(
    bucket='my-data-bucket',
    source='report.csv',
    destination='reports/2024/report.csv'
)

# Download a file
download(
    bucket='my-data-bucket',
    source='reports/2024/report.csv',
    destination='local-report.csv'
)

# List objects
files = list_objects(bucket='my-data-bucket', prefix='reports/')
print(f"Found {len(files)} reports")
```

### Deploy to Any Cloud

**Deploy to AWS** → Transformed to boto3:
```python
import boto3
s3 = boto3.client('s3')
s3.upload_file('report.csv', 'my-data-bucket', 'reports/2024/report.csv')
```

**Deploy to GCP** → Transformed to google-cloud-storage:
```python
from google.cloud import storage
storage_client = storage.Client()
bucket = storage_client.bucket('my-data-bucket')
blob = bucket.blob('reports/2024/report.csv')
blob.upload_from_filename('report.csv')
```

**Deploy to Azure** → Transformed to azure-storage-blob (coming soon)

## 📦 Features

### Storage Module (`infrar.storage`)

Cloud-agnostic object storage operations:

| Function | Description | AWS | GCP | Azure |
|----------|-------------|-----|-----|-------|
| `upload(bucket, source, destination)` | Upload file to storage | ✅ S3 | ✅ Cloud Storage | 🔜 Blob |
| `download(bucket, source, destination)` | Download file from storage | ✅ S3 | ✅ Cloud Storage | 🔜 Blob |
| `delete(bucket, path)` | Delete object | ✅ S3 | ✅ Cloud Storage | 🔜 Blob |
| `list_objects(bucket, prefix='')` | List objects in bucket | ✅ S3 | ✅ Cloud Storage | 🔜 Blob |

### Coming Soon

- `infrar.database` - Relational database operations (RDS, Cloud SQL, Azure SQL)
- `infrar.messaging` - Queue and pub/sub (SQS, Pub/Sub, Service Bus)
- `infrar.compute` - Container deployment (ECS, Cloud Run, Container Apps)

## 📚 Examples

### Simple File Upload

```python
from infrar.storage import upload

upload(
    bucket='backups',
    source='/var/log/app.log',
    destination='logs/2024-10-20/app.log'
)
```

### Data Processing Pipeline

```python
from infrar.storage import upload, download, list_objects

# Download raw data
download(
    bucket='data-processing',
    source='raw/input.csv',
    destination='/tmp/input.csv'
)

# Process data (your custom logic)
process_data('/tmp/input.csv', '/tmp/output.csv')

# Upload results
upload(
    bucket='data-processing',
    source='/tmp/output.csv',
    destination='processed/output.csv'
)

# List all processed files
files = list_objects(bucket='data-processing', prefix='processed/')
print(f"Processed files: {files}")
```

### File Backup System

```python
from datetime import datetime
from infrar.storage import upload, list_objects, delete

def backup_files(files, bucket):
    """Backup files with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

    for file_path in files:
        backup_path = f"backups/{timestamp}/{Path(file_path).name}"
        upload(bucket=bucket, source=file_path, destination=backup_path)
        print(f"✅ Backed up: {file_path}")

def cleanup_old_backups(bucket, keep_latest=5):
    """Keep only latest N backups."""
    all_backups = list_objects(bucket=bucket, prefix="backups/")

    # Group by timestamp and delete old ones
    timestamps = sorted(set(b.split('/')[1] for b in all_backups), reverse=True)
    old_timestamps = timestamps[keep_latest:]

    for backup in all_backups:
        if any(f"backups/{ts}/" in backup for ts in old_timestamps):
            delete(bucket=bucket, path=backup)
            print(f"🗑️  Deleted old backup: {backup}")
```

See [examples/](examples/) for more complete examples.

## 🛠️ How It Works

### 1. Write Code with Infrar SDK

You write provider-agnostic code using the Infrar SDK:

```python
from infrar.storage import upload
upload(bucket='data', source='file.csv', destination='backup/file.csv')
```

### 2. Transform at Deployment

The [infrar-engine](https://github.com/QodeSrl/infrar-engine) transforms your code for your target provider:

```bash
infrar transform --provider aws --input app.py --output app_aws.py
```

### 3. Deploy Native Code

The transformed code uses native cloud provider SDKs with **zero runtime overhead**:

```python
# Deployed to AWS (no infrar dependency!)
import boto3
s3 = boto3.client('s3')
s3.upload_file('file.csv', 'data', 'backup/file.csv')
```

## 🧪 Development & Testing

### Running Tests

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=infrar --cov-report=term-missing
```

### Local Development

For local development/testing with actual cloud providers:

```bash
# Install with AWS support
pip install infrar[aws]

# Install with GCP support
pip install infrar[gcp]

# Install with all providers
pip install infrar[aws,gcp,azure]
```

## ⚠️ Known Limitations (v0.1.0)

The current MVP has a few limitations when writing code for transformation:

### 1. Comments in Functions

**Issue**: Comments inside functions containing infrar calls may cause syntax errors during transformation.

**Example that may fail**:
```python
def upload_data():
    # Upload the file to storage
    upload(bucket='data', source='file.csv', destination='backup.csv')
```

**Workaround**: Remove inline comments before transformation, or add them after:
```python
def upload_data():
    upload(bucket='data', source='file.csv', destination='backup.csv')
```

### 2. Variable Assignments with list_objects()

**Issue**: Assigning the result of `list_objects()` to a variable isn't fully supported yet.

**Example that may not work**:
```python
files = list_objects(bucket='data', prefix='reports/')
print(files)
```

**Workaround**: For MVP testing, call without assignment or handle in post-transformation.

### 3. Recommended Patterns

For best results with the current MVP:

✅ **DO**: Use simple, direct function calls
```python
upload(bucket='data', source='file.csv', destination='backup.csv')
download(bucket='data', source='result.csv', destination='output.csv')
```

✅ **DO**: Use functions without inline comments
```python
def process_data():
    upload(bucket='data', source='input.csv', destination='processed/input.csv')
    download(bucket='data', source='output.csv', destination='result.csv')
```

✅ **DO**: Use multi-line arguments
```python
upload(
    bucket='analytics-bucket',
    source='report.csv',
    destination='reports/2024/report.csv'
)
```

❌ **AVOID**: Inline comments in functions with infrar calls
❌ **AVOID**: Variable assignments with list_objects() for now

These limitations will be addressed in future releases. See [infrar-engine issues](https://github.com/QodeSrl/infrar-engine/issues) for status updates.

## 📖 API Reference

### infrar.storage.upload()

Upload a file to object storage.

```python
def upload(bucket: str, source: str, destination: str) -> None
```

**Parameters:**
- `bucket` (str): Name of the storage bucket
- `source` (str): Local file path to upload
- `destination` (str): Destination path/key in the bucket

**Example:**
```python
upload(
    bucket='analytics-data',
    source='/tmp/report.csv',
    destination='reports/2024-10/report.csv'
)
```

### infrar.storage.download()

Download a file from object storage.

```python
def download(bucket: str, source: str, destination: str) -> None
```

**Parameters:**
- `bucket` (str): Name of the storage bucket
- `source` (str): Object key/path in the bucket to download
- `destination` (str): Local file path where the file will be saved

**Example:**
```python
download(
    bucket='analytics-data',
    source='reports/2024-10/report.csv',
    destination='/tmp/downloaded-report.csv'
)
```

### infrar.storage.delete()

Delete an object from storage.

```python
def delete(bucket: str, path: str) -> None
```

**Parameters:**
- `bucket` (str): Name of the storage bucket
- `path` (str): Object key/path to delete

**Example:**
```python
delete(
    bucket='temporary-data',
    path='temp/processing-file.csv'
)
```

### infrar.storage.list_objects()

List objects in a bucket, optionally filtered by prefix.

```python
def list_objects(bucket: str, prefix: str = "") -> List[str]
```

**Parameters:**
- `bucket` (str): Name of the storage bucket
- `prefix` (str): Optional prefix to filter objects (e.g., 'reports/2024/')

**Returns:**
- `List[str]`: List of object keys/paths in the bucket

**Example:**
```python
# List all objects
all_objects = list_objects(bucket='my-data')

# List objects with prefix
reports = list_objects(bucket='my-data', prefix='reports/')
```

## 🔗 Related Projects

- [infrar-engine](https://github.com/QodeSrl/infrar-engine) - Transformation engine (Go)
- [infrar-plugins](https://github.com/QodeSrl/infrar-plugins) - Transformation rules for AWS, GCP, Azure
- [infrar-cli](https://github.com/QodeSrl/infrar-cli) - Command-line tool
- [infrar-docs](https://github.com/QodeSrl/infrar-docs) - Documentation

## 🤝 Contributing

We welcome contributions! Areas where you can help:

- 🐛 Report bugs or issues
- 💡 Suggest new features or improvements
- 📖 Improve documentation
- ✨ Add new capabilities (database, messaging, etc.)
- 🧪 Write more tests

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

Apache License 2.0 - see [LICENSE](LICENSE) file for details.

## 📞 Support

- **Documentation**: https://docs.infrar.io
- **Issues**: https://github.com/QodeSrl/infrar-sdk-python/issues
- **Email**: support@infrar.io

## 🎯 Roadmap

- [x] Storage module (upload, download, delete, list_objects)
- [x] AWS S3 support
- [x] GCP Cloud Storage support
- [ ] Azure Blob Storage support
- [ ] Database module (RDS, Cloud SQL, Azure SQL)
- [ ] Messaging module (SQS, Pub/Sub, Service Bus)
- [ ] Compute module (ECS, Cloud Run, Container Apps)
- [ ] Node.js SDK
- [ ] Go SDK

## ⭐ Why Infrar?

**Traditional approach** (runtime abstraction):
- ❌ Runtime overhead from proxy layers
- ❌ Feature limitations (lowest common denominator)
- ❌ Complex debugging (multiple abstraction layers)
- ❌ Performance compromises

**Infrar approach** (compile-time transformation):
- ✅ Zero runtime overhead (native SDK code)
- ✅ Full provider features (no limitations)
- ✅ Simple debugging (native stack traces)
- ✅ Native performance (direct SDK calls)

---

**Made with ❤️ by the Infrar Team**

[Website](https://infrar.io) • [Documentation](https://docs.infrar.io) • [GitHub](https://github.com/QodeSrl/infrar-sdk-python)
