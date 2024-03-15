from sqlalchemy import delete, insert, select
from sqlalchemy.exc import SQLAlchemyError

from todo_app.database import async_session_maker


class BaseDao:
    model = None

    @classmethod
    async def show_table(cls):
        """
        Отображает все данные в таблице
        """
        async with async_session_maker() as session:
            try:
                query = select(cls.model)
                result = await session.execute(query)
                return result.mappings().all()
            except (SQLAlchemyError, Exception) as e:
                if isinstance(e, SQLAlchemyError):
                    raise f"Database exc show database: {str(e)}"
                else:
                    raise f"Unknown exc: {str(e)}"

    @classmethod
    async def add_data(cls, **kwargs):
        async with async_session_maker() as session:
            #try:
            query = insert(cls.model).values(**kwargs)
            await session.execute(query)
            await session.commit()
            '''except Exception as e:
                if isinstance(e, SQLAlchemyError):
                    raise f"Database exc show database: {str(e)}"
                else:
                    raise f"Unknown exc: {str(e)}"
'''
    @classmethod
    async def delete(cls, **kwargs):
        try:
            async with async_session_maker() as session:
                query = delete(cls.model).filter_by(**kwargs)
                await session.execute(query)
                await session.commit()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                raise f"Database exc show database: {str(e)}"
            else:
                raise f"Unknown exc: {str(e)}"

    @classmethod
    async def update_date(cls, id_line: id, column, new_data):
        try:
            async with async_session_maker() as session:
                query = await session.get(cls.model, id_line)
                if hasattr(query, column):
                    setattr(query, column, new_data)
                    await session.commit()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                raise f"Database exc show database: {str(e)}"
            else:
                raise f"Unknown exc: {str(e)}"

    @classmethod
    async def found_one_or_none(cls, **kwargs):
        """
        В таблице ищет данные,по заданным параметрам из **kwargs
        """
        async with async_session_maker() as session:
            try:
                query = select(cls.model.__table__.columns).filter_by(**kwargs)
                result = await session.execute(query)
                return result.mappings().all()
            except (SQLAlchemyError, Exception) as e:
                if isinstance(e, SQLAlchemyError):
                    raise f"Database exc show database: {str(e)}"
                else:
                    raise f"Unknown exc: {str(e)}"
