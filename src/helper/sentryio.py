# import sentry_sdk
# import os


# def start_sentryio():
#     try:
#         print("INFO: SentryIO service starting...")
#         sentry_sdk.init((os.getenv("sentry_io")), traces_sample_rate=1.0)
#     except Exception as e:
#         print(f"WARN: SentryIO service did not start...\n{e}")

#     else:
#         print("INFO: SentryIO service started...")
