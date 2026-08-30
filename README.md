# Preenchimento Automático de Produtos

Script em Python para automação de cadastro de produtos em um sistema web, lendo os dados de uma planilha e preenchendo o formulário automaticamente, sem intervenção manual. Projeto desenvolvido como prática de automação de tarefas (RPA) com Python.

## 📋 Sobre o projeto

O script simula o comportamento de um usuário: abre o navegador, acessa o sistema, faz login e cadastra, um por um, todos os produtos listados em uma planilha CSV — preenchendo campos como código, marca, tipo, categoria, preço unitário, custo e observações.

## ⚙️ Como funciona

1. Abre o navegador Microsoft Edge e acessa o sistema de cadastro.
2. Realiza login automaticamente.
3. Lê a planilha `produtos.csv` com a biblioteca **pandas**.
4. Para cada produto na planilha, preenche o formulário de cadastro campo a campo, simulando digitação e navegação por teclado (`tab`, `enter`).
5. Repete o processo até que todos os produtos da planilha tenham sido cadastrados.

## 🛠️ Tecnologias utilizadas

- **Python**
- **PyAutoGUI** — automação de mouse e teclado
- **pandas** — leitura e manipulação da planilha de dados

## 📁 Estrutura do projeto

```
preenchimento-automatico/
├── codigo.py          # Script principal de automação
├── auxiliar.py         # Script auxiliar para identificar coordenadas na tela
└── produtos.csv        # Planilha de exemplo com os produtos a cadastrar
```

## ▶️ Como executar

### Pré-requisitos
- Python instalado
- Bibliotecas: `pyautogui`, `pandas`
  ```bash
  pip install pyautogui pandas
  ```

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/rui-fernando/preenchimento-automatico.git
   cd preenchimento-automatico
   ```
2. Ajuste as coordenadas de clique (`pyautogui.click(x=..., y=...)`) em `codigo.py` de acordo com a resolução da sua tela — use `auxiliar.py` para identificar as coordenadas corretas do seu ambiente.
3. Execute o script:
   ```bash
   python codigo.py
   ```
4. Evite mexer no mouse/teclado enquanto o script estiver rodando, já que ele controla a tela diretamente.

## 📌 Nota

Este projeto foi desenvolvido em um ambiente de treinamento/sandbox voltado para prática de automação, sem uso de dados ou sistemas reais.

## 👤 Autor

Desenvolvido por [Rui Fernando](https://github.com/rui-fernando), estudante de Ciência da Computação na Universidade Estadual da Paraíba (UEPB).
