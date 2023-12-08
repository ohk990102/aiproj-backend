from fastapi import APIRouter, HTTPException

from models.db import Model, Scan, db_session

router = APIRouter(
    prefix='/scans',
    tags=['scans']
)

@router.get("/")
def get_scans():
    return {"status": "success", "result": Scan.query.all()}

@router.post("/new")
def new_scan(model_id: str):
    model = Model.query.filter_by(id=model_id).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")

    scan = Scan(model_id=model_id, status="pending")
    db_session.add(scan)
    db_session.commit()

    return {"status": "success", "result": {"id": scan.id}}