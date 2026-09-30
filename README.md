# 🎵 Music Downloader CLI (Dockerized)

Herramienta de línea de comandos (CLI) interactiva desarrollada en **Python** para descargar y convertir audio a formato **MP3 (192 kbps)** utilizando `yt-dlp`. 

Todo el entorno se encuentra completamente empaquetado en una imagen de **Docker**, integrando las dependencias nativas del sistema operativo (`ffmpeg` para el procesamiento multimedia y `deno` como runtime de JavaScript para solventar los retos de firma/desafíos dinámicos de YouTube).

---

## 🌟 Características

- **Entorno aislado y portable:** No requiere instalar Python, librerías, FFmpeg ni Deno en el sistema operativo local; Docker resuelve todas las dependencias.
- **Bypass dinámico con Deno:** Incorpora el motor Deno para interpretar scripts ofuscados de JavaScript de YouTube de forma nativa, evitando errores de autenticación o bloqueos 403.
- **Filtro individual:** Configurado para ignorar listas de reproducción completas (`noplaylist: True`), descargando exclusivamente la pista indicada.
- **Persistencia mediante volúmenes:** Los archivos generados se sincronizan directamente con una carpeta de tu máquina anfitriona mediante montajes de Docker (`bind mounts`).
- **Modo CLI interactivo:** Bucle continuo para descargar múltiples canciones en una sola sesión de terminal.

---

## 📂 Estructura del Proyecto

```text
music-downloader/
├── app.py                # Script principal con la lógica CLI y configuración de yt-dlp
├── Dockerfile            # Receta de construcción de la imagen Docker
├── requirements.txt      # Dependencias de Python (yt-dlp)
├── .gitignore            # Exclusiones para el control de versiones en Git
├── .dockerignore          # Archivos excluidos del contexto de compilación de Docker
├── README.md             # Documentación del proyecto
└── musica/               # Carpeta local montada donde se alojan los MP3 descargados
```

### Descripción de los archivos clave

- **`app.py`:** Contiene la interfaz de consola, la captura de URLs con manejo de excepciones y las opciones de codificación de `yt-dlp` (conversión a MP3, tasa de muestreo y directorio de salida `/downloads`).
- **`Dockerfile`:** Parte de una imagen ligera `python:3.11-slim`, instala `ffmpeg` y descarga el binario standalone de `deno`, copia el código e instala las dependencias de Python optimizando las capas de caché.
- **`requirements.txt`:** Especifica `yt-dlp` como el extractor multimedia base.
- **`.dockerignore` & `.gitignore`:** Previenen la inclusión accidental de archivos binarios descargados (`*.mp3`), cachés (`__pycache__`) y configuraciones locales tanto en la imagen como en GitHub.

---

## ⚙️ Requisitos Previos

Únicamente necesitas tener instalado **Docker Engine** en tu máquina:

- [Guía oficial de instalación de Docker](https://docs.docker.com/engine/install/)

*(Para usuarios de Linux, se recomienda agregar el usuario al grupo `docker` para ejecutar los comandos sin `sudo`)*.

---

## 🚀 Instalación y Despliegue

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/music-downloader.git
cd music-downloader
```

### 2. Construir la imagen de Docker

Ejecuta el siguiente comando para compilar la imagen local:

```bash
docker build -t music-downloader .
```

> **Nota:** Este paso descarga las capas base de Python, aprovisiona `ffmpeg` y `deno`, e instala las dependencias de Python. Solo necesitas ejecutarlo la primera vez o si modificas el código fuente.

---

## 🎧 Uso de la Aplicación CLI

Para iniciar el descargador, ejecuta el contenedor en modo interactivo mapeando una carpeta local para almacenar los audios:

```bash
docker run --rm -it -v "$(pwd)/musica:/downloads" music-downloader
```

### Desglose del comando:

| Parámetro | Función |
| :--- | :--- |
| `docker run` | Crea e inicia una instancia (contenedor) a partir de la imagen. |
| `--rm` | Destruye el contenedor automáticamente al finalizar la ejecución, manteniendo el disco limpio. |
| `-it` | Asigna una pseudo-terminal (`-t`) y mantiene abierta la entrada estándar (`-i`) para permitir la interacción por teclado. |
| `-v "$(pwd)/musica:/downloads"` | Conecta la carpeta local `musica` con el directorio `/downloads` interno del contenedor. |
| `music-downloader` | Nombre de la imagen compilada previamente. |

### Flujo de interacción:

1. El programa mostrará un banner de bienvenida y solicitará la URL:
   ```text
   === Descargador de audio a MP3 ===
   Escribe 'no' para salir del programa.

   Ingresa la URL del video: 
   ```
2. Pega el enlace de YouTube y presiona `Enter`. Se descargará y convertirá a MP3 automáticamente.
3. Puedes continuar introduciendo URLs sucesivas.
4. Para cerrar la aplicación, escribe `no` o presiona `Ctrl + C`.
5. Los archivos de audio estarán disponibles de inmediato en tu carpeta `./musica`.

---

## 🛠️ Tecnologías Utilizadas (Stack)

- **Lenguaje:** [Python 3.11](https://www.python.org/)
- **Extractor multimedia:** [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- **Codificación de audio:** [FFmpeg](https://ffmpeg.org/)
- **Motor JS:** [Deno](https://deno.land/)
- **Contenerización:** [Docker](https://www.docker.com/)