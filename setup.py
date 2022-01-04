import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="schengulator", 
    version="0.0.2",
    author="Penelope How",
    author_email="pennyruthhow@gmail.com",
    description="A tool to calculate how many days an individual has been in Schengen countries out of a specified 180-day period",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PennyHow/schengulator",
    keywords="schengen travel movement europe",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    install_requires=['datetime', 'csv'],
    python_requires='>=3',
)

