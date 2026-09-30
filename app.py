# Manejar carpetas y rutas
import os
# Para descargar musica
import yt_dlp

# Metodo de descarga
def download_audio(url, output_dir="/downloads"):
    # Si la carpeta de salida no existe, crearla
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'noplaylist': True,
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }

    print(f'[*] Iniciando descarga desde: {url}')

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f'[+] Descarga completada.\n')
    except Exception as e:
        print(f'[!] Error durante la descarga: {e}\n')


def main():

    print('=== Descargador de audio a MP3 ===')
    print("Escribe 'no' para salir del programa.\n")

    while True:
        url = input("Ingrese la URL del video: ").strip()

        if url.lower() == 'no':
            print('Saliendo del programa. ¡Hasta luego!')
            break

        if not url:
            print('[!] URL vacía. Por favor, ingrese una URL válida.\n')
            continue

        download_audio(url)


if __name__ == "__main__":
    main()