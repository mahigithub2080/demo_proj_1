from setuptools import find_packages,setup
HYPHON_E_DOT="-e ."
def get_requirements(file_path):
    """
    this function will return the list of elements

    """
    requirements=[] #empty list
    with open(file_path)as file_obj: # oepning the file as file_obj object
        requirements=file_obj.readlines() # it will read every element of file which we have written in 'requirements.txt' file
        requirements=[req.replace("\n","")for req in requirements] 
        # one problme is there, when it will try to read the next line parameter there will be  "\n" parameter will also get 
        # added in our list... so to avoid this... we have to replace "\n" with blank/none..

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)

    return requirements


setup(
    name="mlproject",
    version='0.0.1',
    author='mahi_patil',
    author_email='mahipatil1593@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt') 
    # it will call get_requirements() method which we have defined above by passing the 'requirements.txt' 
)