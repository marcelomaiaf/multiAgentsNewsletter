import asyncio

from prompts.prompts import coletor_prompt
from utils.utils import NewsletterProcessor, VoiceConfig


async def main():
    processor = NewsletterProcessor()
    resultado = await processor.run(coletor_prompt)
    return resultado

if __name__ == "__main__":
    asyncio.run(main())
    