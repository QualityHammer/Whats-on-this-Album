import setuptools
from scrape_songs.__version__ import __version__

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="scrape-songs",
    version=__version__,

    python_requires=">=3.7",
    install_requires=['scrapy', 'wikipedia'],

    description="A tool used to collect lists of song" \
            " names from albums on wikipedia and format them.",
    author="QualityHammer",
    author_email="agingllama@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/QualityHammer/Whats-on-this-Album",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={
        "console_scripts": ["scrape_songs=scrape_songs.client:run"]
    }
)

