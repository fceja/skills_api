from sqlalchemy import Column, Integer, Table, ForeignKey, UniqueConstraint

from app.models.base import Base

# associative table
user_language = Table(
    "user_languages",
    Base.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("language_id", Integer, ForeignKey("languages.id")),
    UniqueConstraint("user_id", "language_id"),
)
