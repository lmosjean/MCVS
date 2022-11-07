# MCVS v0.2
Modular computational vision system
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Este é um sistema de visão computacional, o objetivo geral é a sua integração com MCUs externas como STM32 e Arduino e funcionamento em computadores de placa unica.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Funcionamento:

Atualmente está rodando em um pc com webcam, pode ser adapdato para computadores de placa única(RaspberryPi, OrangePi)
Interpreta gestos feitos com a mão direita, faz a contagem de dedos mostrados e utiliza este valor para enviar comandos para um microcontrolador.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Comunicação com a MCU:

Utiliza o protocolo firmata para a comunicação serial com a MCU. Para utilizar um modulo bluetooth no arduino e um dongle USB Bluetooth no PC foram feitas alterações no sketch 'Standard Firmata' para adequar a Baud Rate do módulo.  
Utilizar este protocolo permite que comandos sejam enviados ao microcontrolador de maneira remota, sem a necessidade de atualizar o codigo no lado do arduino a cada nova alteração. Neste caso, as portas podem ser utilizadas tanto como saidas quanto entradas. (EX:controlar motores pelo pc, ou ler sensores e enviar para o python)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
_______________________________________________________________________________________________________________________________________________________________________
Implementações futuras:

Reconhecimento de objetos

Trackeamento de rosto (follow me)

Protocolo MQTT + ESP32

Integração com MYSQL  

Travas de segurança em perda de conexão

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Hardware utilizado:
Arduino Pro Mini 5v
Modulo Bluetooth Baud Rate : [9600]
L293 + PCB customizada
LM7805
Mecanica + motores de um carrinho de brinquedo. 
Bateria de LI-Io, 2200Mah

Hardware desenvolvidas para este projeto
Estes ainda estão em teste, serão disponibilizados em breve. 

-PCI Driver L293 (Ponte H) : [LINK]
-PCI Arduino Standalone : [LINK]

As placas foram desenvolvidas utilizando o software Proteus 8.5 e prototipadas em CNC laser. 
Confira o processo: [LINK]
_______________________________________________________________________________________________________________________________________________________________________

