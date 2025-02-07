from src.db import User, session


def test_database():
    new_user = User(name="Test User")
    session.add(new_user)
    session.commit()
    user = session.query(User).filter_by(name="Test User").first()
    assert user is not None


def test_user_creation():
    user = User(name="Integration Test User")
    session.add(user)
    session.commit()
    assert user.id is not None
