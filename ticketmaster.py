from os import system
from threading import Thread
from time import sleep
from selenium import webdriver


# Crea nuestro driver para navegar por internet
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

def checar_boletos(sitio):
    """ Checa si hay boletos disponibles. """

    print("Descargando para {0}...".format(sitio["nombre"]))
    driver.get(sitio["url"])
    sleep(3)

    try:
        # Only exists when there are no tickets
        driver.find_element_by_xpath("//*[@id=\"quickpicks\"]/div[2]/div/span[1]")
        print("Aún no hay boletos :(")
    except:
        print("----------------Hay boletos para {0}!---------------".format(sitio["nombre"]))
        thread = Thread(target=sound_alarm)
        thread.start()


def sound_alarm():
    lapse = 0.1
    up = True
    delta = 1
    while delta > 0:
        freq = 600 if up else 500
        system('play -nq -t alsa synth {} sine {}'.format(lapse, freq))
        up = not up
        delta -= lapse * 0.5
        sleep(lapse)

# Los sitios a checar
sitios = [
    {
        "nombre": "Jueves en general",
        "url": "https://www.ticketmaster.com.mx/rammstein-america-stadium-tour-2020-feuerzone-ga-general-a-y-b-mexico-01-10-2021/event/14005837DFA7FC4C",
    },
    #
    #{
    #    "nombre": "Jueves en grada",
    #    "url": "https://www.ticketmaster.com.mx/rammstein-america-stadium-tour-2020-grada-norte-y-sur-mexico-01-10-2021/event/14005837E8481F55"
    #},
    {
        "nombre": "Viernes en general",
        "url": "https://www.ticketmaster.com.mx/rammstein-amerika-stadium-tour-2020-feuerzone-ga-general-a-y-b-mexico-02-10-2021/event/1400582ADCD487CE"
    }
    #{
    #    "nombre": "Viernes en grada",
    #    "url": "https://www.ticketmaster.com.mx/rammstein-amerika-stadium-tour-2020-grada-norte-y-sur-mexico-02-10-2021/event/1400582AC3D267F6"
    #}
]

# Starts the program
while True:
    for sitio in sitios:
        checar_boletos(sitio)
