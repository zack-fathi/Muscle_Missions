"""Initialize service modules for the Muscle Missions backend."""

def register_services():
    from ....backend.auth_server.services.auth_service import login_user, create_user, edit_user_password, update_user_info, authenticate_user
    from ....workout_server.api.services.workouts_service import generate_workout_plan
    # from .liftbot_service import process_liftbot_message

    return {
        "auth": {
            "login_user": login_user,
            "create_user": create_user,
            "edit_user_password": edit_user_password,
            "update_user_info": update_user_info,
            "authenticate_user": authenticate_user
        },
        "workouts": {
            "generate_workout_plan": generate_workout_plan
        }
        # "liftbot": {
        #     "process_liftbot_message": process_liftbot_message
        # }
    }
