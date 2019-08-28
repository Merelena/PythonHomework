from setuptools import setup

setup(name='pycalc',
      version='1.0',
      description='Calculates mathematical expressions',
      url='https://github.com/Merelena/PythonHomework',
      author='Elena Fyodorova',
      author_email='fedorova.elena.dz@gmail.com',
      packages=['pycalc'],
      entry_points={
          'console_scripts': [
                'pycalc=pycalc.pycalc:main'
          ]
      }
)
