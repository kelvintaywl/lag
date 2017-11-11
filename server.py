import argparse
import asyncio
import json

from japronto import Application, RouteNotFoundException
from japronto.request import HttpRequest


DELAY_MS = 1000  # 1sec


def handler_err_not_found(request: HttpRequest, _: RouteNotFoundException):
    return request.Response(code=404, text='Sorry, Not Found')


def hello(request: HttpRequest):
    return request.Response(text='Hello world!')


async def handler_delay(request: HttpRequest):
    time_ms = int(
        request.match_dict.get('time_ms', DELAY_MS)
    )

    resp_types = {}
    try:
        # if client sends a JSON body, we use that to return as response
        resp_types['json'] = request.json
    except json.JSONDecodeError:
        resp_types['json'] = None
    finally:
        if not resp_types.get('json'):
            resp_types['text'] = 'ping pong'

    await asyncio.sleep((time_ms / 1000))
    return request.Response(**resp_types)


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8080)
    return parser.parse_args()

if __name__ == '__main__':

    opts = parse_args()

    app = Application()
    app.router.add_route('/', hello)
    app.router.add_route('/delay/{time_ms}', handler_delay)
    app.add_error_handler(RouteNotFoundException, handler_err_not_found)
    app.run(debug=True, port=opts.port)
