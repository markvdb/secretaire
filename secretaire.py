import subprocess
import time

def switch_tty(tty_number):
    '''
    We want to make sure the keyboard is attached to a tty.
    Alternatives using evdev are needlessly complicated, especially
    with international keyboard layouts.
    '''
    try:
        subprocess.run(['chvt', str(tty_number)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("Error: Changing tty requires root privileges.")


def select_task():
    options = ['calendar','contacts', 'email', 'news', 'radio', 'sms', 'wikipedia', 'youtube']
    task = ''
    task_menu = "Make your choice:\n"
    for index, item in enumerate(options):
        task_menu += f'{index+1}) {item}\n'
    while task.lower() not in options:
        task = input(task_menu)
    return (task)

switch_tty(7)
time.sleep(3)
task = select_task()

while True:
    i = input('subject: ')
    match task:
        case 'youtube':
            searchstring = 'ytdl://ytsearch100:\''+ i + '\''
            subprocess.run(['mpv', '--no-video', searchstring])
