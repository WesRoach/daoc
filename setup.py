import setuptools

setuptools.setup(
    name="daoc",
    version="0.0.1",
    author="Wes Roach",
    author_email="wesr000@gmail.com",
    description="CLI Utility for DAoC",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        daoc=daoc:cli
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
