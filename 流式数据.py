'''
流式传输：按照数据原始的格式连续不断的输出
'''

import base64
from io import BytesIO

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

import asyncio
from collections.abc import AsyncIterable,Iterable


# messages="""
# Rick: (stumbles in drunkenly, and turns on the lights) Morty! You gotta come on. You got--... you gotta come with me.
# Morty: (rubs his eyes) What, Rick? What's going on?
# Rick: I got a surprise for you, Morty.
# Morty: It's the middle of the night. What are you talking about?
# Rick: (spills alcohol on Morty's bed) Come on, I got a surprise for you. (drags Morty by the ankle) Come on, hurry up. (pulls Morty out of his bed and into the hall)
# Morty: Ow! Ow! You're tugging me too hard!
# Rick: We gotta go, gotta get outta here, come on. Got a surprise for you Morty.
# """


# class PNGStreamingResponse(StreamingResponse):
#     media_type = "text/plain"    
#     # headers={
#     #         "Cache-Control": "no-cache",
#     #         "Connection": "keep-alive",
#     #         "X-Accel-Buffering": "no"  # 禁用 Nginx 缓冲
#     #     }

image_base64="iVBORw0KGgoAAAANSUhEUgAAAB0AAAAdCAYAAABWk2cPAAAAbnpUWHRSYXcgcHJvZmlsZSB0eXBlIGV4aWYAAHjadYzRDYAwCET"
padding = len(image_base64) % 4
if padding:
    image_base64 += "=" * (4 - padding)
binary_image=base64.b64decode(image_base64)

def read_image():
    return BytesIO(binary_image)


app=FastAPI()


@app.get("/story/stream",response_class=StreamingResponse)
async def get_story():
    async def generator():
        with read_image() as f:
            for chunk in f:
                yield chunk
    return StreamingResponse(
        generator(),
        media_type="text/plain"
        )
