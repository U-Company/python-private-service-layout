import setuptools

import info


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


with open("README.md", "r") as fh:
    long_description = fh.read()

private_reqs = parse_requirements('./requirements/private/package')
public_reqs = parse_requirements('./requirements/public/package')
install_reqs = private_reqs + public_reqs
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
)
