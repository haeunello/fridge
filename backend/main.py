from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from ocr_utils import extract_ingredients

app = FastAPI()

# CORS 설정 (모바일 앱 요청 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    ingredients = extract_ingredients(contents)

    # 간단한 요리 추천 예시
    recipes = [
        {"name": "계란 프라이", "ingredients": ["계란"]},
        {"name": "김치볶음밥", "ingredients": ["밥", "김치", "계란"]},
        {"name": "라면", "ingredients": ["라면"]}
    ]

    recommended = [
        r["name"] for r in recipes
        if all(ing in ingredients for ing in r["ingredients"])
    ]

    return {
        "ingredients": ingredients,
        "recommended": recommended
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

