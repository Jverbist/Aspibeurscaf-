from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
import secrets
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud, models

app = FastAPI()
security = HTTPBasic()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

models.Base.metadata.create_all(bind=engine)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, ADMIN_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, ADMIN_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/", response_class=HTMLResponse)
def read_stats(request: Request, db: Session = Depends(get_db)):
    drinks = crud.get_all_drinks(db)
    return templates.TemplateResponse("index.html", {"request": request, "drinks": drinks})

@app.get("/manage", response_class=HTMLResponse)
def manage_page(request: Request, db: Session = Depends(get_db), user: str = Depends(authenticate)):
    drinks = crud.get_all_drinks(db)
    return templates.TemplateResponse("manage.html", {"request": request, "drinks": drinks})

@app.post("/sell")
def sell_drink(drink_id: int = Form(...), db: Session = Depends(get_db), user: str = Depends(authenticate)):
    crud.record_sale(db, drink_id)
    return RedirectResponse(url="/manage", status_code=303)

@app.get("/history/{drink_id}")
def get_price_history(drink_id: int, db: Session = Depends(get_db)):
    history = db.query(models.PriceHistory).filter(models.PriceHistory.drink_id == drink_id).order_by(models.PriceHistory.timestamp).all()
    return JSONResponse(content={
        "timestamps": [h.timestamp.isoformat() for h in history],
        "prices": [h.price for h in history]
    })
