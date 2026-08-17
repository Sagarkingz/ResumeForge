import json
from typing import List, Optional
from database.database import get_connection, init_db
from models.resume_model import ResumeData

class StorageService:
    def __init__(self):
        init_db()

    def save_resume(self, resume: ResumeData) -> int:
        json_data = resume.to_json()
        with get_connection() as conn:
            cursor = conn.cursor()
            if resume.id is not None:
                cursor.execute(
                    "UPDATE resumes SET title = ?, data_json = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
                    (resume.title, json_data, resume.id)
                )
                resume_id = resume.id
            else:
                cursor.execute(
                    "INSERT INTO resumes (title, data_json) VALUES (?, ?)",
                    (resume.title, json_data)
                )
                resume_id = cursor.lastrowid
                resume.id = resume_id
            conn.commit()
            return resume_id

    def get_resume(self, resume_id: int) -> Optional[ResumeData]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT data_json FROM resumes WHERE id = ?", (resume_id,))
            row = cursor.fetchone()
            if row:
                data = json.loads(row["data_json"])
                data["id"] = resume_id
                return ResumeData.from_dict(data)
        return None

    def list_resumes(self) -> List[dict]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, updated_at FROM resumes ORDER BY updated_at DESC")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]