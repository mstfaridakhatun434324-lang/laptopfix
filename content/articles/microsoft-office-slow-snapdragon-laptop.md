---
title: "How to Fix Microsoft Office Running Slow on a Snapdragon Laptop"
slug: microsoft-office-slow-snapdragon-laptop
date: 2026-10-20
categories: ["ai-pc"]
tags: ["microsoft office", "snapdragon laptop", "office slow", "troubleshooting", "ai pc", "windows 11 arm"]
description: "Microsoft Office crawling on your Snapdragon laptop? Fix slow Word, Excel, and Outlook with these Windows 11 on ARM performance troubleshooting steps."
thumbnail: "/images/thumbs/microsoft-office-slow-snapdragon-laptop.webp"
faqs:
  - q: "Does Microsoft Office run natively on Snapdragon laptops?"
    a: 'Yes. Microsoft 365 apps including Word, Excel, PowerPoint, and Outlook ship as native ARM64 builds on Windows 11 on ARM. If Office feels slow, you may be running an older x64 install under emulation, or a setting like hardware graphics acceleration is misbehaving. Both are fixable without buying anything.'
  - q: "Why is Excel so slow with large spreadsheets on my Snapdragon laptop?"
    a: 'Large workbooks stress memory and recalculation, and an emulated x64 Excel build makes it much worse. Confirm you have the native ARM64 build, switch calculation to manual for huge files, and close other heavy apps. Outdated graphics drivers can also slow chart rendering specifically.'
  - q: "Will reinstalling Office make it faster on ARM?"
    a: 'Only if the reinstall fixes the underlying cause. A clean install helps when you are stuck on an emulated x64 build or have corrupted Office files, because the installer then picks the correct native ARM64 version. If your build is already native, look at add-ins, antivirus scanning, and Windows performance settings instead.'
  - q: "Why is Outlook search so slow on my Snapdragon laptop?"
    a: 'Outlook search depends on Windows Search indexing, which can fall behind on a new laptop or after a big mailbox sync. Let indexing finish, check that Outlook data files are included in indexed locations, and rebuild the index if results stay slow. Running Outlook under emulation instead of native ARM64 also drags search down.'
---

Microsoft Office should fly on a Snapdragon laptop. Snapdragon X chips are fast, efficient processors, and Microsoft ships native ARM64 versions of Word, Excel, PowerPoint, and Outlook for Windows 11 on ARM. On paper, documents should open instantly and scrolling should be smooth.

In practice, plenty of users report the opposite: Word stutters while typing, Excel crawls through large spreadsheets, and Outlook searches slowly. It is tempting to blame the ARM chip, but the processor is rarely the problem. Slow Office on Snapdragon machines almost always comes from the wrong Office build, a misbehaving add-in, or Windows settings that hobble performance.

This guide diagnoses the real causes and fixes them in order. Start at the top, verify each fix, and stop when Office feels fast again.

## Why this happens

- **Emulated x64 Office build:** an older x64 install under emulation is much slower than native ARM64, especially in Excel and Outlook.
- **Hardware graphics acceleration glitches:** Office uses the GPU for smooth scrolling. A buggy graphics driver turns this feature into a slowdown.
- **Heavy or broken add-ins:** third-party Outlook and Excel add-ins load at startup and can add seconds to every launch.
- **Antivirus real-time scanning:** aggressive scanning of Office documents and the Outlook data file adds latency to every open and save.
- **Windows Search index incomplete:** Outlook search crawls when the index is still building or has been corrupted.
- **Power plan throttling the CPU:** battery-saver modes keep the Snapdragon chip at low clocks during Office work.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm you are running native ARM64 Office

Native ARM64 Office runs dramatically better on Snapdragon laptops than the x64 build under emulation. You might have the emulated build if Office came from an old offline installer or migrated from an Intel machine. Checking takes a minute. Reinstalling picks the correct architecture automatically.

