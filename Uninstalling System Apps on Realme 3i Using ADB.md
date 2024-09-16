# Uninstalling System Apps on Realme 3i Using ADB

This guide will walk you through the process of uninstalling default system apps, like the Music app, from your Realme 3i using ADB (Android Debug Bridge).

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setting Up ADB](#setting-up-adb)
3. [Enabling Developer Options & USB Debugging](#enabling-developer-options--usb-debugging)
4. [Connecting the Device to ADB](#connecting-the-device-to-adb)
5. [Uninstalling the Music App](#uninstalling-the-music-app)
6. [Troubleshooting ADB Connection Issues](#troubleshooting-adb-connection-issues)

---

## Prerequisites
Before you start, make sure you have the following:
- A **Windows PC** or **Mac** with **ADB** installed.
- **USB cable** to connect your Realme 3i to the PC.
- Installed **Realme USB drivers** (for Windows) or appropriate drivers.

---

## Setting Up ADB

1. **Download ADB**:  
   Download the **Android SDK Platform Tools** from the [official website](https://developer.android.com/studio/releases/platform-tools) and extract it to a convenient location on your PC.

2. **Add ADB to System Path (Optional)**:  
   To make ADB accessible from anywhere, add it to your system's environment variables:
   - **Windows**:
     - Right-click on **This PC** > **Properties**.
     - Click **Advanced System Settings** > **Environment Variables**.
     - Under **System Variables**, select **Path** > **Edit** > **New**. Add the path where `adb.exe` is located (e.g., `C:\platform-tools`).
   - **Mac/Linux**:  
     Add the ADB folder path to your `.bash_profile` or `.zshrc`:
     ```bash
     export PATH=$PATH:/path/to/adb
     ```

---

## Enabling Developer Options & USB Debugging

1. **Enable Developer Mode**:
   - Go to **Settings** > **About Phone** > **Version**.
   - Tap **Build Number** 7 times until you see a message saying **"You are now a developer!"**.

2. **Enable USB Debugging**:
   - Go to **Settings** > **Additional Settings** > **Developer Options**.
   - Scroll down and enable **USB Debugging**.

---

## Connecting the Device to ADB

1. **Connect your phone** to your computer using a USB cable.
   
2. **Set USB Mode to File Transfer (MTP)**:
   - Swipe down from the top of the screen and tap the **USB options** notification.
   - Select **File Transfer** or **MTP** mode.

3. **Authorize the Connection**:
   - When you connect your phone, a pop-up may appear asking you to **Allow USB Debugging**.
   - Tap **Allow** and check **Always allow from this computer**.

---

## Uninstalling the Music App

1. **Open Command Prompt/PowerShell**:
   - Navigate to the folder where you extracted the **ADB tools**.
   - Hold **Shift + Right-click** and choose **Open PowerShell window here** (or Command Prompt).

2. **Check if ADB Detects Your Device**:
   - Run the following command:
     ```bash
     adb devices
     ```
   - If your device is listed, you're good to go! If not, refer to the [Troubleshooting ADB Connection Issues](#troubleshooting-adb-connection-issues) section.

3. **List Installed Apps**:
   - Run the following command to get a list of all installed apps (packages):
     ```bash
     adb shell pm list packages
     ```

4. **Find the Music App**:
   - Look for the **Music app** package name, which should be something like `com.realme.music`.

5. **Uninstall the Music App**:
   - Use the following command to uninstall the app:
     ```bash
     adb shell pm uninstall -k --user 0 com.realme.music
     ```
   - Replace `com.realme.music` with the exact package name if different.

---

## Troubleshooting ADB Connection Issues

If ADB shows **"no devices/emulators found"**, follow these steps:

### 1. **Check USB Debugging**
- Ensure that **USB Debugging** is enabled under **Developer Options**.

### 2. **Set USB Mode to File Transfer**
- Make sure your phone is in **File Transfer (MTP)** mode. Swipe down the notification panel and tap the USB connection mode to verify.

### 3. **Install or Update USB Drivers (Windows)**
- Download and install **Realme USB drivers** from the official Realme website.
- Go to **Device Manager** and ensure there are no errors under **Portable Devices**.

### 4. **Restart ADB Server**
- Run the following commands in Command Prompt/PowerShell:
   ```bash
   adb kill-server
   adb start-server
