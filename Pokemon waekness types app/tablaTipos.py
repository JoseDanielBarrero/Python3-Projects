import numpy as np

tipos=["acero","agua","bicho","dragon","electrico","fantasma","fuego","hielo",
       "lucha","normal","planta","psiquico","roca","siniestro","tierra",
       "veneno","volador"]

acero_strn=[7,12]
agua_strn=[6,12,14]
bicho_strn=[10,11,13]
dragon_strn=[3]
electrico_strn=[1,16]
fantasma_strn=[5,11]
fuego_strn=[0,2,7,9]
hielo_strn=[3,10,14,16]
lucha_strn=[0,7,9,12,13]
normal_strn=[]
planta_strn=[1,12,14]
psiquico_strn=[8,15]
roca_strn=[2,6,7,16]
siniestro_strn=[5,11]
tierra_strn=[0,4,6,12,15]
veneno_strn=[10]
volador_strn=[2,8,10]
debilidades = [acero_strn,agua_strn,bicho_strn,dragon_strn,electrico_strn,fantasma_strn,
               fuego_strn,hielo_strn,lucha_strn,normal_strn,planta_strn,psiquico_strn,roca_strn
               ,siniestro_strn,tierra_strn,veneno_strn,volador_strn]  

ACERO_DEB=[0,1,4,6]
AGUA_DEB=[1,3,10]
BICHO_DEB=[0,5,6,8,15,16]
DRAGON_DEB=[0]
ELECTRICO_DEB=[3,4,10]
FANTASMA_DEB=[0,13]
FUEGO_DEB=[1,3,6,12]
HIELO_DEB=[0,1,6,7]
LUCHA_DEB=[2,11,15,16]
NORMAL_DEB=[0,12]
PLANTA_DEB=[0,2,3,6,10,15,16]
PSIQUICO_DEB=[0,11]
ROCA_DEB=[0,8,14]
SINIESTRO_DEB=[0,8,13]
TIERRA_DEB=[2,10]
VENENO_DEB=[5,12,14,15]
VOLADOR_DEB=[0,4,12]

fortalezas =[ACERO_DEB,AGUA_DEB,BICHO_DEB,DRAGON_DEB,ELECTRICO_DEB,FANTASMA_DEB,FUEGO_DEB
             ,HIELO_DEB,LUCHA_DEB,NORMAL_DEB,PLANTA_DEB,PSIQUICO_DEB,ROCA_DEB,SINIESTRO_DEB,
             TIERRA_DEB,VENENO_DEB,VOLADOR_DEB]

def getTipos():
    return tipos

def getDebilidades():
    return debilidades

def getFortalezas():
    return fortalezas

def tabla_de_tipos_3ra():
    
    ## Creación de la tabla
    
    TABLA_DE_TIPOS = np.ones((17,17))
    
    # Anexo de ataques nulos
    
    TABLA_DE_TIPOS[15,0]=0
    TABLA_DE_TIPOS[14,16]=0
    TABLA_DE_TIPOS[11,13]=0
    TABLA_DE_TIPOS[9,5]=0
    TABLA_DE_TIPOS[8,5]=0
    TABLA_DE_TIPOS[5,9]=0
    TABLA_DE_TIPOS[4,14]=0
    
    # Anexo final a la matriz de la tabal de tipos 
    # Debilidades
    
    TABLA_DE_TIPOS[(0,ACERO_DEB[:])]=0.5
    TABLA_DE_TIPOS[(1,AGUA_DEB[:])]=0.5
    TABLA_DE_TIPOS[(2,BICHO_DEB[:])]=0.5
    TABLA_DE_TIPOS[(3,DRAGON_DEB[:])]=0.5
    TABLA_DE_TIPOS[(4,ELECTRICO_DEB[:])]=0.5
    TABLA_DE_TIPOS[(5,FANTASMA_DEB[:])]=0.5
    TABLA_DE_TIPOS[(6,FUEGO_DEB[:])]=0.5
    TABLA_DE_TIPOS[(7,HIELO_DEB[:])]=0.5
    TABLA_DE_TIPOS[(8,LUCHA_DEB[:])]=0.5
    TABLA_DE_TIPOS[(9,NORMAL_DEB[:])]=0.5
    TABLA_DE_TIPOS[(10,PLANTA_DEB[:])]=0.5
    TABLA_DE_TIPOS[(11,PSIQUICO_DEB[:])]=0.5
    TABLA_DE_TIPOS[(12,ROCA_DEB[:])]=0.5
    TABLA_DE_TIPOS[(13,SINIESTRO_DEB[:])]=0.5
    TABLA_DE_TIPOS[(14,TIERRA_DEB[:])]=0.5
    TABLA_DE_TIPOS[(15,VENENO_DEB[:])]=0.5
    TABLA_DE_TIPOS[(16,VOLADOR_DEB[:])]=0.5
    
    # Fortalezas
    
    TABLA_DE_TIPOS[0,acero_strn[:]]=2
    TABLA_DE_TIPOS[1,agua_strn[:]]=2
    TABLA_DE_TIPOS[2,bicho_strn[:]]=2
    TABLA_DE_TIPOS[3,dragon_strn[:]]=2
    TABLA_DE_TIPOS[4,electrico_strn[:]]=2
    TABLA_DE_TIPOS[5,fantasma_strn[:]]=2
    TABLA_DE_TIPOS[6,fuego_strn[:]]=2
    TABLA_DE_TIPOS[7,hielo_strn[:]]=2
    TABLA_DE_TIPOS[8,lucha_strn[:]]=2
    TABLA_DE_TIPOS[9,normal_strn[:]]=2
    TABLA_DE_TIPOS[10,planta_strn[:]]=2
    TABLA_DE_TIPOS[11,psiquico_strn[:]]=2
    TABLA_DE_TIPOS[12,roca_strn[:]]=2
    TABLA_DE_TIPOS[13,siniestro_strn[:]]=2
    TABLA_DE_TIPOS[14,tierra_strn[:]]=2
    TABLA_DE_TIPOS[15,veneno_strn[:]]=2
    TABLA_DE_TIPOS[16,volador_strn[:]]=2
    
    # print(TABLA_DE_TIPOS)
    return TABLA_DE_TIPOS
