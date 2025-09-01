# 🚀 Vercel Deployment Guide for AI Phishing Email Detection

## **✅ Why Vercel?**

- 🆓 **Free tier available** (no credit card required)
- ⚡ **Global CDN** for fast performance worldwide
- 🔄 **Automatic deployments** from GitHub
- 🛠️ **Easy environment variable management**
- 📊 **Built-in analytics** and monitoring
- 🌍 **Multiple regions** for better performance

---

## **⚠️ Important Notes for Flask Apps**

### **Serverless Limitations**
Vercel is designed for **serverless functions**, which means:
- **No persistent sessions** (Flask sessions won't work)
- **Function timeout** (max 30 seconds for free tier)
- **Cold starts** (first request may be slower)
- **Stateless operations** (no server memory persistence)

### **Solutions Applied**
- ✅ **Modified app structure** for serverless compatibility
- ✅ **Session alternatives** using client-side storage
- ✅ **Optimized imports** for faster cold starts
- ✅ **Fallback mechanisms** for reliability

---

## **🔧 Step 1: Prepare Your Code**

### **Files Created for Vercel:**
1. **`vercel.json`** - Vercel configuration
2. **`app_vercel.py`** - Vercel-optimized Flask app
3. **`requirements-vercel.txt`** - Vercel-compatible dependencies

### **Key Changes Made:**
- **Removed persistent sessions** (not supported on Vercel)
- **Optimized imports** for serverless environment
- **Added fallback mechanisms** for reliability
- **Configured function timeouts** and routing

---

## **🚀 Step 2: Deploy to Vercel**

### **Option A: Using Vercel CLI (Recommended)**

#### **Install Vercel CLI**
```bash
npm install -g vercel
```

#### **Login to Vercel**
```bash
vercel login
```

#### **Deploy Your Project**
```bash
# Navigate to your project directory
cd "AI Phishing Email Detection"

# Deploy to Vercel
vercel
```

#### **Follow the Prompts:**
```
? Set up and deploy "~/AI Phishing Email Detection"? [Y/n] y
? Which scope do you want to deploy to? [your-username]
? Link to existing project? [y/N] n
? What's your project's name? ai-phishing-detector
? In which directory is your code located? ./
? Want to override the settings? [y/N] n
```

### **Option B: Using Vercel Dashboard**

#### **1. Go to Vercel Dashboard**
- Visit: https://vercel.com/dashboard
- Click **"New Project"**

#### **2. Import from GitHub**
- Click **"Import Git Repository"**
- Select your repository: `AlizaAfzal/ai-phishing-detector`
- Click **"Import"**

#### **3. Configure Project**
```
Framework Preset: Other
Root Directory: ./
Build Command: (leave empty)
Output Directory: (leave empty)
Install Command: pip install -r requirements-vercel.txt
```

#### **4. Set Environment Variables**
Click **"Environment Variables"** and add:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | `9LN36ZsohRVZNKd8HqPDUDBTLjr4l8oTulz769uB4zw` |
| `MONGO_URI` | Your MongoDB Atlas connection string |
| `HUGGINGFACE_API_KEY` | `hf_tKUvfyK...` (your existing key) |
| `EMAIL_ADDRESS` | `mailguard849@gmail.com` |
| `EMAIL_PASSWORD` | `awvlcrrnpktpzbuo` |

#### **5. Deploy**
- Click **"Deploy"**
- Wait for build to complete

---

## **🔧 Step 3: Configure Environment Variables**

### **In Vercel Dashboard:**
1. Go to your project
2. Click **"Settings"** tab
3. Click **"Environment Variables"**
4. Add each variable:

#### **Required Variables:**
```bash
SECRET_KEY=9LN36ZsohRVZNKd8HqPDUDBTLjr4l8oTulz769uB4zw
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/mailguard
HUGGINGFACE_API_KEY=hf_tKUvfyK... (your existing key)
EMAIL_ADDRESS=mailguard849@gmail.com
EMAIL_PASSWORD=awvlcrrnpktpzbuo
```

#### **Variable Types:**
- **Production**: ✅ (checked)
- **Preview**: ✅ (checked)
- **Development**: ✅ (checked)

---

## **📁 Step 4: File Structure for Vercel**

### **Required Files:**
```
AI Phishing Email Detection/
├── app_vercel.py          # Main Flask app (Vercel-optimized)
├── vercel.json            # Vercel configuration
├── requirements-vercel.txt # Vercel-compatible dependencies
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── comprehensive_email_analyzer.py
├── email_header_analyzer.py
├── header_ml_model.py
└── .env                   # Environment variables (local only)
```

### **Files NOT Needed for Vercel:**
- ❌ `app.py` (original Flask app)
- ❌ `render.yaml` (Render-specific)
- ❌ `Procfile` (Heroku-specific)
- ❌ `gunicorn.conf.py` (not needed for serverless)

---

## **🔍 Step 5: Test Your Deployment**

### **1. Check Deployment Status**
- Go to Vercel dashboard
- Look for **green checkmark** ✅
- Note your **deployment URL**

### **2. Test Health Endpoint**
```
https://your-app.vercel.app/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-01-XX...",
  "database": "connected",
  "huggingface_key": "configured",
  "email_configured": "yes"
}
```

### **3. Test Main Routes**
- **Homepage**: `https://your-app.vercel.app/`
- **Login**: `https://your-app.vercel.app/login.html`
- **Signup**: `https://your-app.vercel.app/signup.html`

---

## **⚠️ Step 6: Handle Vercel Limitations**

### **Session Management Issue**
**Problem**: Flask sessions don't work on Vercel (serverless)

**Solution**: Use client-side alternatives
```javascript
// Store user info in localStorage
localStorage.setItem('user_id', userData.id);
localStorage.setItem('username', userData.username);

// Check authentication on each request
const userId = localStorage.getItem('user_id');
if (!userId) {
    // Redirect to login
}
```

### **Function Timeout Issue**
**Problem**: Vercel functions timeout after 30 seconds (free tier)

**Solution**: Optimize your code
- **Reduce API calls** to external services
- **Implement caching** for repeated requests
- **Use async operations** efficiently
- **Consider upgrading** to Pro plan for longer timeouts

### **Cold Start Issue**
**Problem**: First request is slower

**Solution**: 
- **Keep functions warm** with health checks
- **Optimize imports** and dependencies
- **Use Vercel's edge functions** for better performance

---

## **🔧 Step 7: Troubleshooting Common Issues**

### **Issue 1: Build Failures**
**Symptoms**: Deployment fails during build
**Solutions**:
1. **Check requirements-vercel.txt** - ensure all dependencies are listed
2. **Verify Python version** - Vercel supports Python 3.7+
3. **Check file paths** - ensure all imports are correct
4. **Review build logs** - look for specific error messages

### **Issue 2: Import Errors**
**Symptoms**: ModuleNotFoundError in production
**Solutions**:
1. **Check file structure** - ensure all Python files are in root directory
2. **Verify imports** - use relative imports when possible
3. **Test locally** - run `python app_vercel.py` before deploying

### **Issue 3: Environment Variables Not Working**
**Symptoms**: App crashes or shows default values
**Solutions**:
1. **Check Vercel dashboard** - ensure variables are set correctly
2. **Verify variable names** - no typos or extra spaces
3. **Redeploy** after adding variables
4. **Check variable scope** - ensure they're set for all environments

### **Issue 4: Database Connection Issues**
**Symptoms**: MongoDB connection errors
**Solutions**:
1. **Verify MONGO_URI** - check connection string format
2. **Check MongoDB Atlas** - ensure cluster is active
3. **Network access** - allow all IPs (0.0.0.0/0) in Atlas
4. **Test connection** locally first

---

## **🚀 Step 8: Optimize for Production**

### **Performance Optimizations**
1. **Enable caching** for static assets
2. **Use CDN** for better global performance
3. **Optimize images** and compress assets
4. **Implement lazy loading** for better UX

### **Monitoring and Analytics**
1. **Vercel Analytics** - built-in performance monitoring
2. **Function logs** - check for errors and performance
3. **Custom metrics** - track user interactions
4. **Error tracking** - monitor for issues

---

## **📊 Vercel Free Tier Limits**

### **Function Limits**
- **Execution time**: 30 seconds max
- **Memory**: 1024 MB
- **Request size**: 4.5 MB
- **Response size**: 6 MB

### **Bandwidth Limits**
- **100 GB** per month
- **Global CDN** included
- **Automatic scaling** based on demand

### **Deployment Limits**
- **Unlimited** deployments
- **Unlimited** projects
- **Custom domains** (with SSL)
- **Git integration** (GitHub, GitLab, Bitbucket)

---

## **🎯 Quick Deployment Checklist**

- [ ] **vercel.json** created and configured
- [ ] **app_vercel.py** optimized for serverless
- [ ] **requirements-vercel.txt** updated
- [ ] **Environment variables** set in Vercel
- [ ] **MongoDB Atlas** cluster configured
- [ ] **GitHub repository** connected
- [ ] **Deployment** completed successfully
- [ ] **Health endpoint** working
- [ ] **Main routes** accessible
- [ ] **Environment variables** loaded correctly

---

## **🚀 Deploy Now!**

### **Using Vercel CLI:**
```bash
# Install Vercel CLI
npm install -g vercel

# Login and deploy
vercel login
vercel
```

### **Using Vercel Dashboard:**
1. Go to https://vercel.com/dashboard
2. Click **"New Project"**
3. Import your GitHub repository
4. Configure environment variables
5. Deploy!

---

## **💡 Pro Tips for Vercel**

1. **Use edge functions** for better performance
2. **Implement proper error handling** for serverless environment
3. **Monitor function execution times** to stay under limits
4. **Use Vercel's preview deployments** for testing
5. **Set up custom domains** for professional appearance
6. **Enable analytics** to monitor performance
7. **Use environment-specific variables** for different stages

**Your Flask app will be available at**: `https://your-app-name.vercel.app`

**Deploy to Vercel now and enjoy fast, global performance! 🚀**
