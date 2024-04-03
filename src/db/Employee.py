from sqlalchemy import String, ForeignKey, create_engine, MetaData, Column, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declarative_base, relationship

meta = MetaData()
db_url = "sqlite:///database.db"
engine = create_engine(db_url, echo= True)
Session = sessionmaker(engine)
session = Session()
connection = engine.connect()

class Base(DeclarativeBase):
    pass

class LeaveRecord(Base):
    __tablename__ = "LeaveRecord"
    leave_id = Column(Integer, primary_key=True)
    type = Column(String)
    status = Column(Integer)
    from_date = Column(DateTime)
    till_date = Column(DateTime)
    emp_email  = Column(ForeignKey('Employees.email_address'))

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
    emp_email = Column(ForeignKey('Employees.email_address'))


class Credentials(Base):
    __tablename__ = "Credentials"
    id = Column(Integer, primary_key=True)
    email_id = Column(String)
    password = Column(String)
    emp_email = Column(ForeignKey('Employees.email_address'))

class Employees(Base):
    __tablename__ = "Employees"
    first_name = Column(String)
    last_name = Column(String)
    position = Column(String)
    email_address = Column(String, primary_key=True)
    leave_status = relationship(LeaveRecord)
    address = relationship(Address)
    credential = relationship(Credentials)

    def __repr__(self) -> str:
        return f"<Employee(id={self.email_address}, firstname={self.first_name}, lastname = {self.last_name})>"


Base.metadata.create_all(engine)