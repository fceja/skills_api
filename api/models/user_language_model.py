from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user_language_model = Table(
    "user_language",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("language_id", Integer, ForeignKey("languages.id")),
)
