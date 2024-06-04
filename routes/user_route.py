from flask import Blueprint # type:ignore

from controllers.users_controllers import index_user , add_user , create_user , view_user , update_user , delete_user

user = Blueprint('user' , __name__)

user.route('/user' , methods=['GET'] , strict_slashes=False)(index_user)
user.route('/add_user' , methods=['GET'] , strict_slashes=False)(add_user)
user.route('/create_user' , methods=['POST'] , strict_slashes=False)(create_user)
user.route('/view_user/<user_id>' , methods=['GET'] , strict_slashes=False)(view_user)
user.route('/update_user/<user_id>' , methods=['GET' , "POST"] , strict_slashes=False)(update_user)
user.route('/delete_user/<user_id>' , methods=['POST' , "DELETE"] , strict_slashes=False)(delete_user)
