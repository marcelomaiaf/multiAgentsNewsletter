from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

from agents import Runner
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

from news_agents.coletor import coletor
from news_agents.redator import redator

from .config import Config


@dataclass
class VoiceConfig:
    """Configuração para geração de voz"""
    voice_id: str = "lWq4KDY8znfkV0DrK8Vb"
    output_format: str = "mp3_22050_32"
    model_id: str = "eleven_turbo_v2_5"
    stability: float = 0.45
    similarity_boost: float = 0.8
    style: float = 1.0
    use_speaker_boost: bool = True
    speed: float = 1.17


@dataclass
class NewsletterResult:
    """Resultado do processamento da newsletter"""
    success: bool
    content: Optional[str] = None
    audio_path: Optional[str] = None
    error_message: Optional[str] = None


class NewsletterProcessor:
    """Processador para criação de newsletters com áudio"""
    
    def __init__(self, voice_config: Optional[VoiceConfig] = None, output_dir: str = "output", max_turns: int = 20):
        self.voice_config = voice_config or VoiceConfig()
        self.output_dir = Path(output_dir)
        self.max_turns = max_turns
        self._elevenlabs_client: Optional[ElevenLabs] = None
        Config.validate_keys()
    
    @property
    def elevenlabs_client(self) -> ElevenLabs:
        if self._elevenlabs_client is None:
            self._elevenlabs_client = ElevenLabs(api_key=Config.get_elevenlabs_key())
        return self._elevenlabs_client
    
    async def criar_roteiro(self, prompt_coletor: str) -> str:
        """Cria o roteiro da newsletter coletando notícias e redigindo conteúdo"""
        noticias_run_result = await Runner.run(coletor, prompt_coletor, max_turns=self.max_turns)
        print(noticias_run_result)
        roteiro_result = await Runner.run(redator, noticias_run_result.final_output, max_turns=self.max_turns)
        
        return roteiro_result.final_output
    
    async def gerar_audio(self, text: str) -> bytes:
        """Gera áudio a partir do texto usando ElevenLabs"""
        voice_settings = VoiceSettings(
            stability=self.voice_config.stability,
            similarity_boost=self.voice_config.similarity_boost,
            style=self.voice_config.style,
            use_speaker_boost=self.voice_config.use_speaker_boost,
            speed=self.voice_config.speed,
        )
        
        return self.elevenlabs_client.text_to_speech.convert(
            voice_id=self.voice_config.voice_id,
            output_format=self.voice_config.output_format,
            text=text,
            model_id=self.voice_config.model_id,
            voice_settings=voice_settings,
        )
    
    def salvar_audio(self, audio_data: bytes, filename: str = "newsletter_audio.mp3") -> bool:
        """Salva os dados de áudio em um arquivo"""
        try:
            output_path = self.output_dir / filename
            self.output_dir.mkdir(parents=True, exist_ok=True)
            
            with open(output_path, "wb") as f:
                if hasattr(audio_data, '__iter__') and not isinstance(audio_data, (str, bytes)):
                    for chunk in audio_data:
                        if chunk:
                            f.write(chunk)
                else:
                    f.write(audio_data)
            return True
        except Exception:
            return False
    
    async def run(self, prompt_coletor: str) -> NewsletterResult:
        """Executa todo o pipeline de criação da newsletter"""
        result = NewsletterResult(success=False)
        
        try:
            # 1. Criar roteiro
            roteiro = await self.criar_roteiro(prompt_coletor)
            result.content = roteiro
            
            # 2. Gerar áudio
            audio_data = await self.gerar_audio(roteiro)
            
            
            filename = f"newsletter_{datetime.now().strftime('%Y%m%d')}.mp3"
            audio_saved = self.salvar_audio(audio_data, filename)
            
            if audio_saved:
                result.audio_path = str(self.output_dir / filename)
                result.success = True
            else:
                result.error_message = "Erro ao salvar áudio"
            
        except Exception as e:
            result.error_message = f"Erro no processamento: {e}"
        
        return result

    