import requests, time, os

url = input('Enter the URL you would like to ping (remember to put https:// at the start): ')
delay = input('Enter the delay between pings (seconds): ')

if url == url :  # stops the code from running before user input is typed
    if delay == delay :  # same as above
        while True :  # forever
            r = requests.get(url)  # request the page
            f = open("temp.txt", "w+")  # open temp.txt
            f.write(r.text)  # write in what it got from the page (r.text)
            print(f'Pinged {url} with status code {r.status_code}.')  # displays a simple message 
            time.sleep(int(delay))  # waits (delay) seconds then repeats

            # you will have to delete temp.txt manually
