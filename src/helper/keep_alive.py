# from flask import Flask
# from threading import Thread

# app = Flask('')


# @app.route('/')
# def main():
#     return "Du hast hier nix verloren"


# def run():
#     app.run(host="0.0.0.0", port=8080)


# def keep_alive():
#     try:
#         print("INFO: Keep_alive service starting...")
#         server = Thread(target=run)
#         server.start()
#     except Exception as e:
#         print(f"WARN: Keep_alive service did not start...\n{e}")
#         return
#     else:
#         print("INFO: keep_alive service started...")
