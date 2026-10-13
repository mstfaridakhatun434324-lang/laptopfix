---
title: "How to Fix the Critical Battery Alarm Not Working on Windows 11"
slug: how-to-fix-critical-battery-alarm-not-working-on-windows-11
date: 2026-09-11
categories: ["battery"]
tags: ["battery alarm", "windows 11", "power settings"]
description: "Critical battery alarm silent on Windows 11? Fix missing low and critical battery notifications with these proven power setting repairs."
thumbnail: "/images/thumbs/how-to-fix-critical-battery-alarm-not-working-on-windows-11.webp"
faqs:
  - q: "Why doesn't my laptop warn me before the battery dies on Windows 11?"
    a: "Usually the low or critical battery notifications are turned off in the advanced power plan settings, the notification level is set too low (like 1%), or the power plan was reset by a Windows update. A corrupt battery driver or a third-party battery manager overriding Windows settings can also silence the alarms."
  - q: "What should the critical battery level be set to on Windows 11?"
    a: "Set the critical battery level to 5% and the low battery level to 10% for most laptops. If your battery is old and dies suddenly, raise the critical level to 8-10% so you get warned earlier. Never set it below 3%, because Windows may not have enough time to hibernate before the power cuts out."
  - q: "What does the critical battery action do?"
    a: "The critical battery action is what Windows does when the battery hits the critical level. The safest choice is Hibernate, which saves everything to disk and powers off. Sleep is riskier because the battery keeps draining, and Do nothing means the laptop will simply die and you may lose unsaved work."
  - q: "Can I make Windows 11 play a sound when the battery is low?"
    a: "Yes. Once the low battery notification is enabled in advanced power settings, Windows plays the default system alert sound. You can change it under Control Panel > Hardware and Sound > Sound > Sounds tab > Low Battery Alarm. Pick a louder sound file if you keep missing the default chime."
---

Your laptop is at 4%, you are mid-sentence in a document, and then the screen goes black. No warning, no chime, no popup — just a dead machine and lost work. That is the classic sign that the critical battery alarm on Windows 11 is not working.

The alarm system is supposed to give you two safety nets: a low battery notification around 10% and a critical battery action around 5% that hibernates or shuts down the laptop before power runs out. When either one goes silent, Windows never gets the chance to protect your work. Here is how to get both alarms back.

## Why this happens

- **Notifications are disabled in the power plan.** The low battery notification toggle can be off, which silences the warning popup and sound completely.
- **Battery levels are set too low.** If the critical level is at 1 or 2%, the battery may die before Windows can react, especially on an aging battery.
- **A Windows update reset the power plan.** Feature updates sometimes restore default power settings and wipe your custom battery thresholds.
- **The battery driver is glitched.** A corrupt Microsoft ACPI-Compliant Control Method Battery driver can stop Windows from reading the charge level correctly, so it never triggers the alarm.
- **A manufacturer battery tool overrides Windows.** Apps like Lenovo Vantage, Dell Power Manager, or MyASUS sometimes take over battery management and conflict with Windows' built-in alarms.
- **Power service issues.** The underlying Windows power services can stall, which breaks the whole notification chain from battery sensor to popup.

## How to fix it

Work through these in order, testing the alarm after each major change by letting the battery drain (or temporarily lowering the thresholds to a level above your current charge).

### Fix 1: Turn on the low battery notification

This single toggle is the cause in most cases I see. It lives in the advanced power settings, which most people never open.

1. Open **Control Panel** (search for it in the Start menu).
2. Go to **Hardware and Sound** > **Power Options**.
3. Next to your active plan, click **Change plan settings**.
4. Click **Change advanced power settings**.
5. Expand the **Battery** section.
6. Expand **Low battery notification** and set both **On battery** and **Plugged in** to **On**.
7. Expand **Low battery level** and set **On battery** to **10%**.
8. Click **Apply**, then **OK**.

### Fix 2: Set the critical battery level and action

The critical battery action is the real safety net. Without it, Windows just dies.

