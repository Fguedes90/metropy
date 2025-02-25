# Planejamento CI/CD

## Ferramentas
- GitHub Actions para CI/CD
- UV para gerenciamento de dependências
- Ruff para linting e formatação
- Pytest para testes
- Semantic Release para versionamento automático

## Estrutura de Branches
- `main`: branch principal, protegida
- `develop`: branch de desenvolvimento
- `feature/*`: branches para novas funcionalidades
- `fix/*`: branches para correções de bugs

## Fluxo de CI

### Pull Requests
1. Ativa quando:
   - PR aberto para `develop` ou `main`
   - Push em PR existente

2. Etapas:
   - Instalação de dependências com UV
   - Verificação de formatação com Ruff
   - Execução de linting com Ruff
   - Execução de testes com Pytest
   - Verificação de cobertura de código
   - Build do pacote para teste

### Push na Main
1. Ativa quando:
   - Push direto na `main`
   - Merge de PR na `main`

2. Etapas:
   - Todas as etapas do PR
   - Geração automática de versão
   - Publicação no PyPI

## Versionamento Semântico
Utilizando Semantic Release para automatizar:
- Incremento de versão baseado em commits
- Geração de CHANGELOG
- Criação de tags no GitHub
- Publicação de releases

### Padrão de Commits
Seguindo Conventional Commits:
- `feat`: Nova funcionalidade (MINOR)
- `fix`: Correção de bug (PATCH)
- `BREAKING CHANGE`: Mudança incompatível (MAJOR)
- `docs`: Documentação
- `chore`: Manutenção
- `test`: Testes
- `refactor`: Refatoração
- `style`: Formatação
- `perf`: Performance

## CHANGELOG
Gerado automaticamente baseado nos commits:
- Agrupado por tipo de mudança
- Links para commits e PRs
- Descrição detalhada das alterações
- Comparação com versão anterior

## Automações Adicionais
1. Dependabot:
   - Atualização automática de dependências
   - PRs automáticos para updates

2. CodeQL:
   - Análise de segurança automática
   - Alertas de vulnerabilidades

3. Issue Templates:
   - Bug report
   - Feature request
   - Pull request template

4. Badges Automáticas:
   - Status do CI
   - Cobertura de código
   - Versão no PyPI
   - Status das dependências

## Ambiente de Desenvolvimento
- Pre-commit hooks para:
  - Formatação
  - Linting
  - Verificação de tipos
  - Testes unitários

## Documentação
- Geração automática de docs
- Deploy automático no GitHub Pages
- Atualização do README com badges
