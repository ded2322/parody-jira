from sqlalchemy import select, insert, delete, update
from sqlalchemy.exc import SQLAlchemyError

from core.logger import logger
from core.utils.repository import AbstractRepository
from core.database import async_session_maker


class SqlalchemyRepository(AbstractRepository):
    models = None

    @classmethod
    async def show_all_table(cls):
        async with async_session_maker() as session:
            try:
                query = select(cls.models.__table__.columns)
                result = await session.execute(query)
                return result.mappings().all()
            except (SQLAlchemyError, Exception) as e:
                if isinstance(e, SQLAlchemyError):
                    msg = f"Database exc show database: {str(e)}"
                else:
                    msg = f"Unknown exc: {str(e)}"

                logger.error(msg, exc_info=True)

    @classmethod
    async def found_one_or_none(cls, **kwargs):
        try:
            async with async_session_maker() as session:
                query = select(cls.models.__table__.columns).filter_by(**kwargs)
                result = await session.execute(query)
                return result.mappings().one_or_none()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = f"Database exc show database: {str(e)}"
            else:
                msg = f"Unknown exc: {str(e)}"
            logger.error(msg, exc_info=True)

    @classmethod
    async def insert_data(cls, **kwargs):
        try:
            async with async_session_maker() as session:
                query = insert(cls.models).values(**kwargs)
                await session.execute(query)
                await session.commit()
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = f"Database exc show database: {str(e)}"
            else:
                msg = f"Unknown exc: {str(e)}"
            logger.error(msg, exc_info=True)

    @classmethod
    async def update_data(cls, id_column: int, new_data):
        try:
            async with async_session_maker() as session:
                query = (update(cls.models).
                         where(cls.models.id == id_column).
                         values(new_data))

                await session.execute(query)
                await session.commit()
                return True
        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = f"Database exc show database: {str(e)}"
            else:
                msg = f"Unknown exc: {str(e)}"
            logger.error(msg, exc_info=True)

    @classmethod
    async def delete_data(cls, **kwargs):
        try:
            async with async_session_maker() as session:
                query = delete(cls.models).filter_by(**kwargs)
                result = await session.execute(query)
                await session.commit()
                deleted_rows = result.rowcount
                return True, deleted_rows

        except (SQLAlchemyError, Exception) as e:
            if isinstance(e, SQLAlchemyError):
                msg = f"Database exc show database: {str(e)}"
            else:
                msg = f"Unknown exc: {str(e)}"
            logger.error(msg, exc_info=True)
