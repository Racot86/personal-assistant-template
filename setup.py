from setuptools import setup, find_packages

setup(name='tardis',
      version='1.0',
      description='AI TARDIS Assistant',
      url='https://github.com/Racot86/project-TimeLords12',
      author='Team Project',
      license='MIT',
      packages=find_packages(),
      entry_points={'console_scripts': ['tardis = .main:main']},
      install_requires=['colorama', 'prompt_toolkit', 'requests'],
)
