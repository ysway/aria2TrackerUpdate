from sys import argv
import os
import requests

def getTrackerList(updateUrl):
    # get the tracker list
    r = requests.get(updateUrl)
    # check status code
    if r.status_code == 200:
        # get the tracker list
        trackerList = r.text.replace('\n\n', ',')
        # remove the last ','
        trackerList = trackerList[:-1]
        return trackerList
    else:
        return 'error'

def atu(filePath, trackerList, fileData):
    # check if folder exists
    os.makedirs(os.path.dirname(filePath), exist_ok=True)
    # check if the file exists
    if os.path.exists(filePath):
        # read the file
        with open(filePath, 'r') as f:
            fileData = f.read()
            # save the reading result into fileData
            f.close()
        content = fileData.split('\n')
        for line in content:
            if line.startswith('bt-tracker='):
                fileData = fileData.replace(line, '')
            else:
                pass
        fileData = fileData + '\n' + 'bt-tracker=' + trackerList + '\n'
        while '\n\n\n' in fileData:
            fileData = fileData.replace('\n\n\n', '\n\n')
        # write the file
        with open(filePath, 'w') as f:
            f.write(fileData)
            f.close()
    else:
        # create the file
        with open(filePath, 'w') as f:
            f.write(fileData + trackerList + '\n')
            f.close()
    
    # if aria2.session file not exists
    if not os.path.exists(f'{filePath[:filePath.rfind("/")]}/aria2.session'):
        # create a empty file
        with open(f'{filePath[:filePath.rfind("/")]}/aria2.session', 'w') as f:
            f.close()

def main(argument):
    global filePath, fileData
    try:
        # get the file path
        filePath = argument[0]
    except:
        # print the usage
        print('Usage: python3 aria2TrackerUpdate.py <filePath> <updateUrl> or python3 aria2TrackerUpdate.py <filePath>')
        return
    try:
        # get the update url
        updateUrl = argument[1]
    except:
        updateUrl = '''https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt'''
    # get the tracker list
    trackerList = getTrackerList(updateUrl)
    # check if the tracker list is error
    if trackerList == 'error':
        print('The trackers list url is not valid')
        return
    else:
        if ':' not in filePath and not \
                      filePath.startswith('/') and not \
                      filePath.startswith('./') and not \
                      filePath.startswith('.\\') and not \
                      filePath.startswith('../') and not \
                      filePath.startswith('..\\') and not \
                      filePath.startswith('~'):
            filePath = f'{os.getcwd()}/{filePath}'
        filePath = os.path.abspath(filePath).replace('\\', '/')
        fileData = fileData.format(filePath[:filePath.rfind('/')], filePath[:filePath.rfind('/')], filePath[:filePath.rfind('/')])
        # update the aria2.session file
        atu(filePath, trackerList, fileData)

# will be modified in main()
filePath = ''

fileData = '''
dir={}
disk-cache=128M
daemon=true

rpc-secret=1234567890
rpc-allow-origin-all=true
enable-rpc=true
rpc-listen-all=true
#file-allocation=none

continue=true
input-file={}/aria2.session
save-session={}/aria2.session
save-session-interval=120

max-overall-download-limit=0
max-download-limit=0
max-overall-upload-limit=0
max-upload-limit=0
enable-color=true

user-agent=Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25

http-accept-gzip=true

max-resume-failure-tries=8
max-tries=8
retry-wait=5
max-concurrent-downloads=10
max-connection-per-server=16
min-split-size=10M
split=32

check-certificate=false
disable-ipv6=false

peer-id-prefix=-TR2770-
user-agent=Transmission/2.77
seed-ratio=0

remote-time=true
reuse-uri=true
bt-enable-lpd=true
bt-max-peers=0
bt-request-peer-speed-limit=50M
bt-detach-seed-only=true
bt-tracker-interval=120
enable-dht=true
enable-dht6=true
enable-peer-exchange=true
listen-port=6881-6999
dht-listen-port=6881-6999

bt-tracker='''

if __name__ == '__main__':
    main(argv[1:])
