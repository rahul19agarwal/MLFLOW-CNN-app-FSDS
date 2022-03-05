from setuptools import setup


## edit below variables as per your requirements -
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["numpy","tqdm"]


setup(
    name=SRC_REPO,
    version="0.0.1",
    description="A small package for MLflow app",
    packages=[SRC_REPO],
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)
