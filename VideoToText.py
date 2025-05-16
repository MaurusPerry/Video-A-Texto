from moviepy.editor import VideoFileClip

def extraer_audio(video_path, audio_path):
    # Cargar el archivo de video
    video = VideoFileClip(video_path)
    
    # Extraer el audio del video
    audio = video.audio
    
    # Guardar el audio en el archivo especificado
    audio.write_audiofile(audio_path)

# Ejemplo de uso
video_path = 'tu_video.mp4'  # Ruta del archivo de video
audio_path = 'audio_extraido.mp3'  # Ruta donde se guardará el audio extraído
extraer_audio(video_path, audio_path)

print(f"Audio extraído correctamente y guardado en {audio_path}")
