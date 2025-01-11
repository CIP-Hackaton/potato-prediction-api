from sqlalchemy import Column, JSON, ForeignKey, TIMESTAMP, text, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.db.session import Base


class Predictions(Base):
    __tablename__ = 'predictions'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    campesino_response = Column(JSON)
    p_characteristics = Column(JSON)
    details = Column(JSON)
    owner = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    allowed_user = Column(ARRAY(UUID))  
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    
    user = relationship("User", back_populates="predictions")
