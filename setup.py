import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smart-pythonistic", # Replace with your own username
    version="0.0.1",
    author="Caroline Silva",
    author_email="carolvicente.tec@gmail.com",
    description="Personal python package with helpful snippets for pyspark features.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carolvicente/simpler-pyspark",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)