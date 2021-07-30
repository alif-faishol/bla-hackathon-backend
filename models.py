from database import Base
from sqlalchemy import Column, Unicode, ForeignKey, Table, Integer, Date
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy_utils import UUIDType

class User(Base):
    __tablename__ = 'user'
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    name = Column(Unicode, nullable=False)
    email = Column(Unicode, unique=True, nullable=False)
    password = Column(Unicode, nullable=False)
    usahas = relationship('Usaha', backref='user')
    phone = Column(Unicode)
    website = Column(Unicode)

class Usaha(Base):
    __tablename__ = 'usaha'
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    user_id = Column(UUIDType, ForeignKey('user.id'), nullable=False)
    products = relationship('Product', backref='usaha')
    alamat = Column(Unicode)
    name = Column(Unicode)
    description = Column(Unicode)

class Product(Base):
    __tablename__ = 'product'
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    name = Column(Unicode, nullable=False)
    description = Column(Unicode)
    usaha_id = Column(UUIDType, ForeignKey('usaha.id'), nullable=False)
    ulasans = relationship('Ulasan', backref='product')
    orders = relationship('Order', backref='product')
    daily_production = Column(Integer)
    price = Column(Integer, nullable=False)

class Order(Base):
    __tablename__ = 'order'
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    product_id = Column(UUIDType, ForeignKey('product.id'), nullable=False)
    tanggal = Column(Date, nullable=False)
    user_id = Column(UUIDType, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='orders')


class Ulasan(Base):
    __tablename__ = 'ulasan'
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    user_id = Column(UUIDType, ForeignKey('user.id'), nullable=False)
    user = relationship('User', backref='ulasans')
    product_id = Column(UUIDType, ForeignKey('product.id'), nullable=False)
    comment = Column(Unicode)
    rating = Column(Integer, nullable=False)

class ProposalModal(Base):
    __tablename__ = 'proposal_modal'
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    user_id = Column(UUIDType, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    title = Column(Unicode, nullable=False)
    content = Column(Unicode, nullable=False)


# DirectSuppliers = Table(
#     'direct_suppliers',
#     Base.metadata,
#     Column('left_id', UUIDType, ForeignKey('company.id')),
#     Column('right_id', UUIDType, ForeignKey('company.id'))
# )
# 
# DistributionChannels = Table(
#     'distribution_channels',
#     Base.metadata,
#     Column('left_id', UUIDType, ForeignKey('company.id')),
#     Column('right_id', UUIDType, ForeignKey('company.id'))
# )
# 
# ImportExport = Table(
#     'import_export',
#     Base.metadata,
#     Column('origin_company', UUIDType, ForeignKey('company.id')),
#     Column('destination_company', UUIDType, ForeignKey('company.id')),
#     Column('description', UUIDType)
# )
# 
# class Company(Base):
#     __tablename__ = 'company'
#     id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
#     name = Column(Unicode, nullable=False)
#     sector_id = Column(UUIDType, ForeignKey('sector.id'))
#     category_id = Column(UUIDType, ForeignKey('category.id'))
#     nation = Column(Unicode)
#     description = Column(Unicode)
#     product = Column(Unicode)
#     direct_suppliers = relationship(
#         'Company',
#         secondary=DirectSuppliers,
#         primaryjoin=DirectSuppliers.c.left_id==id,
#         secondaryjoin=DirectSuppliers.c.right_id==id)
# 
#     distribution_channels = relationship(
#         'Company',
#         secondary=DistributionChannels,
#         primaryjoin=DistributionChannels.c.left_id==id,
#         secondaryjoin=DistributionChannels.c.right_id==id)
# 
#     import_list = relationship(
#         'Company',
#         secondary=ImportExport,
#         primaryjoin=ImportExport.c.origin_company==id,
#         secondaryjoin=ImportExport.c.destination_company==id,
#         backref='export_list')
# 
# class Industry(Base):
#     __tablename__ = 'industry'
#     id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
#     name = Column(Unicode)
#     sectors = relationship('Sector', backref='industry')
# 
# class Sector(Base):
#     __tablename__ = 'sector'
#     id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
#     name = Column(Unicode)
#     industry_id = Column(UUIDType, ForeignKey('industry.id'))
#     companies = relationship('Company', backref="sector")
# 
# class Category(Base):
#     __tablename__ = 'category'
#     id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
#     name = Column(Unicode)
#     companies = relationship('Company', backref="category")

Base.metadata.create_all()
