#
# Setup file for
# tpqoa -- Algorithmic Trading with Oanda
#
# (c) Dr. Yves J. Hilpisch
# The Python Quants GmbH
#
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="tpqoa",
    version="0.0.57",
    description="tpqoa Algorithmic Trading with Oanda updated to 3.13",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yves Hilpisch",
    author_email="team@tpq.io",
    url="http://home.tpq.io",
    packages=["tpqoa"],
    install_requires=[
        "v20 @ git+https://github.com/itsklimov/v20-python-3.13.git@5d2522c6d32b2dad1455d1ba3cafba39f4c1d23d",
        "pyyaml",
    ],
)