1. In the same **Advanced settings** window from Fix 1, expand **Battery** again.
2. Expand **Critical battery level** and set **On battery** to **5%**.
3. Expand **Critical battery action** and set **On battery** to **Hibernate**.
4. Leave **Plugged in** at **Do nothing** — the alarm only matters on battery power.
5. Click **Apply** and **OK**.
6. If your battery is more than two years old, consider raising the critical level to **8%**, since older batteries can drop from 5% to zero in seconds. A fresh [battery report](https://support.microsoft.com/en-us/windows) will show how much capacity your battery has lost, and you can also generate one yourself — see our guide on [generating a battery report](/articles/how-to-generate-battery-report-windows-11-powercfg/).

### Fix 3: Repair the alarm with powercfg commands

If the GUI settings look right but the alarm still stays silent, force the values directly with `powercfg`.

1. Right-click **Start** and choose **Terminal (Admin)**.
2. First, check the current values: `powercfg /query SCHEME_CURRENT SUB_BATTERY`
3. Set the critical level on battery to 5%: `powercfg /SETDCVALUEINDEX SCHEME_CURRENT SUB_BATTERY BATLEVELCRIT 5`
4. Set the low level on battery to 10%: `powercfg /SETDCVALUEINDEX SCHEME_CURRENT SUB_BATTERY BATLEVELLOW 10`
5. Set the critical action to hibernate (value 2): `powercfg /SETDCVALUEINDEX SCHEME_CURRENT SUB_BATTERY BATACTIONCRIT 2`
6. Make the active plan pick up the change: `powercfg /SETACTIVE SCHEME_CURRENT`
7. Reopen the advanced power settings and confirm the numbers stuck.

### Fix 4: Reinstall the battery driver

A bad battery driver can break the communication between the battery hardware and the alarm system.

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries**.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**.
4. If you see **Microsoft AC Adapter**, leave it alone — only remove the battery entry.
5. Click **Action** > **Scan for hardware changes**. Windows reinstalls the driver automatically.
6. Restart the laptop, then check that the battery percentage still reads correctly in the taskbar.

If Windows cannot see the battery at all after this, follow our deeper guide on a [battery not detected in Windows 11](/articles/laptop-battery-not-detected-windows-11/).

### Fix 5: Restore the power plan defaults

A damaged power plan can ignore the settings you apply. Restoring defaults gives you a clean slate.

1. Open **Terminal (Admin)**.
2. Restore the current plan: `powercfg /restoredefaultschemes`
3. Set the balanced plan active: `powercfg /SETACTIVE 381b4222-f694-41f0-9685-ff5bb260df2e`
4. Go back to **Change advanced power settings** and redo Fixes 1 and 2 on the fresh plan.
5. If you use a custom plan, recreate it afterward rather than trying to repair the old one.

### Fix 6: Check for conflicts with manufacturer battery apps

OEM power tools sometimes fight Windows over battery control.

1. Open your manufacturer's app — Lenovo Vantage, Dell Power Manager, MyASUS, or HP's power tool.
2. Look for any battery threshold, alarm, or "battery lifespan" setting.
3. Turn off any feature that manages charge limits or notifications if you want Windows to handle alarms (or keep the OEM tool in charge and disable the Windows ones — never both at once).
4. In **Settings** > **Apps** > **Installed apps**, remove any duplicate or outdated battery utilities.
5. Restart and test the alarm again.

### Fix 7: Check the Windows notification system

Even with the alarm configured, a broken notification pipeline hides the popup.

1. Go to **Settings** > **System** > **Notifications**.
2. Make sure **Notifications** is turned on and **Do not disturb** is off.
3. Open **Control Panel** > **Hardware and Sound** > **Sound** > **Sounds** tab.
4. In the list, find **Low Battery Alarm** and **Critical Battery Alarm**, click **Test** on each to confirm sound plays.
5. If the entries are missing, run `sfc /scannow` in an admin Terminal to repair system files, then restart.
6. As a final check, open **Event Viewer** > **Windows Logs** > **System** and filter by source **Kernel-Power** — you should see battery level events logged as the charge drops.

## Closing

Nine times out of ten, this is just the low battery notification toggle being off or the critical level set too aggressively. Once you set 10% for low, 5% for critical, and Hibernate as the critical action, Windows 11 will warn you in time and save your work automatically.
