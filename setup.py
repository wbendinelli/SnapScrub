from setuptools import setup, find_packages

setup(
    name="snapscrub",
    version="1.0.0",
    author="William Bendinelli",
    author_email="wbendinelli@gmail.com",
    description="SnapScrub - An advanced image processing and classification pipeline.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/SnapScrub",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "pandas",
        "opencv-python",
        "Pillow",
        "scikit-image",
        "tensorflow",
        "torch",
        "torchvision",
        "torchaudio",
        "imagehash",
        "ftfy",
        "regex",
        "tqdm",
        "pillow-heif"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Intended Audience :: Developers",
    ],
    entry_points={
        "console_scripts": [
            "snapscrub=src.main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="image processing, deep learning, computer vision, classification",
    project_urls={
        "Documentation": "https://github.com/yourusername/SnapScrub",
        "Source": "https://github.com/yourusername/SnapScrub",
        "Tracker": "https://github.com/yourusername/SnapScrub/issues",
    },
)