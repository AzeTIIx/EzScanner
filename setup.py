from setuptools import setup, find_packages


setup(
    name='EzScanner',
    version="1.2",
    packages=find_packages(),
    author="CharlesAIMIN",
    author_email="caimin.ing2024@esaip.org",
    install_requires=["pystyle","tqdm"],
    description="EzScanner allow you to perform an NMAP scan on a network",
    include_package_data=True,
    url='http://github.com/CharlesAIMIN/PyPentest',
    entry_points = {'console_scripts': ['EzScanner = src.core:main']},
    classifiers=[
        "Programming Language :: Python",
    ],
)
