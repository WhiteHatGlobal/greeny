from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in greeny/__init__.py
from greeny import __version__ as version

setup(
	name="greeny",
	version=version,
	description="Greeny Medows Custom app",
	author="White Hat Global",
	author_email="rk@whitehatglobal.org",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
