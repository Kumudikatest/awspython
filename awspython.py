import requests

def handler(event, context):
    try:
        res = requests.get(
            "https://paper-api.alpaca.markets/v2/calendar",
            params={"start":"1587549503","end":"1587344461"},
            headers={"Accept":"application/json"}
        )
        # your code goes here
    except BaseException as e:
        # error handling goes here
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
