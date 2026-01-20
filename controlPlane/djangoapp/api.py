from ninja import NinjaAPI
api = NinjaAPI()

@api.get("/")
def cek(request):
    return {"a": ""}
