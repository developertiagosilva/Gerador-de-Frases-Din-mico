# 🌱 Jornada Django — Nível 1: Gerador de Frases Dinâmico

Este repositório marca o início da minha jornada de desenvolvimento com o framework Django. O objetivo deste primeiro nível foi quebrar a inércia, compreender a arquitetura fundamental do framework e colocar uma aplicação web dinâmica para rodar do zero.

O projeto consiste em um **Gerador de Frases Motivacionais** voltado para desenvolvedores, exibindo dados dinâmicos processados no servidor a cada requisição.

---

## 🏗️ O que foi aprendido e aplicado (MVT)

Neste nível, dominei o fluxo básico de uma requisição Django utilizando a arquitetura **MVT (Model-View-Template)**:

1. **Rotas (`urls.py`):** Configuração e mapeamento de caminhos de URL para direcionar as requisições do usuário.
2. **Visões (`views.py`):** Construção da lógica de negócios em Python, utilizando o módulo `datetime` para capturar o horário do servidor em tempo real e a biblioteca `random` para selecionar elementos aleatórios.
3. **Templates (`.html`):** Renderização dinâmica de dados no front-end utilizando o motor de templates do Django (`{{ variavel }}`) e estilização ágil com **Bootstrap 5**.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11+**
* **Django 6.0+**
* **Bootstrap 5** (via CDN para interface responsiva)
* **PowerShell / Terminal** para gerenciamento de ambiente virtual (`.venv`) e automação de arquivos

---

## 📸 Como ficou o projeto

O servidor processa a requisição, escolhe uma frase aleatória, carimba o horário exato da geração no rodapé e entrega um card limpo e responsivo:



---

## 🚀 Como executar este projeto localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/DJANGO_5.git](https://github.com/SEU_USUARIO/DJANGO_5.git)
   cd DJANGO_5