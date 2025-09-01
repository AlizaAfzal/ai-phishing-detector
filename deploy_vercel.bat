@echo off
echo 🚀 Vercel Deployment Script for AI Phishing Email Detection
echo ============================================================
echo.

echo 📋 Checking prerequisites...
echo.

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js is not installed!
    echo Please install Node.js from: https://nodejs.org/
    echo.
    pause
    exit /b 1
)

echo ✅ Node.js found: 
node --version

REM Check if npm is available
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ npm is not available!
    echo Please ensure npm is properly installed with Node.js
    echo.
    pause
    exit /b 1
)

echo ✅ npm found:
npm --version

echo.
echo 🔧 Installing Vercel CLI globally...
npm install -g vercel

if %errorlevel% neq 0 (
    echo ❌ Failed to install Vercel CLI!
    echo Please check your internet connection and try again
    echo.
    pause
    exit /b 1
)

echo ✅ Vercel CLI installed successfully!

echo.
echo 🔐 Logging in to Vercel...
vercel login

if %errorlevel% neq 0 (
    echo ❌ Failed to login to Vercel!
    echo Please check your credentials and try again
    echo.
    pause
    exit /b 1
)

echo ✅ Logged in to Vercel successfully!

echo.
echo 🚀 Deploying to Vercel...
echo.
echo 📝 Important Notes:
echo - Make sure you have set environment variables in Vercel dashboard
echo - Ensure MongoDB Atlas cluster is running
echo - Check that all required files are present
echo.

vercel

if %errorlevel% neq 0 (
    echo ❌ Deployment failed!
    echo Please check the error messages above
    echo.
    pause
    exit /b 1
)

echo.
echo 🎉 Deployment completed successfully!
echo.
echo 📋 Next steps:
echo 1. Check your Vercel dashboard for the deployment URL
echo 2. Test the health endpoint: https://your-app.vercel.app/health
echo 3. Verify all routes are working
echo 4. Test email analysis functionality
echo.
echo 🔗 Your app will be available at: https://your-app-name.vercel.app
echo.

pause
