"""爬虫入口。"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.server import main
from conf.settings import LOG_CONFIG, ip, 端口, 最大连接数

if __name__ == "__main__":
    main(ip,端口,最大连接数)
