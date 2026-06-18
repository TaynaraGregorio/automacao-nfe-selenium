from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import pandas as pd
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\tayna\Downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True    
})
navegador = webdriver.Chrome(options=options)
navegador.implicitly_wait(10)  # ✅ Aguarda elementos carregarem

# Caminhos corretos
pasta_exercicio = os.path.join(os.getcwd(), "19. Exercício - Automatizar Emissão de Nota Fiscal")
arquivo_html = os.path.join(pasta_exercicio, "login.html")
arquivo_excel = os.path.join(pasta_exercicio, "NotasEmitir.xlsx")

navegador.get(arquivo_html)

# Login
navegador.find_element("xpath", "/html/body/div/form/input[1]").send_keys("admin")
navegador.find_element("xpath", "/html/body/div/form/input[2]").send_keys("123456")
navegador.find_element("tag name", "button").click()

# ✅ Caminho completo para o Excel
df = pd.read_excel(arquivo_excel)

for index, row in df.iterrows():
    navegador.find_element("name", "nome").send_keys(row["Cliente"])
    navegador.find_element("name", "endereco").send_keys(row["Endereço"])
    navegador.find_element("name", "bairro").send_keys(row["Bairro"])
    navegador.find_element("name", "municipio").send_keys(row["Municipio"])
    navegador.find_element("name", "cep").send_keys(row["CEP"])

    elemento = navegador.find_element(By.TAG_NAME, 'select')
    Select(elemento).select_by_visible_text(row["UF"])

    navegador.find_element("name", "cnpj").send_keys(row["CPF/CNPJ"])
    navegador.find_element("name", "inscricao").send_keys(row["Inscricao Estadual"])
    navegador.find_element("name", "descricao").send_keys(row["Descrição"])
    navegador.find_element("name", "quantidade").send_keys(row["Quantidade"])
    navegador.find_element("name", "valor_unitario").send_keys(row["Valor Unitario"])
    navegador.find_element("name", "total").send_keys(row["Valor Total"])
    navegador.find_element("class name", "registerbtn").click()

    navegador.refresh()