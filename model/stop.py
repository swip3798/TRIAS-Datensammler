from sqlalchemy import Column, Integer, String, Text, DateTime
from .base import Base

import datetime

class Stop(Base):
    __tablename__ = 'stops'
    stop_id = Column(Integer, primary_key = True, index = True, autoincrement = True)
    stop_point_ref = Column(String(24), index = True)
    stop_point_name = Column(Text)
    timetabled_time = Column(DateTime)
    real_time = Column(DateTime, index = True)
    stop_seq_number = Column(Integer)
    operating_day_ref = Column(String(12))
    journey_ref = Column(String(30), index = True)
    line_ref = Column(String(24), index = True)
    direction_ref = Column(String(10))
    pt_mode = Column(Text)
    submode = Column(Text)
    published_line_name = Column(Text)
    operator_ref = Column(String(16))
    route_description = Column(Text)
    origin_stop_point_ref = Column(String(24))
    destination_text = Column(Text)
    