import base64
import os

import requests


def read_latest() -> str:
    resp = requests.get(
        url="https://api.github.com/repos/RockChinQ/QChatGPT/contents/res/announcement",
    )
    obj_json = resp.json()
    b64_content = obj_json["content"]
    # 解码
    content = base64.b64decode(b64_content).decode("utf-8")
    return content


def read_saved() -> str:
    # 已保存的在res/announcement_saved
    # 检查是否存在
    if not os.path.exists("res/announcement_saved"):
        with open("res/announcement_saved", "w") as f:
            f.write("")

    with open("res/announcement_saved", "r") as f:
        content = f.read()

    return content


def write_saved(content: str):
    # 已保存的在res/announcement_saved
    with open("res/announcement_saved", "w") as f:
        f.write(content)


def fetch_new() -> str:
    latest = read_latest()
    saved = read_saved()
    if latest.replace(saved, "").strip() == "":
        return ""
    else:
        write_saved(latest)
        return latest.replace(saved, "").strip()
