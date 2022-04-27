import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="copipy",
    entry_points={
      'console_scripts': [
        'copipy = main.hello:hello_world',
      ]
    },
    version="0.0.1",
    author="Sudoer",
    author_email="sudoer.zero@gmail.com",
    description="Adding copyright to your project files is now easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sudoer-zero/copipy",
    project_urls={
        "Bug Tracker": "https://github.com/sudoer-zero/copipy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)