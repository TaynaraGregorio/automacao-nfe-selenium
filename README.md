# 🧾 Automação de Emissão de Notas Fiscais com Python

Projeto desenvolvido em Python utilizando Selenium e Pandas para automatizar o preenchimento de um formulário HTML de emissão de notas fiscais a partir de uma planilha Excel.

## 🚀 Tecnologias utilizadas

- Python
- Selenium
- Pandas
- OpenPyXL

## 📋 Funcionamento

1. Os dados dos clientes e produtos são lidos de uma planilha Excel.
2. O Selenium acessa um formulário HTML.
3. Os campos são preenchidos automaticamente.
4. A nota é registrada.
5. Os campos são limpos para processar a próxima linha da planilha.
```

## 📊 Exemplo da planilha

| Cliente | Endereço | Bairro | Município | UF | Quantidade | Valor Unitário |
|-----------|---------|---------|-----------|----|------------|---------------|
| Empresa A | Rua X | Centro | Belo Horizonte | MG | 5 | 20.00 |
| Empresa B | Rua Y | Industrial | São Paulo | SP | 3 | 35.00 |

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/automacao-notas-fiscais-selenium.git
```

Entre na pasta:

```bash
cd automacao-notas-fiscais-selenium
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

## 🎯 Objetivo

Demonstrar a automação de processos utilizando Python, Selenium e manipulação de dados com Pandas, reduzindo tarefas repetitivas e aumentando a produtividade.

---

Desenvolvido por **Taynara Gregório** ❤️
