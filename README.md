# Infrar Python SDK

**Write cloud-agnostic code that transforms to AWS, GCP, or Azure at deployment time**

## 🚧 Status: Coming Soon (Next Priority)

This repository will contain the Python SDK that developers import in their applications. The SDK provides provider-agnostic APIs for cloud infrastructure operations.

## 📦 Planned Structure

```python
# What you'll be able to write
from infrar.storage import upload, download, delete, list_objects

upload(bucket='my-bucket', source='data.csv', destination='backups/data.csv')
```

This code will be transformed at deployment time to native provider SDKs (boto3 for AWS, google-cloud-storage for GCP, etc.) by the [infrar-engine](https://github.com/QodeSrl/infrar-engine).

## 🎯 What's Available Now

While this SDK is being developed, you can already:

1. **Use the transformation engine** - [infrar-engine](https://github.com/QodeSrl/infrar-engine) is fully functional
2. **Test transformations** - Try the CLI tool to see how code transforms
3. **View transformation rules** - Check [infrar-plugins](https://github.com/QodeSrl/infrar-plugins) for AWS and GCP storage operations

## 📋 Planned Features (MVP)

**Storage Module** (`infrar.storage`):
- `upload(bucket, source, destination)` - Upload file to object storage
- `download(bucket, source, destination)` - Download file from storage
- `delete(bucket, path)` - Delete object
- `list_objects(bucket, prefix='')` - List objects in bucket

**Future Modules**:
- `infrar.database` - Database operations (Phase 2)
- `infrar.messaging` - Queue and pub/sub (Phase 2)
- `infrar.compute` - Container deployment (Phase 2)

## 🔗 Related Repositories

- [infrar-engine](https://github.com/QodeSrl/infrar-engine) - ✅ Transformation engine (working!)
- [infrar-plugins](https://github.com/QodeSrl/infrar-plugins) - ✅ Transformation rules (working!)
- [infrar-docs](https://github.com/QodeSrl/infrar-docs) - ✅ Documentation
- [infrar-cli](https://github.com/QodeSrl/infrar-cli) - 🚧 Command-line tool

## 📅 Timeline

This SDK is next in development queue. Expected completion: Within 1 week.

Follow progress in [Phase 1 MVP](https://github.com/QodeSrl/infrar-docs/blob/main/mvp/phase-1.md).

## 📄 License

Apache License 2.0

---

**Part of the Infrar project** - Infrastructure Intelligence for the multi-cloud era
