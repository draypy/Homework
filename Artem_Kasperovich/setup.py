from setuptools import setup, find_packages
with open('requirements.txt') as req:
    all_req = req.read().split('\n')
install_require = [req.strip() for req in all_req]
with open("../README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="rss_reader",
    author="Artem_Kasperovich",
    author_email="kaspiarovich.artsemi@gmail.com",
    long_description=long_description,
    packages=find_packages(),
    python_requires='>=3.8, <4',
    install_requires=install_require,
    entry_points={
        'console_scripts': ['rss_reader=project.rss_reader:main'],
    }
)
