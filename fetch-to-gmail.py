#!/usr/bin/python

# Modo debug mediante environment variable
from os import getenv


# Para ocultar la ventana del navegador
from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Para ocultar el password, que no se vea a simple vista
# Nota: Sigue siendo inseguro dejar el password en un script!
from credenciales import usuario, passwd
from base64 import b64decode

# Para correr sin interfaz grafica
visible = getenv('VISIBLE') or 0
display = Display(visible=visible, size=(800, 600))
display.start()

driver = webdriver.Chrome()
driver.get("http://gmail.com")

driver.find_element_by_name("Email").send_keys(usuario)
driver.find_element_by_id("next").click()
sleep(1)

elem = driver.find_element_by_name("Passwd")
elem.send_keys(b64decode(passwd))
driver.find_element_by_id("signIn").click()

driver.get('https://mail.google.com/mail/u/0/#settings/accounts')

sleep(10)  # Me aseguro de que la pagina termine de cargar

xpath = "//*[contains(text(), 'Comprobar si tengo correo ahora')]"

# El nro de cuentas a comprobar
tope = len(driver.find_elements_by_xpath(xpath))

a = 0
while True:
    elem = driver.find_element_by_xpath(xpath)
    try:
        elem.click()
        sleep(1)
        a = a + 1
	if visible:
	    print "%d/%d" % (a, tope)
    except:
        pass

    if a == tope:
        break

driver.close()  # cierro el navegador
display.stop()  # termino el display virtual
