#!/usr/bin/env python3
"""
Check deployment readiness for Render
"""

import os
import sys

def check_deployment():
    """Check if the app is ready for deployment"""
    
    print("🔍 Deployment Readiness Check")
    print("=" * 50)
    
    # Check required files
    required_files = [
        'app.py',
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        'render.yaml'
    ]
    
    print("\n📁 Required Files:")
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
    
    # Check requirements.txt
    print("\n📦 Dependencies Check:")
    try:
        with open('requirements.txt', 'r') as f:
            requirements = f.read()
            
        required_deps = [
            'Flask',
            'pymongo',
            'Werkzeug',
            'requests',
            'python-dotenv',
            'gunicorn'
        ]
        
        for dep in required_deps:
            if dep in requirements:
                print(f"✅ {dep}")
            else:
                print(f"❌ {dep} - MISSING")
    except Exception as e:
        print(f"❌ Error reading requirements.txt: {e}")
    
    # Check environment variables
    print("\n🔐 Environment Variables:")
    env_vars = [
        'SECRET_KEY',
        'MONGO_URI',
        'HUGGINGFACE_API_KEY',
        'EMAIL_ADDRESS',
        'EMAIL_PASSWORD'
    ]
    
    for var in env_vars:
        value = os.getenv(var)
        if value:
            if var == 'SECRET_KEY':
                print(f"✅ {var} - Set ({len(value)} chars)")
            elif var == 'HUGGINGFACE_API_KEY':
                print(f"✅ {var} - Set ({value[:10]}...)")
            elif var == 'EMAIL_PASSWORD':
                print(f"✅ {var} - Set ({len(value)} chars)")
            else:
                print(f"✅ {var} - Set")
        else:
            print(f"❌ {var} - NOT SET")
    
    # Check app.py syntax
    print("\n🐍 Python Syntax Check:")
    try:
        with open('app.py', 'r') as f:
            compile(f.read(), 'app.py', 'exec')
        print("✅ app.py syntax is valid")
    except SyntaxError as e:
        print(f"❌ app.py syntax error: {e}")
    except Exception as e:
        print(f"❌ Error checking app.py: {e}")
    
    # Check if app can import
    print("\n📥 Import Check:")
    try:
        import app
        print("✅ app.py can be imported")
    except ImportError as e:
        print(f"❌ Import error: {e}")
    except Exception as e:
        print(f"❌ Error importing app: {e}")
    
    # Check MongoDB connection
    print("\n🗄️ MongoDB Connection:")
    try:
        from pymongo import MongoClient
        mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')
        print("✅ MongoDB connection successful")
        client.close()
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Deployment Status Summary:")
    
    # Count issues
    issues = 0
    if not all(os.path.exists(f) for f in required_files):
        issues += 1
        print("❌ Missing required files")
    
    if not all(os.getenv(var) for var in env_vars):
        issues += 1
        print("❌ Missing environment variables")
    
    if issues == 0:
        print("✅ Ready for deployment!")
        print("\n📝 Next steps:")
        print("1. Push to GitHub")
        print("2. Deploy to Render")
        print("3. Set environment variables in Render")
        print("4. Monitor deployment logs")
    else:
        print(f"❌ {issues} issue(s) need to be fixed before deployment")

if __name__ == "__main__":
    check_deployment()
