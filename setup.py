from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML_Based_Book_Recommendation_System"
AUTHOR_USER_NAME = "Hani_Shaikh"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit','numpy']


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Hani_Shaikh",
    description="ML based books recommendation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HNS03/ML-Based-Book-Recommendation-System",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)