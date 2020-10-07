import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="orders",
    version="0.0.1",
    author="Pavel Kotliarov",
    author_email="pk.raven@gmail.com",
    description="Prints statistics and save result csv file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pkraven/orders",
    license="MIT",
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires='>=3.6',
    install_requires=['pandas==1.1.3'],
    scripts=['bin/test_orders']
)
