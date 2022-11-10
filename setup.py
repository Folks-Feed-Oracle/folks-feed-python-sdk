import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="folks-feed-python-sdk",
    description="Folks Feed Oracle Python SDK",
    author="Folks Feed Oracle",
    author_email="info@folksfeed.io",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    project_urls={
        "Source": "https://github.com/Folks-Feed-Oracle/folks-feed-python-sdk",
    },
    install_requires=["py-algorand-sdk >= 1.19.0"],
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
)