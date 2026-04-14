#!/usr/bin/env python3

print("Set-Cookie: side=none; Path=/; HttpOnly; SameSite=Lax")
print("Content-Type: text/html")
print()
print('<meta http-equiv="refresh" content="0; url=/">')
exit(0)