import sqlalchemy as db

engine = db.create_engine('sqlite:///database_bot.db')

connection = engine.connect()

metadata = db.MetaData()

game = db.Table('rooms', metadata,
                    db.Column('id', db.Integer, primary_key=True),
                    db.Column('description', db.Text),
                    db.Column('variations', db.JSON)
                    )

users = db.Table('users', metadata,
                    db.Column('id', db.Integer, primary_key=True),
                    db.Column('id_chat', db.VARCHAR()),
                    db.Column('status', db.VARCHAR())
                    )

states = db.Table('states', metadata,
                    db.Column('id', db.Integer, primary_key=True),
                    db.Column('current_room', db.Integer),
                    db.Column('visited_room', db.JSON),
                    db.Column('inventory', db.JSON),
                    db.Column('characteristic', db.JSON),
                    )

metadata.create_all(engine)

