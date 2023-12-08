from fastapi import FastAPI
from routers import main_router

app = FastAPI()
app.include_router(main_router)


if __name__ == '__main__':
    import uvicorn
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', default=8000)
    parser.add_argument('--reload', action='store_true')
    
    args = parser.parse_args()

    uvicorn.run(app, host=args.host, port=args.port, reload=args.reload, reload_dirs=['.'])
