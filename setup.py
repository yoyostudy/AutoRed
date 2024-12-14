from setuptools import setup, find_packages

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

setup(
    name="autored",
    version="0.0.1",
    description="Automated attack generation framework for red teaming of LLMs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  
    author="Zhe Wang",
    author_email="wangzheyoyo@gmail.com", 
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requirements,
    url="https://github.com/yoyostudy/AutoRed",
    license="Apache 2.0", 
)
