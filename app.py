
from flask import Flask # type:ignore
from flask_migrate import Migrate # type:ignore
from config import db
from routes.article_route import article
from routes.user_route import user

app = Flask (__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app , db )


app.register_blueprint(article , url_prefix='/')
app.register_blueprint(user , url_prefix='/')

if __name__ =='__main__':
    app.run(debug=True)