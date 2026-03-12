from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


# TOOL 1 — Log Interaction
def log_interaction(name: str, email: str, company: str):

    query = text("""
        INSERT INTO leads (name, email, company)
        VALUES (:name, :email, :company)
    """)

    with engine.connect() as conn:
        conn.execute(query, {
            "name": name,
            "email": email,
            "company": company
        })
        conn.commit()

    return f"Interaction with {name} logged successfully."


# TOOL 2 — Get Interactions
def get_interactions():

    query = text("SELECT * FROM leads")

    with engine.connect() as conn:
        result = conn.execute(query)
        interactions = result.fetchall()

    return interactions


# TOOL 3 — Edit Interaction
def edit_interaction(id: int, name: str):

    query = text("""
        UPDATE leads
        SET name = :name
        WHERE id = :id
    """)

    with engine.connect() as conn:
        conn.execute(query, {
            "id": id,
            "name": name
        })
        conn.commit()

    return f"Interaction {id} updated."


# TOOL 4 — Summarize Interaction
def summarize_interaction(text):

    return f"Summary: {text[:50]}..."


# TOOL 5 — Suggest Followup
def suggest_followup():

    suggestions = [
        "Schedule follow-up meeting next week.",
        "Send product brochure to HCP.",
        "Provide clinical trial data.",
        "Arrange product demo session."
    ]

    return suggestions