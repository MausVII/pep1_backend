from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Float, Boolean

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    category: Mapped[str] = mapped_column(String(30))
    price: Mapped[float] = mapped_column(Float())
    image: Mapped[str] = mapped_column(String(50))
    other_colors: Mapped[bool] = mapped_column(Boolean)
    short_description: Mapped[str] = mapped_column(String(200))
    designer: Mapped[str] = mapped_column(String(100))
    depth: Mapped[float] = mapped_column(Float())
    height: Mapped[float] = mapped_column(Float())
    width: Mapped[float] = mapped_column(Float())


    def __repr__(self) -> str:
        return F"Product: {self.id}-{self.name}"
    
    def as_dict(self):
        return {p.name: getattr(self, p.name) for p in self.__table__.columns}