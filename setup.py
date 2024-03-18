from setuptools import setup, find_namespace_packages

setup(
    name="tardis",
    version="6",
    description="TARDIS personal assistant",
    long_description='',
    url="",
    author="TimeLords",
    author_email="",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=[
        "prompt-toolkit",
        'colorama',
        'requests'
    ],
    entry_points={"console_scripts": ["tardis = bot.main:main"]},
    include_package_data=True,
    package_data={"": ["*.txt"]}
)
