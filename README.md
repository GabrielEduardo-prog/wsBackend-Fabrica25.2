# 📚 Sistema de Biblioteca Digital

**Sistema completo de gerenciamento de biblioteca desenvolvido em Django com integração à Google Books API**

![Django](https://img.shields.io/badge/Django-5.2.6-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![API](https://img.shields.io/badge/Google_Books_API-4285F4?style=for-the-badge&logo=google&logoColor=white)

## 🎯 O que é este projeto?

Este é um **sistema completo de biblioteca digital** que permite gerenciar livros e autores com funcionalidades avançadas:

- 📖 **CRUD Completo** - Criar, listar, editar e excluir livros e autores
- 🌐 **API Externa** - Buscar e importar livros da Google Books API
- 🎨 **Interface Moderna** - Design responsivo com gradientes e animações
- 📊 **Relatórios** - Estatísticas usando Jinja2
- 🔄 **Dual Templates** - Django Templates + Jinja2

## ⚡ Quick Start - 3 Passos!

### 1️⃣ Clone e Configure
```bash
git clone https://github.com/GabrielEduardo-prog/wsBackend-Fabrica25.2.git
cd wsBackend-Fabrica25.2
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 2️⃣ Database Setup
```bash
python manage.py migrate
```

### 3️⃣ Execute!
```bash
python manage.py runserver
```

**🚀 Acesse:** http://127.0.0.1:8000/biblioteca/

## 🎮 Como Usar - Guia Interativo

### 📚 Gerenciar Livros Locais
1. **Lista Principal** → Veja todos os livros cadastrados
2. **➕ Novo Livro** → Adicione livros manualmente
3. **✏️ Editar** → Modifique informações existentes
4. **🗑️ Excluir** → Remove livros do sistema

### 🔍 Importar da Google Books API
1. **🔍 Buscar na API** → Clique no botão na lista de livros
2. **Digite** → Título, autor ou palavra-chave
3. **Explore** → Resultados da Google Books
4. **⬇️ Importar** → Clique para adicionar à sua biblioteca
5. **Automático** → Sistema cria autor automaticamente!

### ✍️ Gerenciar Autores
1. **✍️ Escritores** → Acesse pelo menu
2. **Adicionar** → Nome e email dos autores
3. **Editar/Excluir** → Gerencie conforme necessário

### 📊 Visualizar Relatórios
1. **📊 Relatório Jinja2** → Abre em nova aba
2. **Estatísticas** → Total de livros, autores, ISBNs
3. **Lista Completa** → Todos os dados organizados

## 🏗️ Arquitetura Técnica



```

### 🌐 Integração Google Books API

**Endpoint:** `https://www.googleapis.com/books/v1/volumes`

**O que faz:**
- 🔍 Busca livros por qualquer termo
- 🇧🇷 Filtra livros em português
- 📊 Extrai: título, autor, ISBN, data
- 💾 Importa diretamente para o sistema
- 👤 Cria autores automaticamente

**Exemplo de uso:**
```python
# Buscar livros
livros = GoogleBooksService.buscar_livros("Machado de Assis")

# Importar livro
livro, msg = GoogleBooksService.importar_livro(livro_data)
```

## 🎨 Design e Interface

### 🌈 Paleta Visual
- **Primário:** `#667eea` (Azul moderno)
- **Secundário:** `#764ba2` (Roxo elegante)
- **Sucesso:** `#28a745` (Verde confirmação)
- **Background:** Gradientes dinâmicos

### ✨ Características
- **📱 Responsivo** - Funciona em qualquer dispositivo
- **🎭 Glassmorphism** - Efeitos de vidro modernos
- **🎯 Animações** - Transições suaves
- **📝 Tipografia** - Segoe UI para legibilidade
- **🎪 Interativo** - Hover effects e feedbacks

## 🛠️ Stack Tecnológico

### Backend
| Tecnologia | Versão | Função |
|------------|--------|--------|
| **Django** | 5.2.6 | Framework web principal |
| **Python** | 3.13 | Linguagem de programação |
| **SQLite** | - | Banco de dados ativo |
| **PostgreSQL** | - | Configurado (inativo) |

### Frontend
| Tecnologia | Função |
|------------|--------|
| **HTML5** | Estrutura semântica |
| **CSS3** | Estilização moderna (inline) |
| **CSS Grid/Flexbox** | Layout responsivo |

### Templates
| Engine | Uso |
|--------|-----|
| **Django Templates** | Interface principal |
| **Jinja2** | Relatórios específicos |

### APIs & Serviços
| Serviço | Função |
|---------|--------|
| **Google Books API** | Busca externa de livros |
| **requests** | Cliente HTTP |
| **Django REST** | APIs internas |

## 🔐 Segurança e Validações

### 🛡️ Medidas Implementadas
- ✅ **CSRF Protection** - Proteção contra ataques
- ✅ **SQL Injection** - ORM previne automaticamente
- ✅ **XSS Protection** - Templates com escape
- ✅ **ISBN Único** - Previne duplicatas
- ✅ **Validação Forms** - Campos obrigatórios
- ✅ **Integridade** - Relacionamentos consistentes

### 🔍 Validações de Negócio
- **ISBN único** por livro
- **Email válido** para autores
- **Relacionamentos** obrigatórios (Livro → Autor)
- **Tratamento de erros** da API externa

## 🗺️ Mapa de URLs

| URL | Descrição | Ação |
|-----|-----------|------|
| `/biblioteca/` | 🏠 Homepage | Lista livros + navegação |
| `/biblioteca/livro/create/` | ➕ Novo Livro | Formulário criação |
| `/biblioteca/livro/<id>/edit/` | ✏️ Editar | Formulário edição |
| `/biblioteca/livro/<id>/delete/` | 🗑️ Excluir | Confirmação exclusão |
| `/biblioteca/escritor/` | ✍️ Autores | Lista autores |
| `/biblioteca/escritor/create/` | ➕ Novo Autor | Formulário autor |
| `/biblioteca/buscar-api/` | 🔍 API Externa | Busca Google Books |
| `/biblioteca/relatorio/` | 📊 Relatórios | Jinja2 analytics |



## 🎯 Funcionalidades Destacadas

### 🔥 Principais Features
1. **🔄 CRUD Completo** - Operações em livros e autores
2. **🌐 API Integration** - Google Books em tempo real
3. **🎨 UI Moderna** - Design 2025 com gradientes
4. **📊 Analytics** - Relatórios com Jinja2
5. **📱 Responsivo** - Mobile-first design
6. **🔍 Busca Inteligente** - Filtros por título/autor
7. **⚡ Performance** - Django otimizado
8. **🛡️ Segurança** - Validações robustas

### 🚀 Diferenciais Técnicos
- **Dual Template Engines** (Django + Jinja2)
- **API Externa** com tratamento de erros
- **CSS Inline** para simplicidade e portabilidade
- **Relacionamentos** bem estruturados
- **Validações** em múltiplas camadas
- **Interface** intuitiva e moderna
- **Zero JavaScript** - Funciona apenas com HTML/CSS

## 🎉 Demonstração

### 📸 Screenshots das Funcionalidades

**🏠 Homepage - Lista de Livros**
- Interface clean com cards de livros
- Botões de ação visíveis
- Navegação intuitiva

**🔍 Busca na API**
- Campo de busca responsivo
- Resultados da Google Books
- Importação com um clique

**✏️ Formulários**
- Design moderno
- Validações em tempo real
- Feedback visual

**📊 Relatórios**
- Estatísticas organizadas
- Layout Jinja2
- Dados atualizados


### 🔧 Comandos Úteis
```bash
# Criar superuser
python manage.py createsuperuser

# Shell interativo
python manage.py shell

# Verificar erros
python manage.py check

# Migração específica
python manage.py migrate biblioteca

# Dados iniciais (se houver)
python manage.py loaddata initial_data.json
```

---

## 🎯 Resumo Executivo

**📚 Sistema de Biblioteca Digital** é uma aplicação web completa que demonstra:

- **🏗️ Arquitetura Django** profissional e escalável
- **🔄 CRUD Completo** com validações robustas
- **🌐 Integração API** externa (Google Books)
- **🎨 Interface Moderna** responsiva e intuitiva
- **📊 Relatórios** usando múltiplos template engines
- **🛡️ Segurança** e validações em múltiplas camadas

### 🎪 Por que este projeto se destaca?

1. **💡 Funcionalidade Real** - Não é apenas um CRUD básico
2. **🌐 API Externa** - Integração com serviços reais
3. **🎨 Design 2025** - Interface moderna e profissional
4. **🔧 Técnicas Avançadas** - Dual templates, services layer
5. **📱 UX Excelente** - Experiência de usuário cuidadosa
6. **🚀 Produção Ready** - Estrutura escalável

---

**🔥 Desenvolvido com paixão usando Django 5.2.6 + Python 3.13**

> *"Um sistema que demonstra não apenas conhecimento técnico, mas também visão de produto e atenção à experiência do usuário."*

