#🛡️ Analizador de Tráfico de Red

🔍 Visualiza en tiempo real los paquetes de red capturados con Python y una interfaz web moderna.

---

#📌 Descripción

El Analizador de Tráfico de Red es una herramienta que captura paquetes de red utilizando Python y Scapy, mostrando la información en una interfaz web interactiva desarrollada con HTML, Tailwind CSS y JavaScript.

---

#Características principales:

- ✅ Captura de paquetes en tiempo real (IP, protocolo, puertos, direcciones MAC)
  
- ✅ Interfaz intuitiva y moderna con Tailwind CSS

- ✅ Exportación de datos en formato JSON

- ✅ Compatible con Windows sin necesidad de Linux

- 📢 Si la herramienta detecta paquetes sospechosos, puedes analizar los datos para mejorar la seguridad de tu red.

---

#🚀 Requisitos

#Asegúrate de cumplir con los siguientes requisitos antes de ejecutar el script:

- 🔹 Tener Python 3 instalado en tu sistema.

- 🔹 Instalar las dependencias necesarias ejecutando:

```bash
pip install scapy
```
#🔧 Instalación y Uso

- 1️⃣ Clona este repositorio:
```bash
git clone https://github.com/Joel190321/NetworkTrafficAnalyzer.git
```
```bash
cd NetworkTrafficAnalyzer
```

- 2️⃣ Ejecuta el analizador:
```bash
python app.py
```

- 3️⃣ Abre el archivo index.html en un navegador para visualizar los datos capturados en tiempo real.

- 📌 El programa analizará los paquetes de red y mostrará la información en la interfaz web.

#🏗️ Estructura del Código

##El código está dividido en dos partes principales:

- analyzer.py (Captura de paquetes)

- 🛠️ Captura tráfico de red con Scapy

- 🛠️ Guarda los datos en un archivo JSON

- Interfaz Web (index.html + script.js)

- 🎨 Muestra los paquetes capturados en una tabla dinámica

- ⚡ Interactividad mejorada con JavaScript y Tailwind CSS
