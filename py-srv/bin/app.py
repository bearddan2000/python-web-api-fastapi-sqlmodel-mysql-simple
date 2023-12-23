from fastapi import Depends, FastAPI
import uvicorn

from sqlmodel import create_engine, Session, select

import settings
from model import Dog

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine(
    '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **settings.MYSQL
    )
)
app = FastAPI()

@app.get('/dog')
def get_all():
    with Session(engine) as session:
        statement = select(Dog)
        dogs = session.exec(statement).all()
    results = [
        {
            "id": dog.id,
            "breed": dog.breed,
            "color": dog.color
        } for dog in dogs]

    return {"results": results}

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0')