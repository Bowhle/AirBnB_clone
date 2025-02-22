from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


# Create instance of FileStorage
storage = FileStorage()
storage.reload()

# Map of all valid classes for dynamic creation
classes = {
    "BaseModel": BaseModel,
    "User": User,
}
