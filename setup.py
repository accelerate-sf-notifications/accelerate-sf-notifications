from setuptools import find_packages, setup

setup(
    name="asn",
    version="0.0.1",
    description="AI notification for gov",
    author="asn team",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        # 'numpy',
    ],
    python_requires=">=3.5",
)
