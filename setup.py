from setuptools import setup, find_packages

setup(
    name="llm-cost-tracker",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'llm-tracker=llm_cost_tracker.cli:main'
        ]
    },
)