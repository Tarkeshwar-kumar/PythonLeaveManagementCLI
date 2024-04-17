from sqlalchemy import String, ForeignKey, create_engine, MetaData, Column, Integer, Date
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declarative_base, relationship

meta = MetaData()
db_url = "sqlite:///database.db"
engine = create_engine(db_url, echo= True, query_cache_size=0)
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
    from_date = Column(Date)
    till_date = Column(Date)
    emp_email  = Column(ForeignKey('Employees.email_address'))

    def __repr__(self) -> str:
        return f"<Leaves(type={self.type}, applied={self.status}, total={self.from_date})>"

class LeaveStats(Base):
    __tablename__ = "LeaveStats"
    leave_stat_id = Column(Integer, primary_key=True)
    type = Column(String)
    total = Column(Integer)
    availed = Column(Integer)
    emp_email  = Column(ForeignKey('Employees.email_address'))

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
    manager_email = Column(ForeignKey('Manager.email_address'))
    leave_recore = relationship(LeaveRecord)
    address = relationship(Address)
    credential = relationship(Credentials)
    leave_status = relationship(LeaveStats)

    def __repr__(self) -> str:
        return f"<Employee(id={self.email_address}, firstname={self.first_name}, lastname = {self.last_name})>"

class Manager(Base):
    __tablename__ = "Manager"
    first_name = Column(String)
    last_name = Column(String)
    email_address = Column(String, primary_key=True)
    emp_id = relationship(Employees)

Base.metadata.create_all(engine)