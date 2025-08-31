# 🔧 Render Deployment Troubleshooting Guide

## **🚨 Common Deployment Issues**

### **Issue 1: Build Failures**

**Symptoms:**
- Build fails during dependency installation
- Error messages about missing packages
- Python version conflicts

**Solutions:**
1. **Check requirements.txt:**
   ```bash
   # Make sure all dependencies are listed
   Flask==2.3.3
   pymongo==4.5.0
   Werkzeug==2.3.7
   requests==2.31.0
   python-dotenv==1.0.0
   gunicorn==21.2.0
   dnspython==2.4.2
   transformers==4.35.0
   torch==2.1.0
   numpy==1.24.3
   scikit-learn==1.3.0
   pandas==2.0.3
   ```

2. **Check runtime.txt:**
   ```
   python-3.9.16
   ```

3. **Check Procfile:**
   ```
   web: gunicorn app:app
   ```

### **Issue 2: Environment Variables Missing**

**Symptoms:**
- App starts but crashes immediately
- Database connection errors
- API key errors

**Solutions:**
1. **Verify all environment variables are set:**
   ```
   SECRET_KEY=9LN36ZsohRVZNKd8HqPDUDBTLjr4l8oTulz769uB4zw
   MONGO_URI=mongodb+srv://phishing_detector_user:YOUR_PASSWORD@cluster0.xxxxx.mongodb.net/mailguard?retryWrites=true&w=majority
   HUGGINGFACE_API_KEY=hf_tKUvfyK... (your existing key)
   EMAIL_ADDRESS=mailguard849@gmail.com
   EMAIL_PASSWORD=awvlcrrnpktpzbuo (your Gmail App Password)
   ```

2. **Check for typos in variable names**
3. **Ensure no extra spaces in values**

### **Issue 3: Database Connection Problems**

**Symptoms:**
- MongoDB connection timeouts
- Authentication errors
- Network access denied

**Solutions:**
1. **Verify MongoDB Atlas setup:**
   - Cluster is active
   - Network access allows all IPs (0.0.0.0/0)
   - Database user has correct permissions
   - Connection string is correct

2. **Test connection locally:**
   ```bash
   python test_mongodb_atlas.py
   ```

### **Issue 4: App Crashes on Startup**

**Symptoms:**
- App deploys but shows "Application Error"
- 500 Internal Server Error
- App not responding

**Solutions:**
1. **Check app.py for errors:**
   - Verify all imports work
   - Check for syntax errors
   - Ensure Flask app is properly configured

2. **Add error handling:**
   ```python
   if __name__ == '__main__':
       try:
           port = int(os.environ.get('PORT', 5000))
           app.run(host='0.0.0.0', port=port, debug=False)
       except Exception as e:
           print(f"Error starting app: {e}")
   ```

### **Issue 5: Free Tier Limitations**

**Symptoms:**
- App sleeps after inactivity
- Slow startup times
- Resource limitations

**Solutions:**
1. **This is normal for free tier**
2. **First request may take 30-60 seconds**
3. **Consider upgrading for production use**

---

## **🔍 Step-by-Step Debugging**

### **Step 1: Check Render Logs**
1. Go to your Render dashboard
2. Click on your web service
3. Go to "Logs" tab
4. Look for error messages

### **Step 2: Common Error Messages**

**"Build failed":**
- Check requirements.txt
- Verify Python version
- Check for missing dependencies

**"Application Error":**
- Check environment variables
- Verify database connection
- Check app.py for errors

**"Connection timeout":**
- Check MongoDB Atlas setup
- Verify network access
- Test connection locally

### **Step 3: Test Locally First**
```bash
# Test your app locally with production settings
python app.py
```

### **Step 4: Check Environment Variables**
```bash
# Test environment variables
python check_env.py
```

---

## **🚀 Quick Fixes**

### **Fix 1: Update requirements.txt**
Make sure your requirements.txt includes:
```txt
Flask==2.3.3
pymongo==4.5.0
Werkzeug==2.3.7
requests==2.31.0
python-dotenv==1.0.0
gunicorn==21.2.0
dnspython==2.4.2
transformers==4.35.0
torch==2.1.0
numpy==1.24.3
scikit-learn==1.3.0
pandas==2.0.3
```

### **Fix 2: Add Health Check Endpoint**
Add this to your app.py:
```python
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}
```

### **Fix 3: Improve Error Handling**
Add this to your app.py:
```python
@app.errorhandler(500)
def internal_error(error):
    return {'error': 'Internal server error'}, 500

@app.errorhandler(404)
def not_found_error(error):
    return {'error': 'Not found'}, 404
```

---

## **📞 Getting Help**

### **1. Render Support**
- Check Render documentation: https://render.com/docs
- Contact Render support through dashboard

### **2. Check Your Logs**
- Always check the logs first
- Look for specific error messages
- Copy error messages for troubleshooting

### **3. Common Solutions**
- **Redeploy**: Sometimes a simple redeploy fixes issues
- **Check environment variables**: Most common cause of failures
- **Verify database connection**: MongoDB Atlas setup issues
- **Update dependencies**: Outdated packages can cause problems

---

## **🎯 Next Steps**

1. **Check your Render logs** for specific error messages
2. **Verify all environment variables** are set correctly
3. **Test your app locally** with production settings
4. **Check MongoDB Atlas** connection
5. **Update your code** if needed and redeploy

**Share the specific error message from your Render logs, and I can help you fix it!**
