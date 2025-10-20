"""Tests for infrar.storage module."""

import pytest
from infrar.storage import upload, download, delete, list_objects


class TestStorageImports:
    """Test that storage module imports correctly."""

    def test_import_storage_module(self):
        """Test importing storage module."""
        import infrar.storage

        assert infrar.storage is not None

    def test_import_functions(self):
        """Test that all functions can be imported."""
        from infrar.storage import upload, download, delete, list_objects

        assert callable(upload)
        assert callable(download)
        assert callable(delete)
        assert callable(list_objects)

    def test_functions_have_docstrings(self):
        """Test that all functions have docstrings."""
        assert upload.__doc__ is not None
        assert download.__doc__ is not None
        assert delete.__doc__ is not None
        assert list_objects.__doc__ is not None

    def test_module_has_all(self):
        """Test that __all__ is defined."""
        import infrar.storage

        assert hasattr(infrar.storage, "__all__")
        assert "upload" in infrar.storage.__all__
        assert "download" in infrar.storage.__all__
        assert "delete" in infrar.storage.__all__
        assert "list_objects" in infrar.storage.__all__


class TestStorageFunctions:
    """Test storage function signatures and behavior."""

    def test_upload_signature(self):
        """Test upload function signature."""
        # Upload should raise NotImplementedError when called
        # (since it's transformed away at deployment)
        with pytest.raises(NotImplementedError):
            upload(bucket="test", source="file.txt", destination="dest.txt")

    def test_download_signature(self):
        """Test download function signature."""
        with pytest.raises(NotImplementedError):
            download(bucket="test", source="file.txt", destination="dest.txt")

    def test_delete_signature(self):
        """Test delete function signature."""
        with pytest.raises(NotImplementedError):
            delete(bucket="test", path="file.txt")

    def test_list_objects_signature(self):
        """Test list_objects function signature."""
        with pytest.raises(NotImplementedError):
            list_objects(bucket="test")

    def test_list_objects_with_prefix(self):
        """Test list_objects with optional prefix parameter."""
        with pytest.raises(NotImplementedError):
            list_objects(bucket="test", prefix="folder/")


class TestStorageDocumentation:
    """Test documentation quality."""

    def test_upload_has_examples(self):
        """Test that upload docstring contains examples."""
        assert "Example:" in upload.__doc__

    def test_download_has_examples(self):
        """Test that download docstring contains examples."""
        assert "Example:" in download.__doc__

    def test_functions_document_transformation(self):
        """Test that functions document their transformation behavior."""
        assert "transformed" in upload.__doc__.lower()
        assert "transformed" in download.__doc__.lower()
        assert "transformed" in delete.__doc__.lower()
        assert "transformed" in list_objects.__doc__.lower()

    def test_functions_list_providers(self):
        """Test that functions list supported providers."""
        for func in [upload, download, delete, list_objects]:
            docstring = func.__doc__.lower()
            assert "aws" in docstring or "s3" in docstring
            assert "gcp" in docstring or "cloud storage" in docstring


class TestPackageStructure:
    """Test package structure and metadata."""

    def test_infrar_package_imports(self):
        """Test that infrar package can be imported."""
        import infrar

        assert infrar is not None

    def test_infrar_has_version(self):
        """Test that infrar package has version."""
        import infrar

        assert hasattr(infrar, "__version__")
        assert isinstance(infrar.__version__, str)
        assert len(infrar.__version__) > 0

    def test_storage_accessible_from_infrar(self):
        """Test that storage module is accessible from infrar."""
        import infrar

        assert hasattr(infrar, "storage")

    def test_can_import_from_top_level(self):
        """Test various import styles."""
        # Style 1: from infrar import storage
        from infrar import storage

        assert storage is not None

        # Style 2: from infrar.storage import upload
        from infrar.storage import upload

        assert callable(upload)

        # Style 3: import infrar.storage
        import infrar.storage

        assert hasattr(infrar.storage, "upload")
