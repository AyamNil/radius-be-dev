from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class RadCheck(Base):
    __tablename__ = 'radcheck'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    attribute = Column(String)
    op = Column(String)
    value = Column(String)


class RadUserGroup(Base):
    __tablename__ = 'radusergroup'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    groupname = Column(String)
    priority = Column(Integer)


class RadAcct(Base):
    __tablename__ = 'radacct'
    radacctid = Column(Integer, primary_key=True)
    username = Column(String)
    acctstarttime = Column(TIMESTAMP)
    acctstoptime = Column(TIMESTAMP)
    acctinputoctets = Column(Integer)
    acctoutputoctets = Column(Integer)


class AuditLog(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True)
    admin_username = Column(String)
    action = Column(String)
    target = Column(String)
    details = Column(String)
    ip_address = Column(String)
    created_at = Column(TIMESTAMP)