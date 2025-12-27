# Quick Start Script for Chatterbox TTS Streamlit UI
# This script helps you get started with the installation

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Chatterbox TTS - Installation Helper" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is available
Write-Host "[1/5] Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install Python 3.10 or higher." -ForegroundColor Red
    exit 1
}

# Check if conda is available
Write-Host ""
Write-Host "[2/5] Checking for Conda..." -ForegroundColor Yellow
try {
    $condaVersion = conda --version 2>&1
    Write-Host "✓ Found: $condaVersion" -ForegroundColor Green
    $useConda = $true
} catch {
    Write-Host "! Conda not found (optional)" -ForegroundColor Yellow
    $useConda = $false
}

# Check for CUDA
Write-Host ""
Write-Host "[3/5] Checking for NVIDIA GPU..." -ForegroundColor Yellow
try {
    nvidia-smi | Out-Null
    Write-Host "✓ NVIDIA GPU detected - CUDA support available" -ForegroundColor Green
    $hasCuda = $true
} catch {
    Write-Host "! No NVIDIA GPU detected - will use CPU mode (slower)" -ForegroundColor Yellow
    $hasCuda = $false
}

# Check for Visual C++ Build Tools
Write-Host ""
Write-Host "[4/5] Checking for Visual C++ Build Tools..." -ForegroundColor Yellow
$vsWhere = "${env:ProgramFiles(x86)}\Microsoft Visual Studio\Installer\vswhere.exe"
if (Test-Path $vsWhere) {
    Write-Host "✓ Visual C++ Build Tools found" -ForegroundColor Green
    $hasBuildTools = $true
} else {
    Write-Host "✗ Visual C++ Build Tools NOT found" -ForegroundColor Red
    Write-Host "  This is required to install chatterbox-tts on Windows" -ForegroundColor Red
    Write-Host "  Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/" -ForegroundColor Yellow
    $hasBuildTools = $false
}

Write-Host ""
Write-Host "[5/5] Installation Options:" -ForegroundColor Yellow
Write-Host ""

if ($hasBuildTools) {
    Write-Host "✓ You have all prerequisites! Run these commands:" -ForegroundColor Green
    Write-Host ""
    Write-Host "  cd `"$PSScriptRoot`"" -ForegroundColor Cyan
    if ($useConda) {
        Write-Host "  conda install -y numpy scipy" -ForegroundColor Cyan
    }
    Write-Host "  pip install -e ./chatterbox" -ForegroundColor Cyan
    Write-Host "  streamlit run app.py" -ForegroundColor Cyan
} else {
    Write-Host "⚠ Missing Prerequisites:" -ForegroundColor Red
    Write-Host ""
    Write-Host "1. Install Visual C++ Build Tools:" -ForegroundColor Yellow
    Write-Host "   https://visualstudio.microsoft.com/visual-cpp-build-tools/" -ForegroundColor Cyan
    Write-Host "   → Select 'Desktop development with C++'" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "2. After installing build tools, run:" -ForegroundColor Yellow
    Write-Host "   cd `"$PSScriptRoot`"" -ForegroundColor Cyan
    if ($useConda) {
        Write-Host "   conda install -y numpy scipy" -ForegroundColor Cyan
    }
    Write-Host "   pip install -e ./chatterbox" -ForegroundColor Cyan
    Write-Host "   streamlit run app.py" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "For detailed instructions, see:" -ForegroundColor White
Write-Host "  - README.md (usage guide)" -ForegroundColor Cyan
Write-Host "  - INSTALL.md (installation guide)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Offer to open INSTALL.md
$response = Read-Host "Would you like to open INSTALL.md now? (y/n)"
if ($response -eq "y" -or $response -eq "Y") {
    notepad.exe "INSTALL.md"
}
