import setuptools

import info


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


with open("README.md", "r") as fh:
    long_description = fh.read()


install_reqs = parse_requirements('./requirements')
print(install_reqs)

setuptools.setup(
    name=info.name,
    version=info.version,
    author=info.author,
    author_email=info.email,
    description=info.description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/Hedgehogues/{info.name}',
    packages=setuptools.find_packages(exclude=['tests', 'service']),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=install_reqs,
    package_data={'': ['{{ cookiecutter.python_package }}/__cmd/*', '{{ cookiecutter.python_package }}/__service/*']},
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.python_package }}_cli={{ cookiecutter.python_package }}.__cmd.cli:main',
            '{{ cookiecutter.python_package }}_http={{ cookiecutter.python_package }}.__cmd.http_:main',
        ],
    },
)
