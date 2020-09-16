#!/usr/bin/python
# todos os creditos para daniel vitor caetano albieri
import subprocess as o                                     
lista = [3]
cota = 0
while (cota < 100 ):
    print ('Menu')
    print ('Escolha uma opção')
    print ('1- atualizar sistema')
    print ('2- instalar java')
    print ('3- sair sem fazer nada')
    up = input()
    if up == ('1'):
         print ('atualizando sistema...')
         o.run(["sudo apt-get update]), shell=True"])
    elif up == ('2'):
        print ('atualizando e instalando java')
        o.run (['sudo apt-get update && sudo apt-get install default-java]), shell=True'])
    elif up != (lista):
        break
  
