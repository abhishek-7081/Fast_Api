from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_methods=["GET"],
    allow_headers=[],
)

# Pydantic Model
class Tea(BaseModel):
    id: int
    name: str
    origin: str


# In-memory database

      
teas: List[Tea] = [
    Tea(id=1, name="Green Tea", origin="China"),
    Tea(id=2, name="Black Tea", origin="India"),
    Tea(id=3, name="Oolong Tea", origin="Taiwan"),
    Tea(id=4, name="White Tea", origin="China"),
    Tea(id=5, name="Herbal Tea", origin="Various"),
    Tea(id=6, name="Matcha", origin="Japan"),
    Tea(id=7, name="Chai", origin="India"),
    Tea(id=8, name="Earl Grey", origin="England"),
    Tea(id=9, name="Darjeeling Tea", origin="India"),
    Tea(id=10, name="Assam Tea", origin="India"),
    Tea(id=11, name="Sencha", origin="Japan"),
    Tea(id=12, name="Gyokuro", origin="Japan"),
    Tea(id=13, name="Jasmine Tea", origin="China"),
    Tea(id=14, name="Pu-erh Tea", origin="China"),
    Tea(id=15, name="Yellow Tea", origin="China"),
    Tea(id=16, name="Tieguanyin", origin="China"),
    Tea(id=17, name="Da Hong Pao", origin="China"),
    Tea(id=18, name="Genmaicha", origin="Japan"),
    Tea(id=19, name="Hojicha", origin="Japan"),
    Tea(id=20, name="Kukicha", origin="Japan"),
    Tea(id=21, name="Lapsang Souchong", origin="China"),
    Tea(id=22, name="English Breakfast", origin="England"),
    Tea(id=23, name="Irish Breakfast", origin="Ireland"),
    Tea(id=24, name="Ceylon Tea", origin="Sri Lanka"),
    Tea(id=25, name="Nilgiri Tea", origin="India"),
    Tea(id=26, name="Kangra Tea", origin="India"),
    Tea(id=27, name="Kashmiri Kahwa", origin="India"),
    Tea(id=28, name="Masala Chai", origin="India"),
    Tea(id=29, name="Butter Tea", origin="Tibet"),
    Tea(id=30, name="Thai Iced Tea", origin="Thailand"),
    Tea(id=31, name="Vietnamese Lotus Tea", origin="Vietnam"),
    Tea(id=32, name="Moroccan Mint Tea", origin="Morocco"),
    Tea(id=33, name="Turkish Tea", origin="Turkey"),
    Tea(id=34, name="Rooibos Tea", origin="South Africa"),
    Tea(id=35, name="Honeybush Tea", origin="South Africa"),
    Tea(id=36, name="Yerba Mate", origin="Argentina"),
    Tea(id=37, name="Mate Cocido", origin="Argentina"),
    Tea(id=38, name="Chamomile Tea", origin="Egypt"),
    Tea(id=39, name="Peppermint Tea", origin="Various"),
    Tea(id=40, name="Spearmint Tea", origin="Various"),
    Tea(id=41, name="Hibiscus Tea", origin="Africa"),
    Tea(id=42, name="Lavender Tea", origin="France"),
    Tea(id=43, name="Lemon Balm Tea", origin="Europe"),
    Tea(id=44, name="Ginger Tea", origin="India"),
    Tea(id=45, name="Turmeric Tea", origin="India"),
    Tea(id=46, name="Lemongrass Tea", origin="Thailand"),
    Tea(id=47, name="Rose Tea", origin="Iran"),
    Tea(id=48, name="Butterfly Pea Tea", origin="Thailand"),
    Tea(id=49, name="Sage Tea", origin="Mediterranean"),
    Tea(id=50, name="Nettle Tea", origin="Europe"),
    Tea(id=51, name="Pine Needle Tea", origin="Korea"),
    Tea(id=52, name="Barley Tea", origin="Japan"),
    Tea(id=53, name="Corn Silk Tea", origin="Korea"),
    Tea(id=54, name="Buckwheat Tea", origin="Japan"),
    Tea(id=55, name="Mulberry Leaf Tea", origin="Korea"),
    Tea(id=56, name="Ginseng Tea", origin="Korea"),
    Tea(id=57, name="Osmanthus Tea", origin="China"),
    Tea(id=58, name="Chrysanthemum Tea", origin="China"),
    Tea(id=59, name="Goji Berry Tea", origin="China"),
    Tea(id=60, name="Longjing Tea", origin="China"),
    Tea(id=61, name="Biluochun Tea", origin="China"),
    Tea(id=62, name="Keemun Tea", origin="China"),
    Tea(id=63, name="Yunnan Black Tea", origin="China"),
    Tea(id=64, name="Dian Hong Tea", origin="China"),
    Tea(id=65, name="Bai Mudan", origin="China"),
    Tea(id=66, name="Silver Needle Tea", origin="China"),
    Tea(id=67, name="Shou Mei Tea", origin="China"),
    Tea(id=68, name="Milk Oolong", origin="Taiwan"),
    Tea(id=69, name="Oriental Beauty", origin="Taiwan"),
    Tea(id=70, name="Alishan Tea", origin="Taiwan"),
    Tea(id=71, name="Baozhong Tea", origin="Taiwan"),
    Tea(id=72, name="GABA Oolong", origin="Taiwan"),
    Tea(id=73, name="Kokeicha", origin="Japan"),
    Tea(id=74, name="Kabusecha", origin="Japan"),
    Tea(id=75, name="Bancha", origin="Japan"),
    Tea(id=76, name="Kukicha Green Tea", origin="Japan"),
    Tea(id=77, name="Shincha", origin="Japan"),
    Tea(id=78, name="Fukamushi Sencha", origin="Japan"),
    Tea(id=79, name="Kirishima Tea", origin="Japan"),
    Tea(id=80, name="Uji Matcha", origin="Japan"),
    Tea(id=81, name="Anji Bai Cha", origin="China"),
    Tea(id=82, name="Huangshan Maofeng", origin="China"),
    Tea(id=83, name="Taiping Houkui", origin="China"),
    Tea(id=84, name="Liu An Gua Pian", origin="China"),
    Tea(id=85, name="Mengding Ganlu", origin="China"),
    Tea(id=86, name="Rize Tea", origin="Turkey"),
    Tea(id=87, name="Karak Tea", origin="Pakistan"),
    Tea(id=88, name="Noon Chai", origin="Kashmir"),
    Tea(id=89, name="Sulaimani Tea", origin="India"),
    Tea(id=90, name="Irani Chai", origin="India"),
    Tea(id=91, name="Kashmiri Pink Tea", origin="India"),
    Tea(id=92, name="Tandoori Chai", origin="India"),
    Tea(id=93, name="Butterfly Ginger Tea", origin="Thailand"),
    Tea(id=94, name="Pandan Tea", origin="Southeast Asia"),
    Tea(id=95, name="Saffron Tea", origin="Iran"),
    Tea(id=96, name="Cinnamon Tea", origin="Sri Lanka"),
    Tea(id=97, name="Cardamom Tea", origin="India"),
    Tea(id=98, name="Vanilla Tea", origin="Various"),
    Tea(id=99, name="Apple Tea", origin="Turkey"),
    Tea(id=100, name="Peach Tea", origin="China")
]

