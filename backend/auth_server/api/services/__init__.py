"""Initialize Authentication Services."""
from .auth_service import login_user, create_user, edit_user_password, update_user_info, authenticate_user

def register_services():
    """Dynamically register services for authentication."""
    return {
        "auth": {
            "login_user": login_user,
            "create_user": create_user,
            "edit_user_password": edit_user_password,
            "update_user_info": update_user_info,
            "authenticate_user": authenticate_user,
        }
    }
