from project import create_app

if __name__ == '__main__':
<<<<<<< HEAD
    import os
  app = create_app()
   debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
=======
  import os
  app = create_app()
  debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
  app.run(host = '127.0.0.1', port = 8001, debug=debug_mode) 
>>>>>>> 52a9e85b358585eda0da5363e89e619d89206ae8
