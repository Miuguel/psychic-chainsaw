import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import musicbrainzngs

# Configurando a API do MusicBrainz
musicbrainzngs.set_useragent("Michael_Clay", "1.0", "chrono_barros@hotmail.com")

def buscar_informacoes(musica):
    resultado = musicbrainzngs.search_recordings(musica, limit=1)
    if resultado['recording-list']:
        return resultado['recording-list'][0]
    return None

def atualizar_tags(arquivo, info):
    audio = EasyID3(arquivo)
    audio['title'] = info['title']
    audio['artist'] = ', '.join([artist['name'] for artist in info['artist-credit']])
    audio.save()

def processar_pasta(pasta):
    for filename in os.listdir(pasta):
        if filename.endswith(".ogg"):
            file_path = os.path.join(pasta, filename)
            nome_musica = filename.replace(".ogg", "")
            informacoes = buscar_informacoes(nome_musica)

            if informacoes:
                atualizar_tags(file_path, informacoes)
                print(f"Tags de '{filename}' atualizadas com sucesso!")
            else:
                print(f"Informações para '{filename}' não encontradas.")

def extract_info(folder_path, output_file):
    with open(output_file, 'w') as file:
        for filename in os.listdir(folder_path):
            if filename.endswith(".mp3"):
                file_path = os.path.join(folder_path, filename)
                audio = MP3(file_path, ID3=EasyID3)

                title = audio.get('title', ['Unknown'])[0]
                artist = audio.get('artist', ['Unknown'])[0]
                album = audio.get('album', ['Unknown'])[0]
                year = audio.get('date', ['Unknown'])[0]

                file.write(f"File: {filename}\n")
                file.write(f"Title: {title}\n")
                file.write(f"Artist: {artist}\n")
                file.write(f"Album: {album}\n")
                file.write(f"Year: {year}\n")
                file.write("\n")

# Exemplo de uso
pasta_musicas = r'C:/Users/chron/Music/Spotfy'
processar_pasta(pasta_musicas)
output_file = 'informacoes_musicas.txt'
extract_info(pasta_musicas, output_file)
