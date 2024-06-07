from flask import Blueprint #type:ignore

from controllers.web_controller import index , account

web = Blueprint('web' , __name__)


web.route('/' , strict_slashes=False)(index)
web.route('/account' , strict_slashes=False)(account)

