import asyncio
import concurrent
import os
import time
import uvloop

from sanic import Sanic, response, config

# Define a CPU bound worker function
def deep_thought(data):
    print("Working to answer: " + data)
    time.sleep(5)  # Actually not CPU bound in this example, but outcome should be identical
    return 42

# Enable extra asyncio debugging
# os.environ['PYTHONASYNCIODEBUG'] = "1"

# Make sure uvloop is used as event loop by default
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# Create ProcessPoolExecutor
executor = concurrent.futures.ProcessPoolExecutor(max_workers=5)

# Create the Sanic app which should(?!?) use the same event loop as create above
config.Config.LOGO = None
app = Sanic()


# Endpoint to test server responsiveness
@app.route("/")
async def root(request):
    return response.json({"root": True})


# CPU bound endpoint
@app.route("/ask")
async def ask(request):
    # CPU bound 작업은 eventloop를 거치도록 만든다.
    # 미리 만들어둔 executor에 던져서 async 동작이 가능하도록 한다.
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(
        executor,
        deep_thought,
        "GG"
    )
    return response.json({"result": res})


# Run the Sanic app (which will start the event loop again)
app.run(host="0.0.0.0", port=12000, debug=True)
