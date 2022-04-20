import numpy as np
import cv2
from matplotlib import pyplot as plt
import math as m

camera= cv2.VideoCapture(0) #Inicia a câmera

xsb=[]              #Valores de x da matriz
ysb=[]              #Valores de y da matriz
xs=[]               #Valores de x da Amostra
ys=[]               #Valores de y da Amostra
Hor_min=230         #Limite mínimo horizontal
Hor_max=390         #Limite máximo horizontal
Ver_min=200         #Limite mínimo vertical
Ver_max=240         #Limite máximo vertical




def Captura_Imagem():        #função de captura de imagem
    Val, img = camera.read()
    return img

def Img_para_Espectro(img, nome, branco):

    global xsb          #lista valores de x do branco
    global ysb          #lista valores de y do branco
    global xs           #lista valores de x
    global ys           #lista valores de y
    
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # converte a imagem para cinza

    #Dados de calibração da conversão Coluna->Comprimento de Onda (y=ax+b)
    a=2.01
    b=-97.05
    
    print('Processando Dados...')
    for coluna in range(Hor_min,Hor_max): #range de colunas analisadas

        x= a*coluna+b               #aplica a calibração dos valores de x
        if branco==1:
            xsb.append(x)           #adiciona o valor de x no branco 
        else:
            xs.append(x)            #adiciona o valor de x na medida
        y=0
        for linha in range(Ver_min,Ver_max):        #range de linhas analisadas
        
            y=y+(gray[linha,coluna]) #soma os valores de cada pixel da coluna em y
            
            if linha==Ver_max-1:      #ao final da coluna, adiciona a soma de y na lista

                if branco==1:
                    ysb.append(y)
                else:
                    #ADICIONAR AQUI CALCULOS DE TRANSMITANCIA E ABSORVANCIA
                    yT= y*1.0/ysb[coluna-Hor_min]           #converte o valor de y para Transmitância
                    yABS= - m.log(yT,10)        #converte o valor de y de Transmitância para Absorvância
                    #ys.append(y)
                    ys.append(yABS)
            else:
                pass

    if branco==0:
        texto= ''
        print('Salvando Arquivos...')
        for i in range(len(xs)):        #adiciona cada par do espectro em um arquivo externo
            texto= texto+str(xs[i])+';'+str(ys[i])+'\n'     
        salva= open(nome+'.txt','w')
        salva.write(texto)
        salva.close()
        plt.plot(xs,ys)
        plt.show()
                       
            
            

def Medida(NomeArq,branco):
    
    
    for i in range(15):
        temp = Captura_Imagem()  # Bate algumas fotos para ajustar a camera
    print('Capturando Imagem...')
    capMed= Captura_Imagem()    # Captura a imagem de medida
    Img_para_Espectro(capMed,NomeArq, branco)
    
    if branco == 1:
        pass
    else:
        crop = capMed[Ver_min:Ver_max, Hor_min:Hor_max]
        cv2.imwrite(NomeArq+'.png',crop)#salva um arquivo de imagem da medida 
        print('Arquivos Salvos!')
    
    

def main():         #PROGRAMA PRINCIPAL

    arq = input("Digite o nome do arquivo: ")       #Recebe o nome do arquivo 
    
    while True:
        iniciamedidaB= input("Iniciar a análise da matriz (branco)? (s/n): ") #Aguarda para iniciar a medida
        if iniciamedidaB == "s" :
            Medida(arq+"_branco",1)         #Inicia a medida do branco
            
            while True:
                iniciamedidaAm= input("Iniciar medida da amostra?(s/n): ")  #Aguarda para iniciar a medida
                if iniciamedidaAm== "s":
                    Medida(arq,0)       #Inicia a medida da Amostra
                    break
                else:
                    pass
            print()
            print('Obrigado por utilizar o LabitanSpec')
            print()

            break
        
        else:
            pass

    
main()
