from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession, async_sessionmaker


class DatabaseHelper:
    """
    Вспомогательный класс для управления подключением к базе данных.

    :param url: URL подключения к базе данных.
    :param echo: Если True, то SQLAlchemy будет логировать все выполняемые SQL запросы.
    :param echo_pool: Если True, то SQLAlchemy будет логировать все действия пула соединений.
    :param pool_size: Размер пула соединений.
    :param max_overflow: Максимальное количество дополнительных соединений сверх пула.
    """

    def __init__(
            self,
            url: str,
            echo: bool = False,
            echo_pool: bool = False,
            pool_size: int = 10,
            max_overflow: int = 10,
    ) -> None:
        """
        Инициализирует движок базы данных и сессию.

        :param url: URL подключения к базе данных.
        :param echo: Если True, то SQLAlchemy будет логировать все выполняемые SQL запросы.
        :param echo_pool: Если True, то SQLAlchemy будет логировать все действия пула соединений.
        :param pool_size: Размер пула соединений.
        :param max_overflow: Максимальное количество дополнительных соединений сверх пула.
        """
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        """
        Завершает соединение с базой данных, освобождая ресурсы.

        :return: None
        """
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        """Возвращает новую сессию для взаимодействия с базой данных.

        :return: Экземпляр AsyncSession
        :rtype: AsyncSession
        """
        async with self.async_session() as session:
            yield session
