"""Initialize Authentication Services."""
from .auth_service import login_user, create_user, edit_user_password, update_user_info, authenticate_user, get_difficulty, get_profile, update_profile

def register_services():
    """Dynamically register services for authentication."""
    return {
        "auth": {
            "login_user": login_user,
            "create_user": create_user,
            "edit_user_password": edit_user_password,
            "update_user_info": update_user_info,
            "authenticate_user": authenticate_user,
            "get_difficulty": get_difficulty,
            "get_profile": get_profile,
            "update_profile": update_profile
        }
    }
