from setuptools import setup, find_packages

setup(
    name="Munchkin",
    version="0.2.0",
    description="This is my discount version of the game Munchkin",
    author="Jacob Thornton",
    author_email="jacobreidth@hotmail.com",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        # List your project dependencies here
        "pytest==7.3.1",
        "python==3.8.2"
    ],
    classifiers=[
        "Development Status :: 2 - Beta",
        "Intended Audience :: Friends and Family",
        "License :: None?",
        "Programming Language :: Python :: 3.8.2",
    ],
)
