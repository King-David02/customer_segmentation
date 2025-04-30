from setuptools import setup, find_packages

ignore = '-e .'
def get_requirements(file):
    try:
        with open(file) as file:
            requirements = [req.strip() for req in file.readlines()]
            if ignore in requirements:
                requirements.remove(ignore)
        return requirements
    
    except FileNotFoundError:
        print("Requirements.txt not found")
        return []
    

setup(
    name='Customer Segmentation',
    version='0.01',
    description='Customer Segmentation Project',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)