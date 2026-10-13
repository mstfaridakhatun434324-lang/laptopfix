---
title: "How to Fix \"No Battery Detected\" After a Windows Update"
slug: how-to-fix-no-battery-detected-after-windows-update
date: 2026-09-16
categories: ["battery"]
tags: ["no battery detected", "Windows update", "battery driver", "troubleshooting"]
description: "Windows update left you with \"no battery detected\"? Rebuild the battery driver stack, roll back the bad driver, and get the battery recognized again."
thumbnail: "/images/thumbs/how-to-fix-no-battery-detected-after-windows-update.webp"
faqs:
  - q: "Why does Windows say no battery detected after an update?"
    a: "The update replaced or corrupted the battery driver stack — usually the Microsoft ACPI-Compliant Control Method Battery driver or the underlying chipset/ACPI drivers. Windows can no longer talk to the battery's controller, so it reports the battery as missing. The battery itself is almost always fine; it's the communication that broke."
  - q: "Will I lose my files fixing this?"
    a: "No. Every fix here — driver reinstalls, EC resets, driver rollbacks, even uninstalling the update — touches drivers and settings only, not your data. Still, the usual advice applies: if the laptop is already open for another reason, backups are never a bad idea. But nothing in this guide deletes personal files."
  - q: "What if the battery isn't detected even in the BIOS?"
    a: "Then it's not a Windows problem — it's hardware or firmware. Check the BIOS battery information page: if the BIOS doesn't see the battery either, suspect a loose internal cable, a failed battery, or a firmware issue. The Windows fixes below won't help until the BIOS recognizes the battery."
  - q: "How do I stop Windows from breaking the battery driver again?"
    a: "After fixing it, you can pause updates briefly, but the better long-term move is keeping the manufacturer's chipset drivers current — install them from the manufacturer's support site rather than relying solely on Windows Update. Mismatches between new Windows builds and old chipset drivers cause most recurrences."
---

"No battery detected" after a Windows update is a special kind of frustrating: the battery was there yesterday, the update is the only thing that changed, and now the icon shows a red X as if the battery vanished. It didn't vanish. In the overwhelming majority of cases the update broke the driver conversation between Windows and the battery — the hardware is fine, the software just forgot how to see it. Here's how to restore the conversation, simplest fix first.

## Why this happens

- **Battery driver replaced:** The update installed a new or generic ACPI battery driver that doesn't talk to your battery's controller correctly.
- **Driver corruption mid-update:** The update process damaged the existing driver files, leaving a half-installed driver behind.
- **Chipset/ACPI driver mismatch:** Windows updated but the older chipset drivers can't mediate the new power-management interface.
- **Battery device disabled:** The update left the battery device disabled in Device Manager — present but switched off.
- **Fast Startup stale state:** The hybrid shutdown preserved a broken driver state across reboots, so the problem survives restarts.
- **Firmware interface change:** Major feature updates change how Windows talks to firmware, and the battery is the first thing to notice.

## How to fix it

Work through these in order, checking whether the battery is detected after each one before moving on.

### Fix 1: Do a true full shutdown first

1. This sounds too simple, but try it: hold **Shift** while clicking **Shut down** in the Start menu — this bypasses Fast Startup and forces a genuine cold boot.
2. Unplug the charger, wait 30 seconds, plug back in, and power on.
3. Check the battery icon. Fast Startup preserves driver state across normal "shutdowns," so a broken battery driver can survive a dozen reboots until you do a real one.
4. If the battery appears, the fix is done — but consider disabling Fast Startup permanently (Fix 7) so it doesn't recur.

### Fix 2: Check Device Manager for the battery's status

1. Press **Win + X** and open **Device Manager**.
2. Expand **Batteries** — look for **Microsoft ACPI-Compliant Control Method Battery** and the AC adapter entry.
3. If you see a yellow warning icon, that's your culprit. If the battery entries are missing entirely, click **View > Show hidden devices** — grayed-out entries mean the device is present but not active.
4. Right-click any battery entry: if you see **Enable device**, click it — the update may have simply disabled it.

### Fix 3: Reinstall the battery drivers

1. In **Device Manager > Batteries**, right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**. Do the same for the AC adapter entry.
2. Shut down fully (Shift + Shut down), unplug the charger, and wait 60 seconds.
3. Plug in and power on — Windows detects the battery hardware and installs fresh drivers on boot.
4. Give it a minute after login, then check the battery icon. This resolves most post-update detection failures. The general case is covered in our [laptop battery not detected guide](/articles/laptop-battery-not-detected-windows-11/).

### Fix 4: Roll back the driver the update installed

1. In **Device Manager > Batteries**, right-click the battery driver and choose **Properties**.
2. Go to the **Driver** tab — if **Roll Back Driver** is clickable, the update changed this driver, and rolling back restores the working one.
3. Also check **System devices** for ACPI/chipset entries with recent driver dates and roll those back too.
4. Restart with a full shutdown afterward and recheck. If rollback isn't available, the update didn't keep the old driver — continue to Fix 5.

### Fix 5: Update chipset drivers from the manufacturer

1. The deeper cause of many detection failures: Windows is new, but the chipset drivers mediating battery communication are old.
2. Go to your manufacturer's support site (Dell, HP, Lenovo) and download the latest **chipset** and **power management** drivers for your exact model.
3. Install them, then do a full shutdown and cold boot.
4. Manufacturer drivers are written against your specific firmware; the generic ones Windows Update prefers are the ones that break detection.

### Fix 6: Uninstall the problematic Windows update

1. Go to **Settings > Windows Update > Update history > Uninstall updates**.
2. Find the most recent update — particularly driver updates or cumulative updates dated when the problem started.
3. Uninstall it and restart with a full shutdown.
4. If the battery returns, you've confirmed the update as the cause. Pause updates for a week or two (**Settings > Windows Update > Pause updates**) while the manufacturer or Microsoft ships a fix — and grab the manual driver from [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if you need a specific fixed version later.

### Fix 7: Disable Fast Startup and reset the EC

1. Go to **Control Panel > Power Options > Choose what the power buttons do**, click **Change settings that are currently unavailable**, and uncheck **Turn on fast startup**.
2. Shut down fully, unplug, and hold the **power button for 30 seconds** to reset the embedded controller.
3. Plug in, boot, and check detection. This clears both the stale Windows driver state and any confused controller state in one pass.
4. Leave Fast Startup off if the problem ever recurs — the boot-time savings aren't worth a disappearing battery.

### Fix 8: Check the BIOS sees the battery

1. Restart and enter BIOS Setup (**F2**, **Del**, or **F10**).
2. Find the battery information page — if the BIOS doesn't detect the battery either, no Windows fix will help.
3. If the BIOS sees it but Windows doesn't after all the above, run the manufacturer's diagnostics (Dell **F12 > Diagnostics**, Lenovo Vantage hardware scan) and consider a BIOS update.
4. If neither BIOS nor Windows sees it, suspect hardware: a loose internal cable or a failed battery. Our [post-update detection guide](/articles/how-to-fix-battery-not-detected-on-laptop-after-windows-11-update/) covers the hardware side in detail.

## Closing

"No battery detected" after an update is Windows losing the thread, not the battery dying — the cold-boot test and driver reinstall prove that in most cases within fifteen minutes. Work the list in order, and note which step fixed it: if it was a driver rollback or an update uninstall, keep your manufacturer's chipset drivers current going forward, because that's the mismatch that invites a repeat performance next update cycle. The battery was there all along; Windows just needed to be reintroduced.

Microsoft documents driver and update recovery at the [Windows support hub](https://support.microsoft.com/en-us/windows).
