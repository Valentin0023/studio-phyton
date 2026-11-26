import jwt 
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()
CHIAVE_SEGRETA = "CHIAVE-123"

# 1. BIGLIETTERIA: controlli password dal token
@app.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "1234":
        braccialetto = jwt.encode({"utente": username}, CHIAVE_SEGRETA, algorithm="HS256")
        return {"token": braccialetto}
    raise HTTPException(status_code=401, detail="Password sbagliata!")

# 2. INGRESSO VIP: entri solo se mostri il braccialetto valido
@app.get("/area-vip")
def area_vip(token: str = Header()):
    try:
        dati = jwt.decode(token, CHIAVE_SEGRETA, algorithms=["HS256"])
        return {"messaggio": f"Benvenuto {dati['utente']} nell'area VIP!"}
    except:
        raise HTTPException(status_code=401, detail="Braccialetto falso o mancante!")