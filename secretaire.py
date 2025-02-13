import subprocess
import time

# Global variables
inputs= ['camera', 'keyboard', 'phone_dtmf', 'phone_mic', 'qr_scanner', 'scan', 'sd_card']
outputs= ['galvanometer', 'odometer', 'print_thermal', 'print_laser', 'radio_speaker', 'splitflap']
tasks = ['ai', 'calendar','call', 'contacts', 'email', 'news', 'notes', 'rss', 'radio', 'record', 'sms', 'stocks', 'transport', 'weather', 'wikipedia', 'youtube']

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
    task = ''
    task_menu = "Make your choice:\n"
    for index, item in enumerate(tasks):
        task_menu += f'{index+1}) {item}\n'
    while task not in tasks:
        task = input(task_menu)
    return (task)

def select_input():
    input  = ''
    input_menu = "Make your choice:\n"
    for index, item in enumerate(inputs):
        input_menu += f'{index+1}) {item}\n'
    while input not in inputs:
        input = input(input_menu)
    return (input)

def select_output():
    output  = ''
    output_menu = "Make your choice:\n"
    for index, item in enumerate(outputs):
        output_menu += f'{index+1}) {item}\n'
    while output not in options:
        output = input(output_menu)
    return (output)

switch_tty(7)
time.sleep(3)
while True:
    task = select_task()
    
    while True:
        i = input('subject: ')
        if (i == 'q'): break
        match task:
            case 'calendar':
                print('TODO implenent')
                '''
                '''

            case 'call':
                print('TODO implement')
                '''
                read name
                find first phone number for name
                pick up 1980 phone
                voip system calls retrieved phone number
                '''
            
            case 'contacts':
                print('TODO implement')
                '''
                '''

            case 'email':
                print('TODO implement')
                '''
                subswitch:
                    - print overview of new emails
                    - print individual email
                        - enter email id
                    - mark as read:
                        - enter email id
                    - mark as spam
                        - enter email id
                    - delete
                        - enter email id
                    - reply
                        - enter email id
                        - either
                            - write answer on paper by hand; scan
                            - write anwer on paper by typewriter; scan
                            - type blind on keyboard
                    - reply all
                        - enter email id
                    - forward
                        - enter email id
                '''

            case 'notes':
                print('TODO implement')
                '''
                - how to tag?
                - how to digitise?
                '''

            case 'rss':
                print('TODO implement')
                '''
                set rotary switch to feed
                print feed
                '''

            case 'radio':
                print('TODO implement')
                '''
                set subswitch to radio station or podcast
                how to set radio station or podcast?
                  - web interface outside?
                  - keyboard + search service?
                '''

            case 'record':
                print('TODO implement')
                '''
                - pick up phone
                - speak
                - put down phone horn
                - recording stops
                '''

            case 'sms':
                print('TODO implement')
                '''
                subswitch
                    - show sms (print? split flap?)
                    - write sms
                        - read name
                        - find first mobile phone number for name
                        - write sms
                            - keyboard?
                            - paper & scan?
                        - connect to own mobile phone via bluetooth
                        - send sms
                        - feedback
                            - print sent sms
                            - store in sms archive
                '''

            case 'stocks':
                print('TODO implement')
                '''
                subswitch
                    - print portfolio statement
                    - net worth (split flap, galvanometer?)
                    - individual stock 1: shortcode, price, evolution (split flap, galvanometer?)
                '''
            case 'wikipedia':
                print('TODO implement')
                '''
                - enter search string on keyboard
                - print first article matching search string
                '''
                searchstring = 'https://en.wikipedia.org/w/api.php?action=opensearch&search={i}&limit=1&namespace=0&format=json'

            case 'youtube':
                searchstring = 'ytdl://ytsearch100:\''+ i + '\''
                subprocess.run(['mpv', '--no-video', searchstring])
