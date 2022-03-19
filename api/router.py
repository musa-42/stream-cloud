from aiohttp import web
import re
from telethon.client.downloads import MAX_CHUNK_SIZE

class Router:
    
    RANGE_REGEX = re.compile(r"bytes=([0-9]+)-")
    BLOCK_SIZE = 1024*1024

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
        
        file_size = message.file.size
        file_ext = message.file.ext
        name = request.match_info.get("name") or self.get_file_name(message)

        range_http = request.headers.get("Range", 0)

        if not isinstance(range_http, int):
            #matches = self.RANGE_REGEX.search(range_http)
            #if matches is None:
            #    return web.HTTPBadRequest()
            #offset = matches.group(1)
            #end = matches.group(2) or file_size - 1
            #if not offset.isdigit():
            #    return web.HTTPBadRequest()
            #offset = int(offset)
            #end = int(end)
            offset, end = range_http.strip().strip('bytes=').split('-')
            if offset == "":
                offset = 0
            if end == "":
                end = file_size - 1
            offset = int(offset)
            end = int(end)
        else:
            offset = 0
            end = file_size - 1

        download_skip = (offset // self.BLOCK_SIZE) * self.BLOCK_SIZE
        read_skip = offset - download_skip

        if download_skip >= file_size:
            return web.HTTPRequestRangeNotSatisfiable()

        if read_skip > self.BLOCK_SIZE:
            return web.HTTPInternalServerError()

        if range:
            headers={
                'Content-Type': message.file.mime_type,
                'Accept-Ranges': 'bytes',
                'Content-Range': f'bytes {offset}-{end}/{file_size}',
                "Content-Length": str(file_size),
                "Content-Disposition": f'inline; filename={name}' ,
            }
        else :
            headers={
                'Content-Type': message.file.mime_type,
                "Content-Length": str(file_size),
                "Content-Disposition": f'inline; filename={name}' ,
            }

        print (offset,end)
        
        resp = web.StreamResponse(
            headers=headers,
            status = 206 if range_http else 200,
        )
        await resp.prepare(request)

        cls = self.client.iter_download(message.media, offset=download_skip, request_size=1024*1024 )

        async for part in cls:
            if offset > end:
                break
            if len(part) < read_skip:
                read_skip -= len(part)
            elif read_skip:
                await resp.write(part[read_skip:])
                read_skip = 0
            else:
                await resp.write(part)
            offset += len(part)
            
        return resp