from Crypto.Cipher import XOR
import base64

key = "AutomateAllTheThings"

encrypted = "ORoMDUBQRFNxVV9iUFFlXF9DMhFzJBU9JhQOADQLChEtHyIgPhY2OxcS"

cipher = XOR.new(key)
cipher.decrypt(base64.b64decode(encrypted))

API_TOKEN = cipher.decrypt(base64.b64decode(encrypted))

DEFAULT_REPLY = "Sorry but I didn't understand you"
