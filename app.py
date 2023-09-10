from flask import Flask
from index import Flask_Init

def create_app():
    app = Flask(__name__)

    sql_host_port='localhost:3306'
    sql_user_name='root'
    sql_user_key='123456'
    sql_database='ysl'

    app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{sql_user_name}:{sql_user_key}'+\
                                            f'@{sql_host_port}/{sql_database}?charset=utf8'
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SECRET_KEY'] = 'iamthekey'
    app.jinja_env.auto_reload = True

    global port,host
    port=2520
    website=f'localhost:{port}'
    website=f'0.0.0.0:{port}'
    host,port=website.split(':')
    Flask_Init(app)

    return app

if __name__ == '__main__':

    app=create_app()
    app.run(host,port,debug=True)

    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
