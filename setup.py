from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Mashup-Gurdarshan-102303217",
    version="1.0.0",
    author="Gurdarshan Singh",
    author_email="gurdarshansingh7814@gmail.com",
    description="A command-line tool to download, cut, and mashup YouTube audio.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "yt-dlp",
        "pydub"
    ],
    entry_points={
        "console_scripts": [
            "mashup=Mashup_Gurdarshan_102303217.mashup:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)