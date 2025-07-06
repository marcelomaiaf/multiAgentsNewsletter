"""Exemplos de uso da classe NewsletterProcessor"""
import asyncio
from utils.utils import NewsletterProcessor, VoiceConfig
from prompts.prompts import coletor_prompt


async def exemplo_basico():
    """Exemplo básico"""
    processor = NewsletterProcessor()
    resultado = await processor.run(coletor_prompt, "newsletter_basica.mp3")
    return resultado.success


async def exemplo_personalizado():
    """Exemplo com configurações personalizadas"""
    voice_config = VoiceConfig(voice_id="pNInz6obpgDQGcFmaJgB", speed=1.0)
    processor = NewsletterProcessor(voice_config=voice_config, output_dir="output/custom")
    
    # Pipeline em etapas
    roteiro = await processor.criar_roteiro(coletor_prompt)
    audio_data = await processor.gerar_audio(roteiro)
    sucesso = processor.salvar_audio(audio_data, "personalizado.mp3")
    
    return sucesso


async def main():
    """Executa os exemplos"""
    await exemplo_basico()
    await exemplo_personalizado()


if __name__ == "__main__":
    asyncio.run(main())