# 1. Home Route
@app.get("/")
def home():
    return {"message": "Welcome to Tea API"}



# 2. GET - Fetch all teas
@app.get("/teas")
def get_teas():
    return teas


# 3. GET - Fetch tea by ID
@app.get("/teas/{tea_id}")
def get_tea(tea_id: int):
    for tea in teas:
        if tea.id == tea_id:
            return tea

    raise HTTPException(status_code=404, detail="Tea not found")


# 4. POST - Add a new tea
@app.post("/teas", status_code=201)
def add_tea(tea: Tea):
    for existing_tea in teas:
        if existing_tea.id == tea.id:
            raise HTTPException(status_code=400, detail="Tea ID already exists")

    teas.append(tea)
    return {"message": "Tea added successfully", "tea": tea}


# 5. PUT - Update entire tea
@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            if updated_tea.id != tea_id:
                raise HTTPException(status_code=400, detail="ID cannot be changed")

            teas[index] = updated_tea
            return {"message": "Tea updated successfully", "tea": updated_tea}

    raise HTTPException(status_code=404, detail="Tea not found")


# 6. PATCH - Partially update tea
class TeaUpdate(BaseModel):
    name: str = None
    origin: str = None


@app.patch("/teas/{tea_id}")
def partial_update_tea(tea_id: int, updates: TeaUpdate):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            updated_data = tea.model_dump()
            updated_data.update(updates.model_dump(exclude_unset=True))

            updated_tea = Tea(**updated_data)
            teas[index] = updated_tea

            return {"message": "Tea partially updated", "tea": updated_tea}

    raise HTTPException(status_code=404, detail="Tea not found")


# 7. DELETE - Delete tea
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted_tea = teas.pop(index)
            return {"message": "Tea deleted successfully", "tea": deleted_tea}

    raise HTTPException(status_code=404, detail="Tea not found")
