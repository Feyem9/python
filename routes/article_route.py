from flask import Blueprint # type:ignore

from controllers.article_controller import index , add_post , create , view , update , delete

article = Blueprint('article' , __name__)

article.route('/' , methods=['GET'] , strict_slashes=False)(index)
article.route('/add_post' , methods=['GET'] , strict_slashes=False)(add_post)
article.route('/create' , methods=['POST'] , strict_slashes=False)(create)
article.route('/view/<article_id>' , methods=['GET'] , strict_slashes=False)(view)
article.route('/update/<article_id>' , methods=['GET' , "POST"] , strict_slashes=False)(update)
article.route('/delete/<article_id>' , methods=['POST' , "DELETE"] , strict_slashes=False)(delete)
