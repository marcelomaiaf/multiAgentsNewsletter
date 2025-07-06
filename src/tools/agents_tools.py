import json
from datetime import datetime

import requests
from agents import function_tool
from firecrawl import FirecrawlApp

from utils.config import Config


@function_tool
def verificar_data(data: str):
  data = datetime.strptime(data, "%d/%m/%Y")
  hoje = datetime.today()
  subtracao = (hoje - data)
  if subtracao.days <= 15:
    return True
  else:
    return False

@function_tool
def buscar_noticias(query: str):
  print(query)
  url = "https://serpapi.com/search"
  params = {
          "engine":"google",
          "q":query,
          "location_requested":"Brazil",
          "location_used":"Brazil",
          "google_domain":"google.com.br",
          "hl":"pt",
          "gl":"br",
          "num":"15",
          "device":"desktop",
          "tbm":"nws",
          "tbs":"qdr:m",
          "api_key": Config.get_serp_key()
          }
  response = requests.get(url=url,params=params)
  print(json.loads(response.text).get('news_results')[0])
  return str(json.loads(response.text).get('news_results'))

fc = FirecrawlApp(api_key=Config.get_firecrawl_key())
@function_tool
def crawler(url: str):
  #No futuro usar pydantic para tipar o output do firecrawl
  scrape_result = fc.scrape_url(url, formats=['markdown'],only_main_content=True)
  return scrape_result.markdown

def get_extrator_tool():
    """Lazy loading do extrator para evitar importação circular"""
    from news_agents.extrator import extrator
    return extrator.as_tool(
        tool_name="extrator_noticias",
        tool_description="Obtém um resumo estruturado da notícia",
    )


