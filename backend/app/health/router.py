import logging

from sqlalchemy import text

from fastapi import APIRouter, Depends, HTTPException

from app.db import DBDep
from sqlalchemy.exc import SQLAlchemyError

logger = logging.getLogger(__name__)
router = APIRouter(tags=["Health"])

@router.get("/health")
def health_check(db: DBDep):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except SQLAlchemyError as e:
        logger.exception("Database health check failed")
        raise HTTPException(status_code=503, detail="Database unavailable") from e
