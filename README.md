
# Programa python para aplicar alguns ruídos, filtros de suavização e detectores de borda. 
## Autores: Bruno Machado Ferreira e Ernani Neto

Testado com

- Ubuntu 20.04
- Conda 4.10.3
- Python 3.9.7

Autor: Bruno Machado Ferreira, Ernani Neto, Fábio Gomes, Ryan Henrique Nantes


### Preparar o ambiente e instalar dependências.
- $ conda create -n vc
- $ conda env list
- $ conda activate vc
- $ conda install scikit-image opencv
- $ conda list

**Remove tudo para instalar de novo:**
- $ conda remove --name vc --all


### Executar o código para uma imagem
Comandos úteis:
- $ conda activate vc
- $ python --version
- $ python ruidoSuaveBordas.py -i exemplo.jpg -r poisson -pr 20 -s mediana -ps 200 -b robert


### Resultados esperados

- Ao fim do processamento da imagem escolhida, exibe um painel com a versão original e 3 resultantes
  de acordo com os parâmetros inseridos no comando de uso;
- Salvará as imagens resultantes em disco na 
  pasta "postprocessing", separadas da original e com nome modificado.
