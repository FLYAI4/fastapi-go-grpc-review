import os
import sys
import uvicorn

root_path = os.path.abspath(os.path.join(__file__, os.path.pardir))
src_path = os.path.abspath(os.path.join(root_path, "src"))

if src_path not in sys.path:
    sys.path.append(src_path)

if __name__ == "__main__":
    from src import create_app
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
