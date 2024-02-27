# comom tirar print(foto) da telainteira ou parte dela
import pyautogui
# tirar print da tela inteira
pyautogui.screenshot('tela.jpg')
# tirar print de parte d tela
pyautogui.screenshot('prompt de comando.jpg',region=(655,10,650,2))

