from fastapi import APIRouter, UploadFile
import shutil

router = APIRouter(
    prefix = "/images",
    tags = ["Images"]
)

@router.post("/hotels")
async def upload_hotel_image(name: int, file: UploadFile):
    with open(f"app/static/images/{name}.webp", "wb+") as file_obj:
        shutil.copyfileobj(file.file, file_obj)