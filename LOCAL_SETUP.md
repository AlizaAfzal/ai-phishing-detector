# 🏠 Local Setup Guide for AI Phishing Email Detection

## **✅ Quick Start (No MongoDB Required)**

Your app is now configured to run locally without any external dependencies!

### **Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 2: Run the App**
```bash
python app.py
```

### **Step 3: Access the App**
- **Homepage**: http://localhost:5000
- **Login**: http://localhost:5000/login.html
- **Signup**: http://localhost:5000/signup.html
- **Detector**: http://localhost:5000/detector.html (after login)
- **Health Check**: http://localhost:5000/health

---

## **🔧 What's Fixed**

### **✅ MongoDB Connection**
- **Automatic fallback** to in-memory storage when MongoDB is not available
- **No installation required** - works out of the box
- **Persistent data** during app runtime (resets when you restart)

### **✅ Error Handling**
- **Better error messages** with helpful instructions
- **Graceful degradation** when services are unavailable
- **Mock database** for development and testing

### **✅ Simplified Configuration**
- **Removed deployment files** (vercel.json, render.yaml, etc.)
- **Clean local setup** without deployment complexity
- **Environment variables** are optional

---

## **📋 Features Available**

### **✅ User Management**
- **User registration** with email verification
- **Login/logout** functionality
- **Password strength validation**
- **OTP email verification** (requires email setup)

### **✅ Email Analysis**
- **AI-powered phishing detection** using Hugging Face
- **Header analysis** for technical indicators
- **Comprehensive analysis** with confidence scores
- **Analysis history** for logged-in users

### **✅ User Interface**
- **Modern, responsive design**
- **Real-time analysis results**
- **User-friendly error messages**
- **Analysis history display**

---

## **🔧 Optional Setup (For Full Features)**

### **Email Configuration (Optional)**
To enable OTP email sending, create a `.env` file:
```bash
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```

### **Hugging Face API (Optional)**
For better AI analysis, add to `.env`:
```bash
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

### **MongoDB (Optional)**
For persistent data storage:
1. **Install MongoDB locally** or use **MongoDB Atlas**
2. Add to `.env`:
```bash
MONGO_URI=mongodb://localhost:27017/mailguard
```

---

## **🚀 Running the App**

### **Basic Run (No Configuration)**
```bash
python app.py
```

### **With Environment Variables**
```bash
# Create .env file with your settings
# Then run:
python app.py
```

### **Expected Output**
```
⚠️ MongoDB connection failed: [Errno 111] Connection refused
⚠️ Using in-memory storage for development
💡 To use MongoDB, either:
   1. Install MongoDB locally: https://docs.mongodb.com/manual/installation/
   2. Use MongoDB Atlas: https://cloud.mongodb.com/
   3. Set MONGO_URI environment variable
✅ Hugging Face API key configured (first 10 chars: hf_tKUvfyK...)
📧 Email configuration: mailguard849@gmail.com
⚠️ Warning: Using default email password. Please set EMAIL_PASSWORD environment variable.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
```

---

## **🧪 Testing the App**

### **1. Health Check**
Visit: http://localhost:5000/health
Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2025-01-XX...",
  "database": "error: ...",
  "huggingface_key": "configured",
  "email_configured": "no"
}
```

### **2. User Registration**
1. Go to http://localhost:5000/signup.html
2. Create an account
3. Check your email for OTP (if configured)

### **3. Email Analysis**
1. Login to the app
2. Go to the detector page
3. Paste an email for analysis
4. View results and history

---

## **🔧 Troubleshooting**

### **Port Already in Use**
```bash
# Kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or use a different port
python app.py --port 5001
```

### **Import Errors**
```bash
# Install missing dependencies
pip install -r requirements.txt

# Or install individually
pip install Flask pymongo Werkzeug requests python-dotenv
```

### **Email Not Sending**
- Check your `.env` file configuration
- Verify Gmail App Password is correct
- Check internet connection

---

## **📁 File Structure**

```
AI Phishing Email Detection/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (optional)
├── templates/                # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   └── detector.html
├── static/                   # CSS, JS, images
│   ├── style.css
│   └── script.js
├── comprehensive_email_analyzer.py
├── email_header_analyzer.py
├── header_ml_model.py
└── LOCAL_SETUP.md           # This file
```

---

## **🎯 Next Steps**

1. **Test the app** - Make sure everything works
2. **Configure email** - Set up OTP functionality
3. **Add MongoDB** - For persistent data storage
4. **Customize** - Modify the UI or add features
5. **Deploy** - When ready, choose a platform (Vercel, Render, etc.)

---

## **💡 Pro Tips**

- **Use the mock database** for development and testing
- **Set up email configuration** for full OTP functionality
- **Test with real phishing emails** to verify detection
- **Monitor the console** for helpful error messages
- **Check the health endpoint** to verify all services

**Your app is now ready to run locally! 🚀**
