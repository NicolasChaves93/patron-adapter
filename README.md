
# FastAPI XML to JSON - Patron Adapter
## 📌 Descripción
Este proyecto implementa un servicio web utilizando FastAPI y el patrón Adapter para convertir respuestas en XML a JSON.



## 🚀 Características

- Utiliza FastAPI para exponer un endpoint REST.
- Implementa el patrón Adapter para convertir XML a JSON.
- Usa uvicorn para ejecutar el servidor.
- Organización modular con rutas y adaptadores separados.


## 📂 Estructura del Proyecto

```
📁 patron-adapter/
│── 📁 app/
│   ├── __init__.py
│   ├── 📁 adapters/
│   │   ├── __init__.py
│   │   ├── 📄xml_to_json_adapter.py
│   ├── 📁 routes/
│   │   ├── __init__.py
│   │   ├── 📄convert.py
│   ├── 📄main.py
│── 📄requirements.txt
│── 📄README.md 
```
## ⚙️ Requerimientos

Para ejecutar este proyecto, asegúrate de contar con los siguientes requisitos:
- **Python 3.8+**
- XML Parsing con xml.etree.ElementTree
- Librerías necesarias (instalar con `pip install -r requirements.txt`):
  - FastAPI
  - Uvicorn

## 🚀 Instalación y Ejecución
1️⃣ Clonar el Repositorio
```
git clone [patron-adapter](https://github.com/NicolasChaves93/patron-adapter.git)
cd patron-adapter
```
2️⃣ Crear y Activar un Entorno Virtual
```
python -m venv venv
venv\Scripts\activate
```
3️⃣ Instalar Dependencias
```
pip install -r requirements.txt
```
4️⃣ Ejecutar la Aplicación
```
uvicorn main:app --reload
```
## 📡 Uso del Endpoint
Convertir XML a JSON
- URL: http://127.0.0.1:8000/convert
- Método: GET
- Respuesta esperada (JSON):

```
{
  "response": {
    "user": {
      "id": "123",
      "name": "Nicolas Chaves",
      "email": "nicolas@example.com"
    }
  }
}
```


## 📖 Licencia

Este proyecto está bajo la licencia [MIT](https://choosealicense.com/licenses/mit/). ¡Siéntete libre de usarlo y modificarlo!