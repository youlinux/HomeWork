# coding: utf-8

# 导入
import random
from faker import Factory

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship

# 创建对象基类
Base = declarative_base()

# 初始化数据库连接
engine = create_engine('mysql+mysqldb://root@localhost:3306/blog?charset=utf8')

"""
    create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
    '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
"""

# 定义user表
class User(Base):

    # 表的名字
    __tablename__ = 'users'

    # 表的结构,字段
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)

    # 一对多 一个作者,可以有多个文章 backref 表示双向关系
    articles = relationship('Article', backref='author')

    # userlist 表示 一对一
    userinfo = relationship('UserInfo', backref='user', uselist=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)


class UserInfo(Base):

    __tablename__ = 'userinfos'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    qq = Column(String(11))
    phone = Column(String(11))
    link = Column(String(64))


    user_id = Column(Integer, ForeignKey('users.id'))



class Article(Base):

    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    cate_id = Column(Integer, ForeignKey('categories.id'))
    
    # 文章和标签 多<-->多 多对多 需要一个中间表 secondary 指定中间表
    tags = relationship('Tag', secondary='article_tag', backref='articles')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)


class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref='category')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)

# 中间表
article_tag = Table(
    # 表名 + Base.metadata
    'article_tag', Base.metadata,

    # 有两个字段
    Column('article_id', Integer, ForeignKey('articles.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


class Tag(Base):

    __tablename__ = 'tags'

    # 主键
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    # faker 伪造数据
    # 类的实例化
    faker = Factory.create()

    # 创建Session 类型
    Session = sessionmaker(bind=engine)

    # 创建 session 对象
    session = Session()


    faker_users = [User(
        username=faker.name(),
        password=faker.word(),
        email=faker.email(),
    ) for i in range(10)]

    # sqlalchemy  create
    session.add_all(faker_users)

    faker_categories = [Category(name=faker.word()) for i in range(5)]
    session.add_all(faker_categories)

    faker_tags= [Tag(name=faker.word()) for i in range(20)]
    session.add_all(faker_tags)

    for i in range(100):
        article = Article(
            title=faker.sentence(),
            content=' '.join(faker.sentences(nb=random.randint(10, 20))),
            author=random.choice(faker_users),
            category=random.choice(faker_categories)
        )
        for tag in random.sample(faker_tags, random.randint(2, 5)):
            # tags Article 的一个字段
            article.tags.append(tag)
        session.add(article)

    session.commit()

