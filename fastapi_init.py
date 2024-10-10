# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import sqlite3

# 项目结构和文件的生成
def create_project_structure(project_name, additional_requirements=None):
    # 创建静态资源、模板目录
    os.makedirs(f"{project_name}/static/js", exist_ok=True)
    os.makedirs(f"{project_name}/static/css", exist_ok=True)
    os.makedirs(f"{project_name}/static/images", exist_ok=True)  # 图片上传目录
    os.makedirs(f"{project_name}/static/fonts", exist_ok=True)  # 字体文件夹
    os.makedirs(f"{project_name}/templates", exist_ok=True)

    # 创建后端文件
    backend_files = [
        f"{project_name}/main.py",
        f"{project_name}/api.py",
        f"{project_name}/models.py",
        f"{project_name}/schemas.py",
        f"{project_name}/database.py",
        f"{project_name}/crud.py",
        f"{project_name}/init_db.py",  # 数据库初始化文件
    ]
    
    for file in backend_files:
        with open(file, "w", encoding="utf-8") as f:
            if file.endswith("main.py"):
                f.write(main_py_content())
            elif file.endswith("api.py"):
                f.write(api_py_content())
            elif file.endswith("database.py"):
                f.write(database_py_content())
            elif file.endswith("init_db.py"):
                f.write(init_db_content())
            else:
                f.write("# TODO: 添加内容\n")

    # 创建 requirements.txt 并添加依赖
    with open(f"{project_name}/requirements.txt", "w", encoding="utf-8") as f:
        f.write("fastapi\n")
        f.write("uvicorn\n")
        f.write("pysqlite3\n")  # 使用 pysqlite3 作为 SQLite 依赖
        f.write("jinja2\n")  # 添加 Jinja2 依赖
        if additional_requirements:
            f.write("\n".join(additional_requirements) + "\n")

    print(f"项目结构 '{project_name}' 创建成功!")

    # 创建静态文件和模板文件
    static_js_content = '''console.log("静态 JS 文件加载完成.");'''
    static_css_content = '''body {
    font-family: Arial, sans-serif;
}

.sidebar {
    height: 100%;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    z-index: 100;
    padding: 48px 0 0;
}

.content {
    margin-left: 220px;
}

.header {
    background: #343a40;
    color: white;
    padding: 10px;
}

.card {
    margin-top: 20px;
}

    '''
    index_html_content = '''<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/css/style.css">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <title>FastAPI 网页应用</title>
</head>
<body>
    <div class="container-fluid">

        <div class="row">
            <nav class="col-md-2 sidebar bg-light p-3">
                <h4>菜单</h4>
                <ul class="nav flex-column">
                    <li class="nav-item">
                        <a class="nav-link active" href="#">仪表板</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">个人资料</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">设置</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">报告</a>
                    </li>
                </ul>
            </nav>
            <main class="col-md-9 ml-sm-auto col-lg-10 px-4 content">
        <header class="bg-dark text-white p-3">
            <nav class="nav">
                <a class="nav-link text-white" href="#">主页</a>
                <a class="nav-link text-white" href="#">个人资料</a>
                <a class="nav-link text-white" href="#">设置</a>
                <a class="nav-link text-white" href="#">报告</a>
            </nav>
        </header>
                <h2 class="mt-4">主要内容区域</h2>
                <p>这里是主要内容的展示区域。</p>
                <div class="card mb-4">
                    <div class="card-header">
                        图片上传
                    </div>
                    <div class="card-body">
                        <form action="/upload" method="post" enctype="multipart/form-data">
                            <div class="form-group">
                                <input type="file" name="file" accept="image/*" class="form-control-file">
                            </div>
                            <button type="submit" class="btn btn-primary">上传图片</button>
                        </form>
                    </div>
                </div>
                <div id="frame-container" class="mt-4">
                    <h3>其他信息</h3>
                    <p>此处可展示更多内容或信息。</p>
                </div>
            </main>
        </div>
    </div>
    <script src="/static/js/script.js"></script>
</body>

</html>

'''

    # 写入静态文件
    with open(f"{project_name}/static/js/script.js", "w", encoding="utf-8") as js_file:
        js_file.write(static_js_content)

    with open(f"{project_name}/static/css/style.css", "w", encoding="utf-8") as css_file:
        css_file.write(static_css_content)

    with open(f"{project_name}/templates/index.html", "w", encoding="utf-8") as html_file:
        html_file.write(index_html_content)

    print("静态文件和模板创建成功!")

    # 安装依赖
    install_requirements(project_name)

def install_requirements(project_name):
    try:
        print("正在安装依赖...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", f"{project_name}/requirements.txt"])
        print("依赖安装成功.")
    except subprocess.CalledProcessError as e:
        print(f"安装过程中出现错误: {e}")

# main.py 的内容 (后端入口)
def main_py_content():
    return '''# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import init_db

app = FastAPI()

# 初始化数据库
init_db.init_db()

# 设置静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 设置模板目录
templates = Jinja2Templates(directory="templates")

# 路由示例
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    upload_folder = "static/images"
    file_location = os.path.join(upload_folder, file.filename)
    
    with open(file_location, "wb") as f:
        f.write(await file.read())
    
    return {"info": f"文件 '{file.filename}' 已保存至 '{file_location}'"}

# 包含 API 路由
import api
app.include_router(api.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # 运行在 0.0.0.0:8000
'''

# api.py 的内容 (简单的API路由)
def api_py_content():
    return '''# -*- coding: utf-8 -*-
from fastapi import APIRouter

router = APIRouter()

@router.get("/api/items/")
def read_items():
    return {"items": ["item1", "item2", "item3"]}
'''

# database.py 的内容
def database_py_content():
    return '''# -*- coding: utf-8 -*-
import sqlite3

DATABASE_URL = "sqlite:///./app.db"

def get_db():
    conn = sqlite3.connect("app.db")
    try:
        yield conn
    finally:
        conn.close()
'''

# init_db.py 的内容 (数据库初始化)
def init_db_content():
    return '''# -*- coding: utf-8 -*-
import sqlite3
import os

def init_db():
    if not os.path.exists("app.db"):  # 检查数据库是否存在
        conn = sqlite3.connect("app.db")
        cursor = conn.cursor()
        
        # 创建表（根据需要定义表的结构）
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        
        conn.commit()
        conn.close()
        print("数据库初始化完成.")
    else:
        print("数据库已存在，跳过初始化.")

'''

# 执行项目结构创建
if __name__ == "__main__":
    # 获取用户输入的项目名称
    project_name = input("请输入项目名称: ").strip()
    
    if not project_name:
        print("项目名称是必需的！")
        sys.exit(1)
    
    # 获取用户输入的额外依赖项 (可选)
    additional_requirements_input = input("请输入额外依赖项（空格分隔，可选）: ")
    additional_requirements = additional_requirements_input.split() if additional_requirements_input else []

    create_project_structure(project_name, additional_requirements)
