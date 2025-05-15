import os
import uuid
import gradio as gr
from openai import OpenAI
from moviepy import VideoFileClip
import dotenv

# Carrega variáveis de ambiente
dotenv.load_dotenv()

def converter_para_wav(caminho_arquivo_mp4):
    """
    Converte arquivo de vídeo para WAV usando MoviePy
    """
    os.makedirs('uploads', exist_ok=True)
    nome_wav = os.path.join('uploads', f"{uuid.uuid4()}.wav")
    
    try:
        video = VideoFileClip(caminho_arquivo_mp4)
        video.audio.write_audiofile(nome_wav, fps=16000)
        video.close()
        return nome_wav
    
    except Exception as e:
        print(f"Erro na conversão: {e}")
        return None

def transcrever_audio(caminho_arquivo_wav, idioma='pt'):
    """
    Transcreve áudio usando API da OpenAI
    """
    try:
        # Verifica se a chave API está configurada
        if not os.getenv("openaiKey"):
            return "Chave da API OpenAI não configurada. Verifique o arquivo .env"
        
        # Verifica existência do arquivo
        if not os.path.exists(caminho_arquivo_wav):
            return f"Arquivo WAV não encontrado: {caminho_arquivo_wav}"
        
        # Inicializa cliente OpenAI
        client = OpenAI(api_key=os.getenv("openaiKey"))
        
        # Abre o arquivo para upload
        with open(caminho_arquivo_wav, "rb") as arquivo_audio:
            # Realiza a transcrição
            resultado = client.audio.transcriptions.create(
                model="whisper-1",
                file=arquivo_audio,
                language=idioma
            )
        
        return resultado.text
    
    except Exception as e:
        return f"Erro na transcrição: {str(e)}"
    finally:
        # Remove arquivo WAV temporário
        if 'caminho_arquivo_wav' in locals() and os.path.exists(caminho_arquivo_wav):
            os.unlink(caminho_arquivo_wav)

def processar_video(arquivo, idioma='pt'):
    """
    Processa o vídeo: converte para WAV e transcreve
    """
    if not arquivo or not os.path.exists(arquivo):
        return "Arquivo não encontrado ou não selecionado"
    
    try:
        arquivo_wav = converter_para_wav(arquivo)
        
        if arquivo_wav:
            transcricao = transcrever_audio(arquivo_wav, idioma)
            return transcricao
        else:
            return "Falha na conversão de áudio. Verifique o arquivo."
    
    except Exception as e:
        return f"Erro no processamento: {e}"

# Interface Gradio
with gr.Blocks() as demo:
    gr.Markdown("# Transcrição de Vídeo com Whisper OpenAI")
    gr.Markdown("Faça upload de um arquivo de vídeo para transcrição")
    
    with gr.Row():
        input_video = gr.File(label="Faça upload do seu vídeo")
        output_texto = gr.Textbox(
            label="Transcrição", 
            lines=10
        )
    
    with gr.Row():
        idioma_select = gr.Dropdown(
            label="Idioma", 
            choices=['pt', 'en', 'es', 'fr', 'de'], 
            value='pt'
        )
    
    btn_processar = gr.Button("Transcrever Vídeo")
    
    btn_processar.click(
        fn=processar_video, 
        inputs=[input_video, idioma_select], 
        outputs=output_texto
    )

# Lança a interface
if __name__ == "__main__":
    demo.launch()