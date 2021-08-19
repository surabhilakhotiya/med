from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in med/__init__.py
from med import __version__ as version

setup(
	name="med",
	version=version,
	description="Med-Charge",
	author="Vp",
	author_email="vaibhav.parmar@syscort.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
