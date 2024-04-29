from pytest import fixture
from lms.model.model import Credentials, Base, Employees, LeaveRecord, Manager, LeaveStats, Address
from sqlalchemy import String, ForeignKey, create_engine, MetaData, Column, Integer, Date
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declarative_base, relationship

@fixture
def db_session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)


def test_employees(db_session):
    employee = Employees(
        first_name='John',
        last_name='Doe',
        position='Developer',
        email_address='john.doe@example.com'
    )
    db_session.add(employee)
    db_session.commit()

    retrieved_employee = db_session.query(Employees).filter_by(email_address='john.doe@example.com').first()

    assert retrieved_employee is not None
    assert retrieved_employee.first_name == 'John'
    assert retrieved_employee.last_name == 'Doe'
    assert retrieved_employee.position == 'Developer'

def test_credentials(db_session):
    credentials = Credentials(email_id='test@example.com', password='password123')

    db_session.add(credentials)
    db_session.commit()

    retrieved_credentials = db_session.query(Credentials).filter_by(email_id='test@example.com').first()

    assert retrieved_credentials is not None
    assert retrieved_credentials.email_id == 'test@example.com'
    assert retrieved_credentials.password == 'password123'

def test_leave_record(db_session):
    leave_record = LeaveRecord(type='Sick Leave', status=1, from_date='2024-04-28', till_date='2024-04-30')

    db_session.add(leave_record)
    db_session.commit()

    retrieved_leave_record = db_session.query(LeaveRecord).filter_by(type='Sick Leave').first()

    assert retrieved_leave_record is not None
    assert retrieved_leave_record.type == 'Sick Leave'
    assert retrieved_leave_record.status == 1
    assert str(retrieved_leave_record.from_date) == '2024-04-28'
    assert str(retrieved_leave_record.till_date) == '2024-04-30'

def test_leave_stats(db_session):
    leave_stats = LeaveStats(type='Annual', total=20, availed=5)

    db_session.add(leave_stats)
    db_session.commit()

    retrieved_leave_stats = db_session.query(LeaveStats).filter_by(type='Annual').first()

    assert retrieved_leave_stats is not None
    assert retrieved_leave_stats.type == 'Annual'
    assert retrieved_leave_stats.total == 20
    assert retrieved_leave_stats.availed == 5

def test_address(db_session):
    address = Address(
        flat_number=123,
        sector=7,
        city='New York',
        state='NY',
        country='USA'
    )

    db_session.add(address)
    db_session.commit()

    retrieved_address = db_session.query(Address).filter_by(city='New York').first()

    assert retrieved_address is not None
    assert retrieved_address.flat_number == 123
    assert retrieved_address.sector == 7
    assert retrieved_address.city == 'New York'
    assert retrieved_address.state == 'NY'
    assert retrieved_address.country == 'USA'

def test_manager(db_session):
    manager = Manager(
        first_name='Alice',
        last_name='Smith',
        email_address='alice.smith@example.com'
    )

    db_session.add(manager)
    db_session.commit()

    retrieved_manager = db_session.query(Manager).filter_by(email_address='alice.smith@example.com').first()

    assert retrieved_manager is not None
    assert retrieved_manager.first_name == 'Alice'
    assert retrieved_manager.last_name == 'Smith'
    assert retrieved_manager.email_address == 'alice.smith@example.com'