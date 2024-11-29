from pydub import AudioSegment
import os

def convert_audio_to_wav(audio_path):
    """
    Converte um arquivo de áudio para o formato .wav.
    """
    # Verifica se o arquivo já está no formato .wav
    if audio_path.endswith('.wav'):
        return audio_path

    audio = AudioSegment.from_file(audio_path)
    wav_path = os.path.splitext(audio_path)[0] + '.wav'
    audio.export(wav_path, format='wav')

    return wav_path
