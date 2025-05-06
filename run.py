from project import create_app

if __name__ == '__main__':
    import os
  app = create_app()
   debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
