import os
from typing import Optional

from dotenv import load_dotenv

# Carrega as variáveis do .env uma única vez quando o módulo é importado
load_dotenv()

class Config:
    """Classe para gerenciar configurações e variáveis de ambiente"""
    
    # OpenAI
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    
    # SERP API
    SERP_API_KEY: Optional[str] = os.getenv("serp_api")
    
    # Firecrawl API
    FIRECRAWL_API_KEY: Optional[str] = os.getenv("fc_api")
    
    # ElevenLabs API
    ELEVENLABS_API_KEY: Optional[str] = os.getenv("eleven_api")
    
    @classmethod
    def validate_keys(cls) -> bool:
        """Valida se todas as chaves de API necessárias estão presentes"""
        missing_keys = []
        
        if not cls.OPENAI_API_KEY:
            missing_keys.append("OPENAI_API_KEY")
        if not cls.SERP_API_KEY:
            missing_keys.append("serp_api")
        if not cls.FIRECRAWL_API_KEY:
            missing_keys.append("fc_api")
        if not cls.ELEVENLABS_API_KEY:
            missing_keys.append("eleven_api")
        
        if missing_keys:
            raise ValueError(f"Chaves de API faltando no .env: {', '.join(missing_keys)}")
        
        return True
    
    @classmethod
    def get_openai_key(cls) -> str:
        if not cls.OPENAI_API_KEY:
            raise ValueError("OpenAI API key não encontrada no arquivo .env")
        return cls.OPENAI_API_KEY
    
    @classmethod
    def get_serp_key(cls) -> str:
        if not cls.SERP_API_KEY:
            raise ValueError("SERP API key não encontrada no arquivo .env")
        return cls.SERP_API_KEY
    
    @classmethod
    def get_firecrawl_key(cls) -> str:
        if not cls.FIRECRAWL_API_KEY:
            raise ValueError("Firecrawl API key não encontrada no arquivo .env")
        return cls.FIRECRAWL_API_KEY
    
    @classmethod
    def get_elevenlabs_key(cls) -> str:
        if not cls.ELEVENLABS_API_KEY:
            raise ValueError("ElevenLabs API key não encontrada no arquivo .env")
        return cls.ELEVENLABS_API_KEY
