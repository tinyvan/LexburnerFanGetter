import json,requests
def get():
    return json.loads(requests.get("https://api.bilibili.com/x/relation/stat?vmid=777536").text)["data"]["follower"]
