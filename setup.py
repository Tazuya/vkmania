import setuptools
from vkmania.const import __version__

try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except UnicodeDecodeError:
    with open("README.md", "r") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ""

setuptools.setup(
    name="vkmania",
    version=__version__,
    author="Tazuya Shiba",
    author_email="deterrisadstellae@mail.ru",
    description="Simple VK API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tazuya/vkmania",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)