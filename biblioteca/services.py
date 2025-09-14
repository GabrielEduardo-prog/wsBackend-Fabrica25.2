import requests
from datetime import datetime
from .models import Livro, Escritor


class GoogleBooksService:
    """
    Serviço para consumir a API do Google Books
    """
    BASE_URL = 'https://www.googleapis.com/books/v1/volumes'
    
    @staticmethod
    def buscar_livros(query, max_results=10):
        """
        Busca livros na API do Google Books
        """
        try:
            params = {
                'q': query,
                'maxResults': max_results,
                'langRestrict': 'pt'  
            }
            
            response = requests.get(GoogleBooksService.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            livros = []
            
            if 'items' in data:
                for item in data['items']:
                    livro_info = GoogleBooksService._extrair_info_livro(item)
                    if livro_info:
                        livros.append(livro_info)
            
            return livros
            
        except requests.RequestException as e:
            print(f"Erro ao buscar livros: {e}")
            return []
    
    @staticmethod
    def _extrair_info_livro(item):
        """
        Extrai informações relevantes de um livro da resposta da API
        """
        try:
            volume_info = item.get('volumeInfo', {})
            
            titulo = volume_info.get('title', 'Título não disponível')
            autores = volume_info.get('authors', ['Autor desconhecido'])
            autor_principal = autores[0] if autores else 'Autor desconhecido'
            
            
            data_publicacao = None
            published_date = volume_info.get('publishedDate', '')
            if published_date:
                try:
                    
                    if len(published_date) == 4:  
                        data_publicacao = datetime.strptime(f"{published_date}-01-01", "%Y-%m-%d").date()
                    elif len(published_date) == 7:  
                        data_publicacao = datetime.strptime(f"{published_date}-01", "%Y-%m-%d").date()
                    else:  
                        data_publicacao = datetime.strptime(published_date, "%Y-%m-%d").date()
                except ValueError:
                    pass
            
           
            isbn = None
            industry_identifiers = volume_info.get('industryIdentifiers', [])
            for identifier in industry_identifiers:
                if identifier.get('type') in ['ISBN_13', 'ISBN_10']:
                    isbn = identifier.get('identifier')
                    break
            
            
            descricao = volume_info.get('description', '')
            categoria = ', '.join(volume_info.get('categories', []))
            imagem = volume_info.get('imageLinks', {}).get('thumbnail', '')
            
            return {
                'titulo': titulo,
                'autor': autor_principal,
                'data_publicacao': data_publicacao,
                'isbn': isbn,
                'descricao': descricao[:500] if descricao else '',  
                'categoria': categoria,
                'imagem': imagem,
                'google_id': item.get('id')
            }
            
        except Exception as e:
            print(f"Erro ao extrair informações do livro: {e}")
            return None
    
    @staticmethod
    def importar_livro(livro_data):
        """
        Importa um livro da API para o banco de dados local
        """
        try:
           
            if livro_data.get('isbn'):
                if Livro.objects.filter(isbn=livro_data['isbn']).exists():
                    return None, "Livro já existe (ISBN duplicado)"
            
            
            escritor, created = Escritor.objects.get_or_create(
                nome=livro_data['autor'],
                defaults={'email': ''}  
            )
            
            
            livro = Livro.objects.create(
                titulo=livro_data['titulo'],
                escritor=escritor,
                data_publicacao=livro_data.get('data_publicacao'),
                isbn=livro_data.get('isbn', '')
            )
            
            return livro, "Livro importado com sucesso"
            
        except Exception as e:
            return None, f"Erro ao importar livro: {str(e)}"