from setuptools import setup, find_packages


setup(
    name='PyPentest',
    version="1",
    packages=find_packages(),
    author="CharlesAIMIN",
    author_email="caimin.ing2024@esaip.org",
    install_requires=["pystyle","python-nmap","tqdm"],
    description="PyPentest allow you to perform an NMAP scan on a network",
    include_package_data=True,
    url='http://github.com/CharlesAIMIN/PyPentest',
    entry_points = {'console_scripts': ['PyPentest = src.core:main']},
    classifiers=[
        "Programming Language :: Python",
    ],
)
