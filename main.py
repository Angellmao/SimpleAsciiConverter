import pyfiglet
import time
import os

error = '[ERROR]'
unsuccess = '[-]'
success = '[+]'

def main():
    banner = pyfiglet.figlet_format('Ascii Converter')
    print(banner + '\n')
    your_ascii = input('\n' + '[>] Write text you wanna convert to ascii: ')

    os.system('cls')
    print('Converting...')
    time.sleep(2)
    os.system('cls')
    your_ascii = pyfiglet.figlet_format(your_ascii)
    print('[>] Results: ')
    print(your_ascii + '\n')
    time.sleep(1)
    save = input('Do you wanna to save results to text file(y/n): ')
    if save == 'y':
        results_txt = open('results.txt', 'a')
        results_txt.write(your_ascii)
        if os.path.exists('results.txt'):
            print(f'{success} Succsefully created a text file.' + '\n')
            print('Closing in 3 seconds...')
            time.sleep(3)
            exit
        else:
            print(f'{unsuccess} Text file didnt created.' + '\n')
            print('Closing in 3 seconds...')
            time.sleep(3)
            exit
    else:
        os.system('pause')
        exit

try:
    if __name__ == '__main__':
        main()
except:
    print(f'{error} Cant open script.')
    print('Closing in 3 seconds...')
    time.sleep(3)
    exit