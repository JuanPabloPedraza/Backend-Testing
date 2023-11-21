# Automation-Pagos360
Framework automation with Python-Pytest-allure

## Getting Started

Las siguientes instrucciones premiten obtener una copia del proyecto, setear el entorno 
y poder correrlo localmente para desarollo de nuevas funcionalidades o testing.


### Prerequisitos

> #### Python 
>
> - Ingresar a la sección Descargas de [Python](https://www.python.org/downloads/).
> - Descargar la última versión o >= to 3.9.0.
> - Instalar Python y setear las variables de entorno.
> - Verificar que se haya instalado correctamenete con *python --version* desde cualquier consola/terminal 
> - (PowerShell, CMD, bash).
> ```
> PS C:\Users\you_user> python --version
> Python 3.9.0
> ```

> #### Entorno virtual de Python
>
> Los entornos virtuales de Python son útiles para evitar conflictos entre distintos proyectos que 
> pueden utilizar distintas versiones de librerías.
> - Ubicado desde una consola en la raíz del proyecto, ejecutar el siguiente comando:
> ```
> python -m venv .venv
> ```
> - Al finalizar, se debería haber creado una carpeta con nombre ".venv" la raíz del proyecto.
> - Para acitvar el entorno virtual, ejecutar el siguiente comando:
> -- En Linux bash/zsh -> ``` $ source .venv/bin/activate ```
> -- En Windows cmd.exe -> ``` .\.venv\Scripts\activate.bat ```
> -- En Windows PowerShell -> ``` .\.venv\Scripts\Activate.ps1 ```
> - Para indagar más sobre el tema, ingresar a la siguiente url [venv](https://docs.python.org/3/library/venv.html).

> #### Java
>
> Es necesario instalar Java para poder generar y levantar el reporte de Allure.
> - Descargar la versión correspondietnte al SO [Oracle](https://www.oracle.com/ar/java/technologies/downloads/).
> - Instalar Java.
>- Agregar al Path

> #### Allure 
>
> Se necesita instalar Allure en el sistema.
> - Ingresar a [allure release](https://github.com/allure-framework/allure2/releases/).
> - Descargar la versión zip: **2.20.1**.
> - Descomprimir en el directorio que prefieras. Por ejemplo, crear una carpeta de nombre *allure* en *C:\\* y descomprimir aquí.
> ```
> C:\allure
> ```
> - Agregar la carpeta *bin* de allure a las Variables de Entorno *PATH*.
> - > - Verificar la instalación de Allure ejecutando el comando *allure --version* desde cualquier consola/terminal.
> ```bash
> PS C:\Users\you_user> allure --version
> 2.20.1

### Instalación

>
> #### Python Libs
> - Es neceasrio instalar en el proyecto los módulos/librerías que se usan como 
> - dependencias desde el archivo *requirements.txt*.
> ```
> PS C:\Users\you_user\you_workspace\you_proyect> pip install -r requirements.txt
> ```
> - Finalizada la instalación, se puede verificar la instalación de los módulos con el comando *pip freeze* 
> - y se debe observar lo siguente:
> ```console
> PS C:\Users\you_user\you_workspace\you_proyect> pip freeze
> ...
> allure-pytest==2.13.2
> allure-python-commons==2.13.2
> attrs==23.1.0
> certifi==2023.11.17
> charset-normalizer==3.3.2
> colorama==0.4.6
> exceptiongroup==1.2.0
> idna==3.4
> iniconfig==2.0.0
> packaging==23.2
> pluggy==1.3.0
> pytest==7.4.3
> requests==2.31.0
> tomli==2.0.1
> urllib3==2.1.0
> python-dotenv==1.0.0
> ...
>```

## Ejecución de tests
> El framework está basado en *pytest*, por lo que las distintas formas de ejecutar los test se pueden revisar en la documenetación: [pytest](https://docs.pytest.org/en/6.2.x/usage.html#calling-pytest-through-python-m-pytest).
> Por ejemplo, para ejecutar el set completo de test se debe correr el siguiente comando:
> ```
> PS C:\Users\you_user\you_workspace\you_proyect\tests> pytest  -v -s --alluredir=./allure-results

> ```
> Por ejemplo, para ejecutar un test específico se debe correr el siguiente comando:
> 
> PS C:\Users\you_user\you_workspace\you_proyect\tests> pytest test_payment.py -v -s --alluredir=./allure-results 
> PS C:\Users\you_user\you_workspace\you_proyect\tests> pytest test_description.py -v -s --alluredir=./allure-results
> ```

### Reporte Allure
> Para acceder al reporte allure se debe utilizar el siguiente comando:
> ```
> PS C:\Users\you_user\you_workspace\you_proyect\tests> allure serve ./allure-results 
> ```
>
> **Advertencia:** el directorio donde se busca el reporte con el comando anterior, debe coincidir con el 
> especificado en el comando con el que se ejecutó el script del test.
> 

## License

MIT

