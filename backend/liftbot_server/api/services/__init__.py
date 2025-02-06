"""Initialize Authentication Services."""
from .liftbot_service import init_liftbot, process_message

def register_services():
    """Dynamically register services for authentication."""
    return {
        "liftbot": {
            "init_liftbot": init_liftbot,
            "process_message": process_message
        }
    }
