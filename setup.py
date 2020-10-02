from setuptools import setup
import io


def readme():
    with io.open("README.md", encoding="utf8", errors="ignore") as f:
        with io.open("Changelog.md", encoding="utf8", errors="ignore") as c:
            return f.read() + c.read()


setup(name="opener",
      version="0.0.4",
      description="Solve open the lock puzzle.",
      long_description=readme(),
      long_description_content_type="text/markdown",
      install_requires=[],
      classifiers=[
          "Operating System :: OS Independent",
          "License :: OSI Approved :: MIT License",
          "Environment :: Console",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          "Development Status :: 5 - Production/Stable",
          "Topic :: Games/Entertainment :: Puzzle Games",
          "Topic :: Scientific/Engineering :: Mathematics"
      ],
      keywords="opener puzzle open_the_lock solver",
      url="http://github.com/arsho/opener",
      author="Ahmedur Rahman Shovon",
      author_email="shovon.sylhet@gmail.com",
      license="MIT",
      packages=["opener"],
      include_package_data=True,
      zip_safe=False
      )
