# Multi-Agent Newsletter Generator 🤖📰

An intelligent multi-agent system that automatically generates newsletters with curated news, engaging content, and natural voice narration.

## How it works

The project uses a sophisticated multi-agent architecture where each agent has a specialized role in the content creation pipeline:

**Collector Agent**: Searches for relevant news using SerpAPI, filtering content based on configurable topics and date ranges.

**Extractor Agent**: Accesses collected links and uses Firecrawl to extract full article content, creating structured summaries from web pages.

**Writer Agent**: Transforms raw content into engaging, fluid scripts optimized for audio consumption and human-like narration.

**Voice Generator**: Converts the final script into natural-sounding audio using ElevenLabs' advanced text-to-speech technology.

The result is a professionally crafted audio newsletter, ready for distribution via various channels.

## Project Structure

```
multiAgentsNewsletter/
├── README.md                    # Project documentation
├── pyproject.toml              # Project configuration and dependencies
├── uv.lock                     # Dependency lock file
└── src/                        # Source code directory
    ├── main.py                 # Main execution script
    ├── example_usage.py        # Usage examples and tutorials
    ├── requirements.txt        # Python dependencies list
    │
    ├── news_agents/            # Multi-agent system components
    │   ├── coletor.py         # News collector agent
    │   ├── extrator.py        # Content extractor agent
    │   └── redator.py         # Content writer/editor agent
    │
    ├── prompts/               # AI prompts and agent instructions
    │   ├── instructions.py    # Detailed agent instructions
    │   └── prompts.py         # User prompts and templates
    │
    ├── tools/                 # Agent tools and custom functions
    │   └── agents_tools.py    # Custom tools for web scraping and search
    │
    ├── utils/                 # Utility modules and configurations
    │   ├── __init__.py        # Package initialization
    │   ├── config.py          # Environment variables and API key management
    │   └── utils.py           # Newsletter processor and voice generation
    │
    └── output/                # Generated files (created at runtime)
        ├── newsletter_*.mp3   # Generated audio newsletters
```

### Key Components

- **`src/main.py`**: Entry point that orchestrates the entire newsletter generation process
- **`src/news_agents/`**: Contains the three main agents (collector, extractor, writer) that work together
- **`src/utils/utils.py`**: Core `NewsletterProcessor` class that manages the pipeline
- **`src/utils/config.py`**: Handles API key validation and environment configuration
- **`src/tools/agents_tools.py`**: Custom tools for web search, scraping, and content extraction

## Setup and Installation

### Prerequisites
- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### 1. Clone the repository
```bash
git clone https://github.com/marcelomaiaf/multiAgentsNewsletter.git
cd multiAgentsNewsletter
```

### 2. Install dependencies
```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or on Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install project dependencies
uv sync
```

### 3. Configure environment variables
Create a `.env` file in the `src/` directory:

**Windows (Command Prompt):**
```cmd
copy nul src\.env
```

**Windows (PowerShell):**
```powershell
New-Item -Path "src\.env" -ItemType File
```

**Content of `src/.env`:**
```env
OPENAI_API_KEY=sk-proj-your_openai_api_key_here
serp_api=your_serpapi_key_here
fc_api=fc-your_firecrawl_api_key_here
eleven_api=sk_your_elevenlabs_api_key_here
```

### 4. API Keys Setup
- **OpenAI**: Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
- **SerpAPI**: Sign up at [SerpAPI](https://serpapi.com/) for web search
- **Firecrawl**: Get your key from [Firecrawl](https://firecrawl.dev/) for content extraction
- **ElevenLabs**: Register at [ElevenLabs](https://elevenlabs.io/) for voice generation

## How to Run

### Basic execution
```bash
# Run the main newsletter generator
uv run python src/main.py
```



### Using the NewsletterProcessor directly
Modify the folder prompts passing your own instructions e prompts

```python
import asyncio
from src.utils.utils import NewsletterProcessor, VoiceConfig

async def run_newsletter():
    # Customize voice settings
    voice_config = VoiceConfig(
        voice_id="your_preferred_voice_id",
        speed=1.2,
        stability=0.5
    )
    
    # Create processor
    processor = NewsletterProcessor(
        voice_config=voice_config,
        output_dir="custom_output",
        max_turns=25
    )
    
    # Run pipeline
    result = await processor.run("Your custom prompt")
    
    if result.success:
        print(f"Newsletter created: {result.audio_path}")
    else:
        print(f"Error: {result.error_message}")

# Run the async function
asyncio.run(run_newsletter())
```

## Output

The project generates:
- **Audio file**: `output/newsletter_YYYYMMDD.mp3`

## Technologies used

- **[OpenAI Agents SDK](https://github.com/openai/openai-python)** - Multi-agent orchestration
- **[SerpAPI](https://serpapi.com/)** - Web search for news collection
- **[Firecrawl](https://firecrawl.dev/)** - Web content extraction
- **[ElevenLabs](https://elevenlabs.io/)** - AI voice generation
- **[uv](https://docs.astral.sh/uv/)** - Modern Python package manager
- **Python 3.12+** - Programming language

## Features

**Multi-agent architecture** with specialized roles  
**Automated news collection** from multiple sources  
**Content extraction and summarization**  
**Natural voice generation** with ElevenLabs  
**Configurable voice settings**  
**Error handling and validation**  
**Easy-to-use API**  

## Troubleshooting

### Common Issues

**Import errors**: Make sure all dependencies are installed with `uv sync`

**API key errors**: Verify all API keys are correctly set in the `.env` file

**Audio generation fails**: Check ElevenLabs API quota and voice ID

**No news found**: Verify SerpAPI key and internet connection

### Getting Help

1. Check the example files in `src/example_usage.py`
2. Verify your `.env` configuration
3. Run with verbose logging for debugging

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.