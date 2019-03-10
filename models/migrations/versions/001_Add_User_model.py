from sqlalchemy import MetaData, Table, Column, String, Boolean, DateTime, ForeignKey, Integer
from migrate import *


meta = MetaData()

user = Table(
    "users", meta,
    Column("id", String(15), primary_key=True, index=True),
    Column("screen_name", String(20)),
    Column("password", String(150)),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
    Column("is_admin", Boolean),
    Column("delete_flag", Boolean)
)


post = Table(
    "posts", meta,
    Column("id", String(26), primary_key=True, index=True),
    Column("userid", String(15), ForeignKey("users.id"), index=True),
    Column("body", String(500)),
    Column("posted_at", DateTime, index=True),
    Column("delete_flag", Boolean)
)


relationship = Table(
    "relationship", meta,
    Column("id", Integer, primary_key=True),
    Column("user_id", String(15), ForeignKey("users.id"), index=True),
    Column("target", String(15), ForeignKey("users.id"), index=True),
    Column("relationship", Integer)
)

def upgrade(migrate_engine):
    meta.create_all(migrate_engine)

def downgrade(migrate_engine):
    meta.drop_all(migrate_engine)