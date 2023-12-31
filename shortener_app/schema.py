from lib2to3.pytree import Base
from pydantic import BaseModel

class URLBase(BaseModel):
    target_url : str

class URL(URLBase):
    is_active : bool
    clicks : int

    class Config:
        orm_mode = True  # to work with a database ORM model


class URLInfo(URL):
    url : str
    admin_url : str


