#!/usr/bin/env python3
# Script para testar via ping os roteadores da operadoras
# Arquivo de entrada no formato CSV
# Formato: Nome roteador, IP,Operadora, Localidade 
# Exemplo:Rot_MHNET_ADZ_Abelardo Luz,10.30.8.1,MHNET,Abelardo Luz
#
# importação de módulos
import subprocess
import teste_ping
import teste_snmp
from pysnmp import hlapi

# abertura dos arquivos de entrada e saída
lista_roteadores_entrada = open("lista_roteadores_entrada.txt","r")
lista_roteadores_saida = open ("lista_roteadores_saida.txt","w")
# Lê as linhas do arquivo de entrada
# Para cada linha, separa os campos e faz ping para os roteadores
# Gravando o resultado em um arquivo
if lista_roteadores_entrada.mode == "r":
   quantidade_linhas=lista_roteadores_entrada.readlines()
   for linha in quantidade_linhas:
      print (linha)
      itens=linha.split(',')
      nome_roteador=itens[0]
      IP=itens[1]
      operadora=itens[2]
      localidade_aux=itens[3]
      localidade=localidade_aux.rstrip("\n")
      print (itens[0])
      res = teste_ping.executa_teste_ping(IP) 
      if res == 0:
         saida_ping="OK"
      else:
         saida_ping="sem resposta"
      linha_do_arquivo=','.join([nome_roteador,IP,operadora,localidade,saida_ping+"\n"])
      lista_roteadores_saida.write(linha_do_arquivo)
lista_roteadores_entrada.close()
lista_roteadores_saida.close()
