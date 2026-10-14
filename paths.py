# -*- coding: utf-8 -*-
"""مسارات الملفات: على Railway اربط Volume وسيتم استخدامه تلقائياً."""
import os
import shutil

_CODE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = (
    os.environ.get("DATA_DIR")
    or os.environ.get("RAILWAY_VOLUME_MOUNT_PATH")
    or _CODE_DIR
)
os.makedirs(DATA_DIR, exist_ok=True)

ACCOUNTS_FILE = os.path.join(DATA_DIR, "accounts.json")
TOKEN_CACHE_FILE = os.path.join(DATA_DIR, "token_cache.json")
DEVICES_FILE = os.path.join(DATA_DIR, "devices.json")

# أول تشغيل على Volume فاضي: انسخ devices.json المرفق مع المشروع
_seed = os.path.join(_CODE_DIR, "devices.json")
if os.path.abspath(DATA_DIR) != _CODE_DIR and not os.path.exists(DEVICES_FILE) and os.path.exists(_seed):
    try:
        shutil.copyfile(_seed, DEVICES_FILE)
    except Exception:
        pass
