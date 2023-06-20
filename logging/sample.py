import logging
from logging import FileHandler, Formatter, StreamHandler, config, getLogger

# 設定ファイル読み込み
config.fileConfig("logging.conf")

logger = getLogger()

# # loggerの設定
# logger = getLogger("log test")

# logger.setLevel(logging.DEBUG)

# # handlerの設定
# stream_handler = StreamHandler()
# stream_handler.setLevel(logging.DEBUG)
# handler_format = Formatter(
#     "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )
# stream_handler.setFormatter(handler_format)
# logger.addHandler(stream_handler)

# file_handler = FileHandler("test.log")
# file_handler.setFormatter(handler_format)
# logger.addHandler(file_handler)


logger.debug("Hello world")
logger.info("info")
