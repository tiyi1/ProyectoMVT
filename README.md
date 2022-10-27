# ProyectoMVT

This project aims to create a system for patients, suppliers and employees administration for a medical center. 
Among the different funcionalities that it has, we can find:
- Create a new patient, supplier or employee within the database using the following urls:
    localhost:8000/empleados/cargar         -> to set up a new employee
    localhost:8000/pacientes/cargar         -> to set up a new patient
    localhost:8000/proveedores/cargar       -> to set up a new supplier
- Search for a specific employee through the following url:
    localhost:8000/empleados/buscar_empleado
- Get the full list of employees, suppliers or patients using the following urls:
    localhost:8000/empleados        -> to get the employees' list
    localhost:8000/pacientes        -> to get the patients' list
    localhost:8000/proveedores      -> to get the suppliers' list

INSTALL
For installing this software you need to:

1. CHECK PYTHON VERSION
This project was written with python 3.10.6. 
Test this project with this version or higher to avoid any compatibility issues.
To check python version,

- in *nix systems:
> python --version
> Python 3.8.0

- in windows:
c:\> py --version
c:\> Python 3.8.0

2. INSTALL DEPENDENCIES
You need to run pip install (or pip3), make sure you are in the project folder and you can see the requirements.txt file when you do a ls or dir:

> pip install -r requirements.txt
This last will return a bunch of stuff in the terminal.

Some operative systems will required you to use pip3 instead of pip

3. SETTING UP DJANGO APPLICATIONS
Once you finish the dependencies installation you need to run some django commands.

a. MIGRATIONS
Initialize the database *nix:

> python mananage.py migrate
windows:

c:\> py mananage.py migrate

b. RUN THE TEST SERVER
> python mananage.py runserver
windows:

c:\> py mananage.py runserver

Finally, go to localhost:8000/ to access to the app.

If everthing goes well you should be able to open the browser and see the application running.