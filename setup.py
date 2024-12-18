from setuptools import setup, find_packages

setup(
    name="Quizzify",                      
    version="1.0.1",                      
    packages=find_packages(),             
    include_package_data=True,            
    install_requires=[                    
        "flask"
    ],
    description="General Knowledge Quiz App",      
    author="Ameer Hamzah Daiyan",                   
    author_email="ameerhamzah.daiyan@gmail.com",
    url="https://github.com/ameerhamzahd/Edge_Quizzify.git",    
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Flask",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',              
)
