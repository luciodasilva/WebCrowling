from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

#teste
#Não abrir Navegador
#options = webdriver.ChromeOptions()
#options.add_argument("--headless")
#driver = webdriver.Chrome(chrome_options=options)


driver.get("https://tdwebconference.com/?rc=WmfqCi7ZWsPW&rs=whatsapp")

fieldname = driver.find_element_by_id("form-field-name")
fieldname.send_keys("Haroldo Rodrigues")

fieldemail = driver.find_element_by_id("form-field-email")
fieldemail.send_keys("haroldorodrigues@gmail.com")

fieldfone = driver.find_element_by_id("form-field-telefone")
fieldfone.send_keys("  11 9 5253 3441")

fieldrole = driver.find_element_by_id("form-field-cargo")
fieldrole.send_keys("Assistente")

fielddpto = driver.find_element_by_id("form-field-departamento")
fielddpto.send_keys("Tecnologia")

fieldco = driver.find_element_by_id("form-field-empresa")
fieldco.send_keys("Atento Brasil SA")

fieldfunclen = driver.find_element_by_id("form-field-funcionarios")
fieldfunclen.send_keys("Mais de 5000")

sleep(10)

fieldcountry = driver.find_element_by_id("form-field-pais")
fieldcountry.send_keys("Brasil")

fieldterm = driver.find_element_by_id("form-field-termos_de_uso")
fieldterm.click()


btnsubmit = driver.find_element_by_class_name("elementor-button")
btnsubmit.click()


driver.close()