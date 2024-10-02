import asyncio
import pandas as pd
import aiohttp
from django.core.management.base import BaseCommand
from data_loader.models import Produto

class Command(BaseCommand):
    help = 'Carrega dados da planilha e enriquece com API externa.'

    async def fetch_dados_adicionais(self, session, produto):
        
        url = f'http://localhost:8000/api_mock/produtos/{produto["id"]}/'
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()  # Obtiene os dados de  API mock
            return {}

    async def process_data(self, dados):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for _, produto in dados.iterrows():
                task = asyncio.ensure_future(self.fetch_dados_adicionais(session, produto))
                tasks.append(task)
            resultados = await asyncio.gather(*tasks)
            return resultados

    def handle(self, *args, **kwargs):
        # Carrega o plnailha
        caminho = 'C:/Users/pablo/Desktop/Projeto_Pablo_Perez/projetopabloperez/Produtos3.csv'  # o .xlsx
        dados = pd.read_csv(caminho, encoding='ISO-8859-1')

        # Limpeza de dados
        dados = dados.dropna(subset=['nome', 'preco'])
        dados['preco'] = dados['preco'].astype(float)

        # Enriquecer dados com API externa
        loop = asyncio.get_event_loop()
        dados_adicionais = loop.run_until_complete(self.process_data(dados))

        # Atualizar ou criar objetos Produto
        for index, produto in dados.iterrows():
            Produto.objects.update_or_create(
                nome=produto['nome'],
                defaults={
                    'categoria': produto['categoria'],
                    'preco': produto['preco'],
                    'descricao': produto.get('descricao', ''),
                     'stock': produto['stock'],
                    'dados_adicionais': dados_adicionais[index]  # Dados adicionais são armazenados aqui
                }
            )

        self.stdout.write(self.style.SUCCESS('Dados carregados e enriquecidos com sucesso!'))
