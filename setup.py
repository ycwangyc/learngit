from setuptools import setup, find_packages
 
setup(
  name = "punittest",
  version = "0.1.18",
  keywords = ("pip", "punittest"),
  description = "An extented unittest",
  long_description = "An extented unittest",
  license = "",
 
  url = "http://www.google.com",
  author = "ads",
  author_email = "asd.com",
 
  packages = find_packages(),
  include_package_data = True,
  platforms = "any",
  install_requires = [
    "openpyxl>=2.5.2",
  ]
)