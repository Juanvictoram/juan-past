import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=dolar&oq=dolar&gs_lcrp=EgZjaHJvbWUyDwgAEEUYORiDARixAxiABDINCAEQABiDARixAxiABDINCAIQABiDARixAxiABDINCAMQABiDARixAxiABDINCAQQABiDARixAxiABDINCAUQABiDARixAxiABDIGCAYQABgDMg0IBxAAGIMBGLEDGIAEMg0ICBAAGIMBGLEDGIAEMgoICRAAGLEDGIAE0gEINTU2MWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)
print(requisicao)
#print(requisicao.text)
site = BeautifulSoup(requisicao.text, "html.parser")
#print(site.prettify())

#pesquisa = site.find_all("span")
#print(pesquisa[36])
titulo = site.find( class_="vLqKYe")
#print(titulo.get_text())
pesquisa2 = site.find( class_= "DFlfde SwHCTb")
#print(pesquisa2.get_text())
#print(pesquisa2["data-value"])