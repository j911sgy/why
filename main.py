import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "659d4142-ad67-4cc9-9cb9-ed2c51ac91ae")
    .replace("__vl__", "/vless")
    .replace("__vm__", "/vmess")
    .replace("__tr__", "/trojan")
)