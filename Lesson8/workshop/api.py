import httpx

URL = "https://api.agify.io/?name=Marek"
response = httpx.get(URL)
data = response.json()
print(data)
print(data["age"])