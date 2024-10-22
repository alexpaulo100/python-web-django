from setuptools import setup

setup(
    name="django-blog",
    version="0.1.0",
    packages=["djblog", "blog"],
    install_requires=["django", "django-markdownify"],
)
