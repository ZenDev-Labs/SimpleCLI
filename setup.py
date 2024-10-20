from setuptools import setup, find_packages
setup(
    name='simplecli',
    version='0.1.0',
    packages=find_packages(),  # Automatically find packages
    entry_points={
        'console_scripts': [
            'simplecli = simplecli_pkg.__main__:main'  # Entry point for the CLI
        ]
    }
)