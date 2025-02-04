"""Initialize Authentication Services."""
from .liftbot_service import show_liftbot, process_message

def register_services():
    """Dynamically register services for authentication."""
    return {
        "liftbot": {
            "show_liftbot": show_liftbot,
            "process_message": process_message
        }
    }
