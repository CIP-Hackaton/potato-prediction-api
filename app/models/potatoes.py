from sqlalchemy import Column, String, JSON, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base

class Potatoes(Base):
    __tablename__ = 'potatoes'
    
    id = Column(UUID, primary_key=True)
    name = Column(String)
    description = Column(String)
    url_photo = Column(String)
    characteristics = Column(JSON)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))