from aiohttp import web
import re
from telethon.client.downloads import MAX_CHUNK_SIZE

class Router:
    
    RANGE_REGEX = re.compile(r"bytes=([0-9]+)-")
    BLOCK_SIZE = MAX_CHUNK_SIZE
    ext_attachment = [".mp4", ]

    
    async def hello(self, request):
        return web.Response(text="Hello, world")

    async def Downloader(self, request):
        id_hex = request.match_info.get("id")
        
        try:
            id = int(id_hex,16)
        except ValueError:
            return web.HTTPNotFound()
        
        message = await self.client.get_messages(self.CHANNEL, ids=id)

        if not message or not message.file :
            return web.HTTPNotFound()
        
        offset = request.headers.get("Range", 0)

        if not isinstance(offset, int):
            matches = self.RANGE_REGEX.search(offset)
            if matches is None:
                return web.HTTPBadRequest()
            offset = matches.group(1)
            if not offset.isdigit():
                return web.HTTPBadRequest()
            offset = int(offset)

        file_size = message.file.size
        file_ext = message.file.ext
        download_skip = (offset // self.BLOCK_SIZE) * self.BLOCK_SIZE
        read_skip = offset - download_skip
        
        name = request.match_info.get("name") or self.get_file_name(message)

        if download_skip >= file_size:
            return web.HTTPRequestRangeNotSatisfiable()

        if read_skip > self.BLOCK_SIZE:
            return web.HTTPInternalServerError()

        resp = web.StreamResponse(
            headers={
                'Content-Type': message.file.mime_type, #'application/octet-stream',
                'Accept-Ranges': 'bytes',
                'Content-Range': f'bytes {offset}-{file_size}/{file_size}',
                "Content-Length": str(file_size),
                "Content-Disposition": f'attachment; filename={name}' if file_ext in self.ext_attachment else f'inline; filename={name}' ,
            },
            status = 206 if offset else 200,
        )
        await resp.prepare(request)

        cls = self.client.iter_download(message.media, offset=download_skip)

        async for part in cls:
            if len(part) < read_skip:
                read_skip -= len(part)
            elif read_skip:
                await resp.write(part[read_skip:])
                read_skip = 0
            else:
                await resp.write(part)
                
        return resp