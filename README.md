# syscall

Syscall - Sistema Interno de Chamados

# Índice

1. Sobre o Projeto

2. Requisitos

3. Funcionalidades

4. Workflow

5. Instalação

6. Tecnologias Utilizadas

7. Uso Interno

8. Contato

# 1 - Sobre o Projeto

    O Syscall é um sistema simples para o atendimento de chamados internos, desenvolvido em Python com banco de dados MySQL. Destina‑se a gerenciar solicitações de suporte dentro da companhia de forma organizada e controlada.

# 2 - Requisitos

    Python 3.x

    MySQL

    Dependências Python (no requirements.txt):

    asgiref==3.8.1
    Django==5.1.6
    mysqlclient==2.2.7
    sqlparse==0.5.3
    tzdata==2025.1

# 3 - Funcionalidades

    Cadastro de usuários em dois cargos:

    Líder de Posto: abre e acompanha chamados.

    Suporte Técnico: atende, edita, altera status, cadastra usuários, reseta senhas e reabre chamados.

    Identificação automática de cada chamado por número.

    Controle de acesso baseado em e-mail e senha (mínimo 8 caracteres, combinação de letras, números e opcionalmente caracteres especiais).

# 4 - Workflow

**Abertura do chamado (Líder de Posto):**

    Posto (preenchido automaticamente)

    Telefone para contato

    Endereço IPv4 do computador

    Solicitante (nome do líder, preenchido automaticamente)

    Descrição do problema

**Acompanhamento:** 

    O Líder vê todos os chamados do seu posto, em qualquer status.

**Atendimento (Suporte Técnico):**

    Adicionar/editar informações no campo "Resposta"

    Alterar status:

        Aberto (novo)

        Em andamento

        Fechado

    Encerrar ou reabrir chamados, cadastrar usuários, resetar senha.

**Reset de senha:** 

    Líder de posto deve contatar o suporte pelo telefone (62) 3201 2706 para redefinir sua senha.

# 5 - Instalação

    # Clone o repositório
    git clone https://github.com/PatoRoco38/syscall.git

    # Acesse o diretório
    cd syscall

    # (Opcional) Crie e ative um ambiente virtual
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

    # Instale as dependências
    pip install -r requirements.txt

# 6 - Tecnologias Utilizadas

    Python

    Django

    MySQL

    HTML, JavaScript e CSS para o front-end Bootstrap

# 7 - Uso Interno

Esta aplicação é somente para uso interno da companhia. O link não deve ser compartilhado com terceiros e pessoas de fora não têm permissão para abrir reclamações ou acessar o sistema.

# 8 - Contato

    Para críticas, sugestões ou dúvidas, entre em contato por e-mail:

    renato.lancelot@gmail.com

    PS: Este foi o primeiro sistema que criei. Agradeço seu feedback!