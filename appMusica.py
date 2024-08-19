import yt_dlp
import os

def download_video_as_mp3(youtube_url, output_path):
    try:
        # Configurações para o yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            video_title = info_dict.get('title', None)
            if video_title:
                original_file = os.path.join(output_path, f"{video_title}.webm")
                new_file = os.path.join(output_path, f"{video_title}.mp3")
                if os.path.exists(original_file):
                    os.rename(original_file, new_file)
                    print(f"Download e conversão concluídos! Arquivo salvo em: {new_file}")
                else:
                    print(f"Arquivo original não encontrado: {original_file}")
            else:
                print("Não foi possível obter o título do vídeo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    while True:
        youtube_url = input("Digite a URL do vídeo do YouTube: ")
        output_path = "/home/phss/Músicas"
        download_video_as_mp3(youtube_url, output_path)

        continuar = input("Você quer baixar outro vídeo? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
