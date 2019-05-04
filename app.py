import requests, json, time

dynmap = "https://portal.retrominecraft.com/dynmap/standalone/dynmap_retromc.json"
url = "https://node.johnymuffin.com"
serverName = "test"
serverKey = "test"

def ping(dynmap, url, serverName, serverKey):
    import requests, json, time
    content = requests.get(dynmap)
    json = json.loads(content.content)

    playerCount = str(len(json['players']))
    worldTime = str(json['servertime'])
    unixTime = str(int(time.time()))

    post = url + "/listner/" + serverName + "/" + serverKey + "/" + playerCount + "/" + worldTime + "/" + unixTime

    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2'
    headers = {'User-Agent': user_agent}

    requests.get(post,headers=headers)
    print("Pinging")

while True:
    ping(dynmap, url, serverName, serverKey)
    time.sleep(60)