# Memo & Planejamento do Projeto

## Visão Geral
Projeto de coleta e análise de dados de e-commerce com agentes de IA locais (Ollama) e https://docs.crawl4ai.com/, armazenamento em Firebase, ETL para data warehouse e dashboard com Streamlit.

## Status Atual
- Estrutura de pastas e módulos criada
- Integração inicial com Firebase e Ollama
- Dependências para scraping, IA, ETL, dashboard e testes instaladas
- Estrutura de testes unitários pronta para TDD

## Próximos Passos Sugeridos
1. **Agente de Coleta**
   - Implementar busca automática de lojas virtuais por país
   - Definir padrão de extração de produtos (nome, preço, descrição, categorias)
   - Integrar Ollama para classificação/categorização
2. **Schema de Dados no Firebase**
   - Definir e documentar o formato dos dados de produto
   - Implementar validação e exemplos de escrita/leitura
3. **ETL**
   - Definir transformações e agregações relevantes
   - Garantir compatibilidade com o data warehouse
4. **Dashboard**
   - Criar visualizações iniciais (preço, categorias, tendências)
   - Adicionar filtros e métricas de negócio
5. **Testes e TDD**
   - Escrever testes antes de cada nova funcionalidade
   - Cobertura mínima recomendada: 80%

## Decisões Tomadas
- Uso de pytest para TDD
- Firebase Realtime Database como backend
- Ollama para IA local
- Estrutura modular para facilitar manutenção

## Anotações Rápidas
- Adicionar exemplos de uso no README
- Automatizar execução de testes via task do VS Code
- Documentar endpoints e fluxos principais

---

> Atualize este arquivo sempre que tomar decisões, implementar novas features ou planejar próximos ciclos.
