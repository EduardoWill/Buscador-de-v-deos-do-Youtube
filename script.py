from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class RoboYoutube:
    def __init__(self):
        # Configurações do ChromeDriver
        options = Options()
        options.add_argument("--disable-gpu")  # Desabilitar GPU
        self.webdriver = webdriver.Chrome(options=options)  # Inicia o driver com as opções

    def busca(self, busca, paginas):
        videos = []
        pagina = 1

        url = f"https://www.youtube.com/results?search_query={busca}"  #simula a barra de pesquisa usando o url
        self.webdriver.get(url)
        while pagina <= paginas:
            titulos = self.webdriver.find_elements(By.XPATH,"//a[@id='video-title']")
            for titulo in titulos: #laço que printa o título de todos os vídeos
                if titulo.text not in videos: #se o título estiver na lista ele pula
                    print("Esses foram os vídeos encontrados %s"% titulo.text)
                    videos.append(titulo.text)
            self.next_page(pagina)
            pagina +=1
    def next_page(self,pagina): #rola para baixo
        print(f"Mudando para a página {pagina + 1}")
        bottom = pagina * 10000
        self.webdriver.execute_script(f"window.scrollTo(0, {bottom})") #simula o scroll do mouse
        time.sleep(5)
        pass

# Inicializa o robô e realiza a busca
bot = RoboYoutube()
bot.busca("one piece", 5)
