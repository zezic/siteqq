from instance.config import HOST, PORT, DEBUG
from backend.app import app
app.run(debug=DEBUG, host=HOST, port=PORT)
