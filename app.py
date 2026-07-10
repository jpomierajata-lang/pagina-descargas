from flask import Flask, request, send_file, render_template
import yt_dlp
import os

app = Flask(__name__)

# 🔹 Función para obtener título y miniatura
def obtener_info_video(url):
    opciones = {'skip_download': True}
    with yt_dlp.YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(url, download=False)
        titulo = info.get("title", "Sin título")
        miniatura = info.get("thumbnail", "")
    return titulo, miniatura

# 🔹 Descargar video
def descargar_video(url, carpeta="Mis_videos"):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    opciones = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': f'{carpeta}/%(title).50s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(url, download=True)
        nombre_archivo = ydl.prepare_filename(info)
    return nombre_archivo

# 🔹 Descargar audio
def descargar_audio(url, carpeta="Mis_audios"):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': f'{carpeta}/%(title).50s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(url, download=True)
        nombre_archivo = ydl.prepare_filename(info)
    return nombre_archivo

# 🔹 Ruta principal
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("url")
        tipo = request.form.get("tipo")

        # Mostrar preview
        if tipo == "preview":
            titulo, miniatura = obtener_info_video(url)
            return render_template("index.html", preview=True, titulo=titulo, miniatura=miniatura, url=url)

        # Descargar video o audio
        if tipo == "video":
            archivo = descargar_video(url)
        else:
            archivo = descargar_audio(url)

        return send_file(archivo, as_attachment=True)

    return render_template("index.html", preview=False)

if __name__ == "__main__":
    app.run(debug=True)
