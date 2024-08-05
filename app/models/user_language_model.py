from sqlalchemy import Column, Integer, Table, ForeignKey

from app.models.base import Base

# associative table
user_language = Table(
    "user_language",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("language_id", Integer, ForeignKey("languages.id")),
)