1. In Word, go to File > Account > About Word and read the version line.
2. If it is the x64 build, uninstall Office from Settings > Apps > Installed apps.
3. Restart, then reinstall from your Microsoft 365 account page.
4. Recheck About Word and confirm the native ARM64 build is installed.

### Fix 2: Disable hardware graphics acceleration

Office's hardware graphics acceleration should smooth scrolling and animations, but on some Snapdragon graphics drivers it does the opposite. Typing lag in Word and choppy scrolling are the classic symptoms. Disabling it forces CPU rendering. That is often faster when the GPU driver is at fault.

1. In Word or Excel, go to File > Options > Advanced.
2. Scroll to Display and check "Disable hardware graphics acceleration".
3. Click OK, close all Office apps, then reopen Word.
4. Test typing and scrolling to confirm the improvement.

### Fix 3: Strip out slow add-ins

Add-ins are a silent performance killer. Every COM add-in in Outlook or Excel loads at startup, and a single outdated one can add seconds to launch times. Users often migrate add-ins from old Intel machines without checking compatibility. Disable them in bulk, then re-enable only what you need.

1. In Outlook or Excel, go to File > Options > Add-ins.
2. Set Manage to "COM Add-ins", click Go, and uncheck everything.
3. Restart the Office app and check whether it is fast now.
4. Re-enable add-ins one at a time, restarting between each.
5. Leave the add-in that reintroduces the slowdown disabled or update it.

### Fix 4: Update Windows, Office, and graphics drivers

ARM platform support improves constantly. Microsoft and driver releases have fixed Office-specific slowdowns over time. An outdated Windows 11 build, an old Office channel, or a stale graphics driver can each cause the symptoms you are seeing. Use the official [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) if you ever need clean installation media, and [Microsoft support](https://support.microsoft.com/en-us/windows) for update troubleshooting.

1. In Settings > Windows Update, install every update and restart.
2. In any Office app, go to File > Account > Update Options > Update Now.
3. Update your graphics driver from your laptop maker's support page.
4. Restart and test Word, Excel, and Outlook.

### Fix 5: Tune antivirus and Windows Search indexing

Security software and search indexing both touch every Office file you open. Real-time antivirus scanning of large Outlook data files adds latency, and a broken Windows Search index makes Outlook search painfully slow. Exclude trusted Office data files from scanning and let indexing finish. If your browser is also misbehaving, see our guide to [Chrome ARM64 crashing on Windows](/articles/chrome-arm64-crashing-windows/) for the same diagnostic approach.

1. Let a new laptop finish its first full Windows Search index before judging Outlook search.
2. In Indexing Options, confirm Outlook and your document folders are included.
3. If search stays slow, use Advanced > Rebuild to recreate the index overnight.
4. In antivirus settings, add Outlook .ost/.pst files as trusted exclusions.
5. Restart Outlook and test search on a common term.

### Fix 6: Switch to a performance power plan

Snapdragon laptops are tuned for battery life, and aggressive power saving can keep the chip at low clocks during Office work. Excel recalculations and large Word documents need burst performance that battery-saver modes withhold. Switching to Best Performance while plugged in costs little and can transform responsiveness. This matters more than the chip tier — even the [Snapdragon X Plus vs X Elite](/articles/snapdragon-x-plus-vs-x-elite/) gap is smaller than the gap between power modes.

1. Open Settings > System > Power & battery.
2. Set Power mode to "Best performance" while plugged in.
3. Set the on-battery mode to "Balanced" to protect battery life.
4. Check your laptop maker's app for extra performance or quiet modes.
5. Retest Excel recalculation and Word scrolling.

## Closing

Slow Office on a Snapdragon laptop is almost never the chip's fault. Verify the native ARM64 build, tame graphics acceleration and add-ins, keep updates current, and give the processor room to boost. Work through these six fixes and Word, Excel, and Outlook should feel as fast as the hardware promises. If AI features are also acting up, check our guide to [Snapdragon X Elite NPU driver issues](/articles/snapdragon-x-elite-npu-driver-issues/) next.
