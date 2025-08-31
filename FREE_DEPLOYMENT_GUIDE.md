# 🆓 Free Render Deployment Guide (No Credit Card Required)

## **✅ What You Can Deploy for FREE:**

### **Web Service (Your Flask App)**
- ✅ **Free Plan Available**
- ✅ **No Credit Card Required**
- ✅ **512 MB RAM, 0.1 CPU**
- ✅ **750 hours/month** (enough for 24/7 operation)
- ✅ **Sleeps after 15 minutes of inactivity**

### **❌ What Requires Payment:**
- ❌ **MongoDB Database** (use MongoDB Atlas free tier instead)
- ❌ **Background Workers**
- ❌ **Cron Jobs**
- ❌ **Custom Domains** (on static sites)

---

## **🚀 Step-by-Step Free Deployment**

### **Step 1: Prepare Your Code**
Your code is already ready! The updated `render.yaml` now only deploys the web service.

### **Step 2: Deploy to Render**

#### **Option A: Using render.yaml (Recommended)**
1. **Go to Render Dashboard**: https://dashboard.render.com
2. **Click "New +"**
3. **Select "Blueprint"**
4. **Connect your GitHub repository**
5. **Select the repository**
6. **Click "Apply"**
7. **Render will automatically detect render.yaml**

#### **Option B: Manual Web Service**
1. **Go to Render Dashboard**
2. **Click "New +"**
3. **Select "Web Service"**
4. **Connect GitHub repository**
5. **Configure:**
   ```
   Name: phishing-detector
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   Plan: Free
   ```

### **Step 3: Set Environment Variables**
In Render dashboard, go to **Environment** tab and add:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | `9LN36ZsohRVZNKd8HqPDUDBTLjr4l8oTulz769uB4zw` |
| `MONGO_URI` | Your MongoDB Atlas connection string |
| `HUGGINGFACE_API_KEY` | `hf_tKUvfyK...` (your existing key) |
| `EMAIL_ADDRESS` | `mailguard849@gmail.com` |
| `EMAIL_PASSWORD` | `awvlcrrnpktpzbuo` |

### **Step 4: Use MongoDB Atlas (Free)**
Since Render's free plan doesn't include databases:

1. **Go to MongoDB Atlas**: https://cloud.mongodb.com
2. **Create free cluster** (M0 tier)
3. **Set up database user**
4. **Get connection string**
5. **Add to MONGO_URI environment variable**

---

## **🔧 Troubleshooting Free Plan Issues**

### **Issue: "Insufficient Funds" Error**
**Cause**: You're trying to deploy a database or paid service
**Solution**: 
- Deploy only the **Web Service**
- Use **MongoDB Atlas** for database
- Make sure you select **Free plan**

### **Issue: "Plan Not Available"**
**Cause**: You might be in a region where free plan isn't available
**Solution**:
- Try different regions
- Contact Render support

### **Issue: App Sleeps After Inactivity**
**Cause**: This is normal for free plan
**Solution**:
- First request after sleep takes 30-60 seconds
- Consider upgrading for production use

---

## **📋 Free Plan Limitations**

### **Performance:**
- **512 MB RAM**
- **0.1 CPU**
- **Sleeps after 15 minutes**
- **750 hours/month**

### **Features:**
- ✅ **Custom domains** (with paid plan)
- ✅ **SSL certificates**
- ✅ **Environment variables**
- ✅ **GitHub integration**
- ✅ **Automatic deployments**

---

## **🎯 Quick Deployment Checklist**

- [ ] **render.yaml** updated (no database section)
- [ ] **GitHub repository** connected
- [ ] **MongoDB Atlas** cluster created
- [ ] **Environment variables** set in Render
- [ ] **Free plan** selected
- [ ] **Deployment** started

---

## **🚀 Deploy Now!**

1. **Push your updated code to GitHub**
2. **Go to Render Dashboard**
3. **Create new Web Service**
4. **Select Free plan**
5. **Set environment variables**
6. **Deploy!**

**Your app will be available at**: `https://your-app-name.onrender.com`

---

## **💡 Pro Tips for Free Plan**

1. **Monitor usage** - Stay under 750 hours/month
2. **Optimize startup** - First request is slow
3. **Use health endpoint** - `/health` to check status
4. **Set up monitoring** - Check logs regularly
5. **Consider upgrade** - For production use

**You can deploy your app completely free! No credit card needed! 🎉**
