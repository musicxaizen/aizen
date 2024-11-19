from pyrogram.enums import MessageEntityType
from pyrogram.types import Message, User
from pyrogram.errors import PeerIdInvalid

from Dev import app

async def extract_user(m: Message) -> User:
    try:
        if m.reply_to_message:
            return m.reply_to_message.from_user
        
        if not m.entities:
            raise ValueError("No entities found in the message.")
        
        # Extract the relevant entity
        msg_entities = m.entities[1] if m.text.startswith("/") else m.entities[0]

        # Determine the user ID based on the type of entity
        if msg_entities.type == MessageEntityType.TEXT_MENTION:
            user_id = msg_entities.user.id
        elif msg_entities.type == MessageEntityType.MENTION:
            # Handle case where mention is in text
            user_id = int(m.command[1]) if m.command[1].isdecimal() else m.command[1]
        else:
            raise ValueError("Unsupported entity type.")

        # Get user information
        return await app.get_users(user_id)
    
    except PeerIdInvalid:
        # Handle case where the user ID is invalid
        raise ValueError("The user ID is invalid or the user is not known.")
    except Exception as e:
        # Handle any other exceptions
        raise RuntimeError(f"An error occurred while extracting the user: {e}")
