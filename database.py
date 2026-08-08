from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# -------SQLITE3-------
SQLAlCHEMY_DATABASE_URL = "postgresql://postgres.askbgzwdlummdtetsews:AbbuAmmu0123@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres"
engine = create_engine(SQLAlCHEMY_DATABASE_URL)

# -------POSTGRESQL-------
# SQLAlCHEMY_DATABASE_URL = (
#     "postgresql://postgres:password@localhost/TodoApplicationDatabase"
# )
# engine = create_engine(SQLAlCHEMY_DATABASE_URL)

# -------MYSQL-------
# SQLAlCHEMY_DATABASE_URL = (
#     "mysql+pymysql://root:password@127.0.0.1:3306/todoapplicationdatabase"
# )
# engine = create_engine(SQLAlCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
