from subprocess import call


def create_2_migrations() -> None:
    """
    With using subprocess.call makes initial migration which
    auto generates tables, then upgrading
    After that creates empty migration so we can manually
    write migration script
    """
    call("alembic revision --autogenerate -m 'creating_tables'")
    call("alembic upgrade head")
    call("alembic revision -m 'manual_migration'")


if __name__ == "__main__":
    create_2_migrations()
