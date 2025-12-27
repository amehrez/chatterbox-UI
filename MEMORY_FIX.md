# 🔧 Fixing Memory Issues - Windows Paging File Guide

## Problem: "The paging file is too small" Error

This error occurs when Windows runs out of virtual memory while loading the AI models. The Chatterbox TTS models are large and need sufficient virtual memory to run.

---

## ✅ Solution: Increase Windows Paging File

Follow these steps to increase your virtual memory (paging file):

### Step 1: Open System Settings
1. Press **Windows key**
2. Type: `View advanced system settings`
3. Click on the result

### Step 2: Access Performance Settings
1. In the "System Properties" window
2. Under the "Advanced" tab
3. Click **Settings** button under "Performance"

### Step 3: Change Virtual Memory
1. Go to the **Advanced** tab
2. Under "Virtual memory", click **Change...**

### Step 4: Configure Custom Size
1. **Uncheck** "Automatically manage paging file size for all drives"
2. Select your **C:** drive (or drive with most space)
3. Select **Custom size** radio button
4. Enter these values:
   - **Initial size**: `16000` MB (16 GB)
   - **Maximum size**: `32000` MB (32 GB)
5. Click **Set** button
6. Click **OK** on all windows
7. **Restart your computer** for changes to take effect

### Visual Guide:
```
System Properties
└─ Advanced tab
   └─ Performance > Settings
      └─ Advanced tab
         └─ Virtual memory > Change
            ├─ ☐ Automatically manage (UNCHECK THIS)
            ├─ Select C: drive
            ├─ ⦿ Custom size
            ├─ Initial size: 16000
            ├─ Maximum size: 32000
            └─ Click "Set" then "OK"
```

---

## 🚀 After Restarting

Once you've restarted your computer:

1. Navigate to your project folder:
```bash
cd "c:/Users/ahmed/OneDrive - ashghal.gov.qa/CODING/Chatterbox TTS"
```

2. Run Streamlit:
```bash
streamlit run app.py
```

3. Open **http://localhost:8501** (or the port shown)

4. Try generating speech again - the memory error should be resolved!

---

## 💡 Alternative Solutions

If you still have issues after increasing the paging file:

### Option 1: Use Turbo Model (Recommended)
- **Chatterbox-Turbo** is the most memory-efficient model
- Uses only ~350M parameters vs larger models
- Select "Chatterbox-Turbo" in the sidebar
- Still provides excellent quality with emotional tags

### Option 2: Close Other Applications
- Close web browsers with many tabs
- Close other memory-intensive applications
- Close unnecessary background processes

### Option 3: Restart Streamlit
Sometimes memory gets fragmented. Try:
```bash
# Stop streamlit (Ctrl+C in terminal)
# Then restart:
streamlit run app.py
```

### Option 4: Check System Requirements
Minimum requirements:
- **RAM**: 8GB minimum, 16GB+ recommended
- **Virtual Memory**: 16GB+ (as configured above)
- **Disk Space**: 10GB free for models
- **GPU** (optional): 4GB+ VRAM for faster generation

---

## 🎯 Verification

To check if your paging file is configured correctly:

1. Open **Task Manager** (Ctrl+Shift+Esc)
2. Go to **Performance** tab
3. Click **Memory**
4. Check "Committed" memory - it should show a large value (e.g., 32/48 GB)

---

## 📊 What the Updated App Now Does

The optimized app now includes:

✅ **Automatic memory cleanup** after each generation
✅ **GPU cache clearing** before and after model use
✅ **Garbage collection** to free unused memory
✅ **Better error messages** with specific fix instructions
✅ **Memory tips** in the sidebar
✅ **Always-visible language selector** (you asked for this!)
✅ **GPU memory info** displayed in sidebar

---

## 🆕 UI Improvements

1. **Language Selector**: Now always visible in sidebar (under "🌍 Language Settings")
   - Shows for all models
   - Clearly indicates when it's active (Multilingual model)

2. **Memory Tips Section**: New sidebar section with quick troubleshooting

3. **System Info**: Shows GPU memory and device info

4. **Better Error Messages**: Specific instructions for common errors

---

## Still Having Issues?

If problems persist:

1. Check the app sidebar for "⚠️ Memory Tips"
2. Verify paging file settings (should show 16-32 GB)
3. Try Turbo model first
4. Restart your computer
5. Make sure no other heavy apps are running

**The app is now optimized and ready to use!** 🎉
