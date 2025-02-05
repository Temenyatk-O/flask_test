from sqlalchemy.orm import DeclarativeBase,relationship,sessionmaker,selectinload
from sqlalchemy import Column,String,Integer,ForeignKey,create_engine,func


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__='users'

    id= Column(Integer,primary_key=True)
    name=Column(String(50))
    department_id=Column(Integer,ForeignKey("departments.id"))
    department=relationship("Department",back_populates="users")




    
class Department():
    __tablename__='departments'
    id= Column(Integer,primary_key=True)
    name=Column(String(50))
    users=relationship("User",back_populates="department")
# username="artem"
# password="password"
# host="localhost"
# port="5432"
# db_name="database_name"

# url=f"postgresql://{username}:{password}@{host}:{port}/{db_name}"
# engine=create_engine(url,echo=True)

engine=create_engine("sqlite:///memory:", echo=True)

Base.metadata.create_all(engine)
session=sessionmaker(bind=engine)
ses=session()


departement_it=Department(name="IT")
departement_hq=Department(name="HQ")


user_1=User(name="Artem",department=departement_hq)
user_2=User(name="Artem2",department=departement_hq)
user_3=User(name="Artem3",department=departement_it)
user_4=User(name="Artem4",department=departement_it)

ses.add_all([departement_it,departement_hq,user_1,user_2,user_3,user_4])

ses.commit()    

departments=ses.query(Department).all()
for i in departments:
    print(f"Department{i.name}")
    for user in i.users:
        print(f"User: {user.name}")

deps=ses.query(Department).options(selectinload(Department.users)).all()
for i in departments:
    print(f"Department{i.name}")
    for user in i.users:
        print(f"User: {user.name}")


user_count=(
    ses.query(Department.name,func.count(User.id))
    .outerjoin(User)
    .group_by(Department.id)
    .all()
)
for i in user_count:
    print(f"Dep{i[0]},Users {i[1]}")



