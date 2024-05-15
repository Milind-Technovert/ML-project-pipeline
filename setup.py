from setuptools import find_packages, setup
from typing import List

hyphon_e_dot="-e ."

def get_requirements(filepath: str)-> List[str]:
    requirements=[]

    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]

        if hyphon_e_dot in requirements:
            requirements.remove(hyphon_e_dot)

# from distutils.core import setup

setup(name='ML Pipeline',
      version='0.0.1',
      description='ML project pipeline demo',
      author='Milind Mali',
      author_email='milind.mali@technovert.com',
    #   url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      install_requires=get_requirements("requirements.txt")
     )