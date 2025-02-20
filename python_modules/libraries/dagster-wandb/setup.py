from pathlib import Path
from typing import Dict

from setuptools import find_packages, setup


def get_version() -> str:
    version: Dict[str, str] = {}
    with open(Path(__file__).parent / "dagster_wandb/version.py", encoding="utf8") as fp:
        exec(fp.read(), version)

    return version["__version__"]


ver = get_version()
# dont pin dev installs to avoid pip dep resolver issues
pin = "" if ver == "1!0+dev" else f"=={ver}"
setup(
    name="dagster-wandb",
    version=get_version(),
    author="Elementl",
    author_email="hello@elementl.com",
    license="Apache-2.0",
    description="Package for wandb Dagster components.",
    url="https://github.com/dagster-io/dagster/tree/master/python_modules/libraries/dagster-wandb",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=["dagster_wandb_tests*"]),
    install_requires=[
        f"dagster{pin}",
        "wandb>=0.13.5,<0.15.5",
    ],
    extras_require={"dev": ["cloudpickle", "joblib", "callee", "dill"]},
    zip_safe=False,
)
