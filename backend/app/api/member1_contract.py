"""Compatibility endpoints for the Member 1 -> Member 2 API contract."""

from __future__ import annotations

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from app.api.video import process_session_video
from app.db.session import get_db

router = APIRouter(tags=["Member 1 API Contract"])


@router.post("/timeline", summary="Queue timeline processing for a lecture session")
def timeline_contract(
    session_id: UUID,
    background_tasks: BackgroundTasks,
    db: Annotated[Session, Depends(get_db)],
):
    return process_session_video(session_id=session_id, background_tasks=background_tasks, db=db)
