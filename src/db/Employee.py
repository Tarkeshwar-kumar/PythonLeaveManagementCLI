from sqlalchemy import String, ForeignKey, create_engine, MetaData, Column, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declarative_base, relationship

meta = MetaData()
db_url = "sqlite:///database.db"
engine = create_engine(db_url, echo= True)
Session = sessionmaker(engine)
session = Session()
connection = engine.connect()

class Base(DeclarativeBase):
    pass

class LeaveStats(Base):
    __tablename__ = "LeaveStats"
    status_id = Column(Integer, primary_key=True)
    type = Column(String)
    applied = Column(Integer)
    total = Column(Integer)
    emp_id  = Column(ForeignKey('Employees.id'))

    def __repr__(self) -> str:
        return f"<Leaves(type={self.type}, applied={self.applied}, total={self.total})>"


class Address(Base):
    __tablename__ = "Address"
    address_id = Column(Integer, primary_key = True)
    flat_number = Column(Integer)
    sector= Column(Integer)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    emp_id = Column(ForeignKey('Employees.id'))


class Credentials(Base):
    __tablename__ = "Credentials"
    id = Column(Integer, primary_key=True)
    email_id = Column(String)
    password = Column(String)
    emp_id = Column(ForeignKey('Employees.id'))

class Employees(Base):
    __tablename__ = "Employees"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    position = Column(String)
    email_address = Column(String)
    leave_status = relationship(LeaveStats)
    address = relationship(Address)
    credential = relationship(Credentials)

    def __repr__(self) -> str:
        return f"<Employee(id={self.id}, firstname={self.first_name}, lastname = {self.last_name})>"


Base.metadata.create_all(engine)