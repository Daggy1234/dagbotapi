from fastapi import FastAPI,Header
import aiohttp
from fastapi.responses import StreamingResponse,JSONResponse
from io import BytesIO
from PIL import Image,ImageDraw,ImageFont,ImageEnhance,ImageOps,ImageFilter,ImageSequence
import wand.image as wi
from functools import partial
import asyncio
app = FastAPI()
async def checktoken(tok):
    return (True)
    if str(tok) == 'atMoMn2Pg3EUmZ065QBvdJN4IcjNxCQRMv1oZTZWg98i7HelIdvJwHtZFKPgCtf':
        return(True)
async def getimg(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            print(r)
            if r.status == 200:
                # imgf = await aiofiles.open(f'avatar{name}.png', mode='wb')
                byt = await r.read()
                return(byt)
                # await imgf.close()
            else:
                return False
            del r
def getsepia(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with wi.Image() as dst_image:
        with wi.Image(blob=io) as src_image:
            for frame in src_image.sequence:
                frame.sepia_tone(threshold=0.8)
                dst_image.sequence.append(frame)
        bts = dst_image.make_blob()
        i = BytesIO(bts)
        i.seek(0)
        return(i)
def getwasted(image: BytesIO):
    io = BytesIO(image)
    io.seek(0)
    with wi.Image() as dst_image:
        with wi.Image(blob=io) as src_image:
            for frame in src_image.sequence:
                frame.transform_colorspace('gray')
                dst_image.sequence.append(frame)
        bts = dst_image.make_blob()
        i = BytesIO(bts)
        i.seek(0)
    im = Image.open(i)
    fil = Image.open('wasted.png')
    w, h = im.size
    filr = fil.resize((w, h), 5)
    flist = []
    for frame in ImageSequence.Iterator(im):
        ci = im.convert('RGBA')
        ci.paste(filr, mask=filr)
        flist.append(ci)
    retimg = BytesIO()
    flist[0].save(retimg,format='gif', save_all=True, append_images=flist)
    retimg.seek(0)
    return(retimg)
def getgay(image:BytesIO):
    io = BytesIO(image)
    io.seek(0)
    with Image.open(io) as im:
        flist = []
        w, h = im.size
        fil = Image.open('gayfilter.png')
        filr = fil.resize((w, h), 5)
        for frame in ImageSequence.Iterator(im):
            ci = frame.convert('RGBA')
            ci.paste(filr, mask=filr)
            ci.show()
            flist.append(ci)
        retimg = BytesIO()
        flist[0].save(retimg, format='gif', save_all=True, append_images=flist)
    retimg.seek(0)
    return (retimg)
def getcharc(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with wi.Image() as dst_image:
        with wi.Image(blob=io) as src_image:
            for frame in src_image.sequence:
                frame.transform_colorspace("gray")
                frame.sketch(0.5, 0.0, 98.0)
                dst_image.sequence.append(frame)
        bts = dst_image.make_blob()
        i = BytesIO(bts)
        i.seek(0)
        return(i)
def getpaint(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with wi.Image() as dst_image:
        with wi.Image(blob=io) as src_image:
            for frame in src_image.sequence:
                frame.oil_paint(sigma=3)
                dst_image.sequence.append(frame)
        bts = dst_image.make_blob()
        i = BytesIO(bts)
        i.seek(0)
        return(i)
def getpixel(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with Image.open(io) as t:
        flist = []
        for frame in ImageSequence.Iterator(t):
            imgSmall = frame.resize((32, 32), resample=Image.BILINEAR)
            fim = imgSmall.resize(frame.size, Image.NEAREST)
            flist.append(fim)
        retimg = BytesIO()
        flist[0].save(retimg, format='gif', save_all=True, append_images=flist[1:])
    retimg.seek(0)
    return(retimg)
def getinvert(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with Image.open(io) as t:
        flist = []
        for frame in ImageSequence.Iterator(t):
            blurred_image = ImageOps.invert(frame)
            flist.append(blurred_image)
        retimg = BytesIO()
        flist[0].save(retimg, format='gif', save_all=True, append_images=flist[1:])
    retimg.seek(0)
    return(retimg)
def getblur(image: BytesIO):
    io =BytesIO(image)
    io.seek(0)
    with Image.open(io) as t:
        flist = []
        for frame in ImageSequence.Iterator(t):
            blurred_image = t.filter(ImageFilter.BLUR)
            flist.append(blurred_image)
        retimg = BytesIO()
        flist[0].save(retimg, format='gif', save_all=True, append_images=flist[1:])
    retimg.seek(0)
    return(retimg)

def gethitler(image: BytesIO):
    with Image.open(BytesIO(image)) as t:
        im = Image.open('hitler.jpg')
        wthf = t.resize((260, 300), 5)

        width = 800
        height = 600
        fim = im.resize((width, height), 4)
        area = (65, 40)
        fim.paste(wthf, area)
        retimg = BytesIO()
        fim.save(retimg, 'png')

    retimg.seek(0)
    return (retimg)





def getsatan(image: BytesIO):
    with Image.open(BytesIO(image)) as t:
        im = Image.open('satan.jpg')
        wthf = t.resize((400, 225), 5)
        width = 800
        height = 600
        fim = im.resize((width, height), 4)
        area = (250, 100)
        fim.paste(wthf, area)
        retimg = BytesIO()
        fim.save(retimg, 'png')

    retimg.seek(0)
    return (retimg)



def getwanted(image: BytesIO):
    with Image.open(BytesIO(image)) as av:
        im = Image.open('wanted.png')
        tp = av.resize((800, 800), 0)
        im.paste(tp, (200, 450))
        retimg = BytesIO()
        im.save(retimg, 'png')

    retimg.seek(0)
    return (retimg)



def getsithorld(image: BytesIO):
    with Image.open(BytesIO(image)) as ft:
        im = Image.open('sithlord.jpg')

        topa = ft.resize((250, 275), 5)
        size = (225, 225)
        mask = Image.new('L', size, 0)
        draw_mask = ImageDraw.Draw(mask)
        draw_mask.ellipse((50, 10) + size, fill=255)
        topt = ImageOps.fit(topa, mask.size, centering=(0.5, 0.5))
        im.paste(topt, (225, 180), mask=mask)
        retimg = BytesIO()
        im.save(retimg, 'png')
    retimg.seek(0)
    return (retimg)



def gettrash(image: BytesIO):
    with Image.open(BytesIO(image)) as t:
        im = Image.open('trash.jpg')
        wthf = t.resize((200, 150), 5)
        width = 800
        height = 600
        fim = im.resize((width, height), 4)
        area = (500, 250)
        fim.paste(wthf, area)
        retimg = BytesIO()
        fim.save(retimg, 'png')
    retimg.seek(0)
    return (retimg)



def getthoughtimg(image: BytesIO, text):
    with Image.open(BytesIO(image)) as ft:
        im = Image.open('speech.jpg')

        file = str(text)
        if len(file) > 200:
            return (f'Your text is too long {len(file)} is greater than 200')
        else:
            if len(file) > 151:
                fo = file[:50] + '\n' + file[50:]
                ft = fo[:100] + '\n' + fo[100:]
                ff = ft[:150] + '\n' + ft[150:]
                size = 10
            elif len(file) > 101:
                fo = file[:50] + '\n' + file[50:]
                ff = fo[:100] + '\n' + fo[100:]
                size = 12
            elif len(file) > 51 and len(file) < 100:
                ff = file[:50] + '\n' + file[50:]
                size = 14
            elif len(file) > 20 and len(file) <= 50:
                ff = file
                size = 18
            else:
                ff = file
                size = 25
            wthf = ft.resize((200, 225), 5)

            width = 800
            height = 600
            fim = im.resize((width, height), 4)
            area = (125, 50)
            fim.paste(wthf, area)
            base = fim.convert('RGBA')
            txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
            fnt = ImageFont.truetype('Helvetica-Bold-Font.ttf', size)
            d = ImageDraw.Draw(txt)
            d.text((400, 150), f"{ff}", font=fnt, fill=(0, 0, 0, 255))
            out = Image.alpha_composite(base, txt)
            retimg = BytesIO()
            out.save(retimg, 'png')
    retimg.seek(0)
    return (retimg)




def badimg(image : BytesIO):
    io = BytesIO(image)
    io.seek(0)
    with Image.open(BytesIO(image)) as im:
        back = Image.open('bad.png')
        t = im.resize((200, 200), 5)
        back.paste(t, (20, 150))
        bufferedio = BytesIO()
        back.save(bufferedio, format="PNG")
    bufferedio.seek(0)
    return (bufferedio)

def getangel(image: BytesIO):
    with Image.open(BytesIO(image)) as t:
        im = Image.open('angel.jpg')
        wthf = t.resize((300, 175), 5)
        width = 800
        height = 600
        fim = im.resize((width, height), 4)
        area = (250, 130)
        fim.paste(wthf, area)
        bufferedio = BytesIO()
        fim.save(bufferedio, format="PNG")
    bufferedio.seek(0)
    return (bufferedio)
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post('/api/wanted')
async def wanted(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getwanted,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/png")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/bad')
async def bad(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return ('Error')
        else:
            img = badimg(byt)
            return StreamingResponse(img, media_type="image/png")
    else:
        return ('Invalid token')

# @app.post('/api/deepfry')
# async def deepfry(token: str = Header(None),url:str = Header(None)):
#
#     r = await checktoken(token)
#     if r:
#         byt = await getimg(url)
#         if byt == False:
#             return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
#         else:
#             fn = partial(get,byt)
#             loop = asyncio.get_event_loop()
#             img = await loop.run_in_executor(None,fn)
#             if isinstance(img,BytesIO):
#                 return StreamingResponse(img, status_code=200,media_type="image/png")
#
#             else:
#                 return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
#     else:
#         return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/hitler')
async def hitler(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(gethitler,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/png")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/thoughtimage')
async def thoughtimage(token: str = Header(None),url:str = Header(None),text:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getthoughtimg,byt,text)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/png")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/angel')
async def angel(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getangel,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/png")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/trash')
async def trash(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(gettrash,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/png")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/satan')
async def satan(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getsatan,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/png")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/paint')
async def paint(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getpixel,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/gif")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})

@app.post('/api/evil')
async def evil(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getsithorld,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/png")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/blur')
async def blur(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getblur,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/gif")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})

@app.post('/api/invert')
async def invert(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getinvert,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/gif")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
#uvicorn main:app --reload
@app.post('/api/pixel')
async def pixel(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getpixel,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/gif")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/sepia')
async def sepia(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getsepia,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/gif")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/wasted')
async def wasted(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getwasted,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/gif")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/gay')
async def gay(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getgay,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/gif")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
@app.post('/api/charcoal')
async def charcoal(token: str = Header(None),url:str = Header(None)):

    r = await checktoken(token)
    if r:
        byt = await getimg(url)
        if byt == False:
            return JSONResponse(status_code=400,content={'error':"We were unable to use the link your provided"})
        else:
            fn = partial(getcharc,byt)
            loop = asyncio.get_event_loop()
            img = await loop.run_in_executor(None,fn)
            if isinstance(img,BytesIO):
                return StreamingResponse(img, status_code=200,media_type="image/gif")

            else:
                return JSONResponse(status_code=500,content={"error":"The Image manipulation had a small"})
    else:
        return JSONResponse(status_code=401,content={'error':'Invalid token'})
