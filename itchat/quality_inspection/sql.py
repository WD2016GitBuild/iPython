from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义Channel对象:
class Channel(Base):

    # 表名
    __tablename__ = 'quality_inspection_records'

    # 表结构
    id = Column(String(20),primary_key=True)
    title = Column(String(45))
    order_id = Column(String(80))
    make_id = Column(String(45))
    url=  Column(String(45))
    point = Column(String(45))

    def __init__(self,id,title,order_id,make_id,url,point):
        self.id = id
        self.title = title
        self.order_id = order_id
        self.make_id = make_id
        self.url = url
        self.point = point

# 初始化数据库连接,:
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/wd')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()

# 增操作
item1 = Channel(id='1',title='catv1',order_id='http://10.10.10.188/catv1',make_id='news',url='abc', point='450')
session.add(item1)


session.commit()
session.close()
