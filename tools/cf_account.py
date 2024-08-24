import httpx

def main(auth_bearer: str) -> dict:
    url = "https://api.cloudflare.com/client/v4/accounts"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_bearer}"
    }
    with httpx.Client() as client:
        response = client.get(url, headers=headers)
    
    data = response.json()
    result = []
    
    if data["success"] and "result" in data:
        for account in data["result"]:
            result.append({
                "id": account["id"],
                "name": account["name"]
            })
    
    return {"result": result}

if __name__ == "__main__":
    auth_bearer = "xxxxxxxxxxxx-iPt"
    output = main(auth_bearer)
    print(output)