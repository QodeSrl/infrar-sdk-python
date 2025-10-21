#!/usr/bin/env python
"""Setup script for infrar Python SDK."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the long description from README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="infrar",
    version="0.1.0",
    description="Write cloud-agnostic infrastructure code that transforms to AWS, GCP, or Azure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Infrar Team",
    author_email="support@infrar.io",
    license="Apache License 2.0",
    url="https://github.com/QodeSrl/infrar-sdk-python",
    project_urls={
        "Documentation": "https://docs.infrar.io",
        "Source": "https://github.com/QodeSrl/infrar-sdk-python",
        "Tracker": "https://github.com/QodeSrl/infrar-sdk-python/issues",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples"]),
    python_requires=">=3.8",
    install_requires=[
        # No runtime dependencies - code is transformed away at deployment
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
            "flake8>=6.0.0",
        ],
        # Optional: For local development/testing with actual cloud providers
        "aws": ["boto3>=1.28.0"],
        "gcp": ["google-cloud-storage>=2.10.0"],
        "azure": ["azure-storage-blob>=12.0.0"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Internet",
    ],
    keywords="cloud multi-cloud aws gcp azure infrastructure-as-code portability",
    zip_safe=False,
    include_package_data=True,
)
