from re import sub
import subprocess

def extract_wifi_passwords():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')

    profilies = [i.split(':')[1].strip() for i in profiles_data if 'All user profile' in i]

    for profile in profilies:
        profile_info = subprocess.check_output('netsh wlan show profile {profile} key=clear').decode('utf-8').split('\n')

        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Key Content' in i]
        except IndexError:
            password = None

        print(f'Profile: {profile}\nPassword: {password}\n{"#" * 20}')

        with open(file='wifi_password.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Profile: {profile}\nPassword: {password}\n{"#" * 20}')


extract_wifi_passwords()

"""
use command
pyinstaller --onefile wifiPassword.py
to make exe file

"""
