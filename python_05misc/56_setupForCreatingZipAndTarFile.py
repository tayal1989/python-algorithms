'''
To Distribute a module named “MyMath.py”
Contents of Setup.py

from distutils.core import setup
 
setup(name = 'AddNoFromString', version = '2.0', py_modules=['AddNoFromString'],)

python   setup.py   sdist  
[ will create archive named AddNoFromString.tar.gz  or .zip ]
'''

from distutils.core import setup
 
setup(name = 'AddNoFromString', version = '2.0', py_modules=['AddNoFromString'],)
