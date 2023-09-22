import time as tm
from plot import *
start = tm.time()
async def hola():
    await create_graph("x**2", 10, 20, "papo9292@gmail.com")
await hola()
print(tm.time()-start)
