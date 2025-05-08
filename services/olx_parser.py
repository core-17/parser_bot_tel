import aiohttp
import logging

async def check_url(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                if resp.status == 200:
                    return True
                else:
                    return False
    except Exception as e:
        logging.error(f"Parser error for {url}: {e}")
        return False