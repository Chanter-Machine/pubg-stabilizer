from playsound import playsound
import os
import edge_tts
import sys
from model.contants import c_contants
import asyncio

VOICE = "zh-CN-XiaoxiaoNeural"
VOICE_BASE_PATH = "./resource/voice/"


async def generate_voice(text):
    communicate = edge_tts.Communicate(text, VOICE)
    with open(VOICE_BASE_PATH + text + ".mp3", "wb") as file:
        async for stream in communicate.stream():
            if stream["type"] == "audio":
                file.write(stream["data"])
        file.flush()
        os.fsync(file.fileno())
    await asyncio.sleep(1)
    return VOICE_BASE_PATH + text + ".mp3"


async def text2voice_task(text):
    if not c_contants.isAuthorized:
        sys.exit()
    try:
        if not os.path.exists(VOICE_BASE_PATH + text + ".mp3"):
            await generate_voice(text)
        playsound(VOICE_BASE_PATH + text + ".mp3")
    except Exception:
        print(Exception)


async def text2voice_list_task(text_list):
    for text in text_list:
        await text2voice_task(text)
        await asyncio.sleep(0.1)


def text2voice(text):
    asyncio.run(text2voice_task(text))


def text2voice_list(text_list):
    asyncio.run(text2voice_list_task(text_list))


if __name__ == '__main__':
    VOICE_BASE_PATH = "../resource/voice/"
    asyncio.run(text2voice("已停止"))
