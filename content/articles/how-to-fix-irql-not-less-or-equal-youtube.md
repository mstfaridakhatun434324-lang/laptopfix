---
title: "How to Fix IRQL_NOT_LESS_OR_EQUAL When Watching YouTube"
slug: how-to-fix-irql-not-less-or-equal-youtube
date: 2026-09-28
categories: ["windows-errors"]
tags: ["bsod", "irql-not-less-or-equal", "youtube"]
description: "Blue screen with IRQL_NOT_LESS_OR_EQUAL while watching YouTube? Fix the browser, GPU, and driver causes with these steps."
thumbnail: "/images/thumbs/how-to-fix-irql-not-less-or-equal-youtube.webp"
faqs:
  - q: "Why does YouTube trigger IRQL_NOT_LESS_OR_EQUAL?"
    a: "YouTube stresses a specific chain: browser hardware acceleration, the GPU driver, and network drivers all working at once. A bug or corruption in any one of them — most often the GPU or network driver — crashes the system, and video playback is simply the workload that exposes it."
  - q: "Is my browser the problem?"
    a: "Sometimes. A corrupted browser profile or a bad GPU-acceleration interaction can trigger driver bugs. Disabling hardware acceleration is a quick test — if crashes stop, the browser/GPU interaction was the trigger, though the underlying driver still deserves an update."
  - q: "Can bad RAM cause crashes only on YouTube?"
    a: "Yes. Video decoding uses specific memory patterns, and a marginal RAM stick can fail only under those patterns while passing general use. If driver fixes don't help, test the memory — it's a five-minute check that rules out a whole category."
  - q: "Should I reinstall Windows for this?"
    a: "Almost certainly not. This is a driver or browser issue in the vast majority of cases. A reinstall is the last resort after driver cleanup, browser reset, and memory testing have all failed."
---
# How to Fix IRQL_NOT_LESS_OR_EQUAL When Watching YouTube

It's a weirdly specific crash: your laptop is fine all day, then a YouTube video blue-screens it with **IRQL_NOT_LESS_OR_EQUAL**. The specificity is actually a clue — YouTube exercises your browser's hardware acceleration, your GPU driver, and your network driver simultaneously, and one of them has a bug.

Don't reinstall Windows over this. The fix is almost always in the browser settings, the GPU driver, or the network driver. Work through the list below — Fix 1 alone (disabling hardware acceleration) tells you immediately which half of the problem you're in. For IRQL crashes that happen everywhere, not just YouTube, see our [driver IRQL fix guide](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/).

## Why this happens

- **Buggy GPU driver + hardware acceleration:** The browser offloads video decoding to the GPU; a driver bug in that path crashes the kernel.
- **Outdated network driver:** Streaming stresses the Wi-Fi/Ethernet driver continuously, exposing bugs that idle use never hits.
- **Corrupted browser profile or cache:** Damaged GPU-cache files in the browser can feed garbage to the graphics driver.
- **Faulty RAM:** Video decoding memory patterns can trip a marginal memory stick that passes normal use.
- **Overheating during video playback:** Sustained decode load on a dust-clogged laptop pushes thermals over the edge.
- **Conflicting browser extensions:** Ad blockers and video downloaders that hook into the media pipeline can destabilize playback.

## How to fix it

Work through these in order. The first two fixes identify the culprit; the rest eliminate it.

### Fix 1: Disable hardware acceleration in your browser

This is the fastest diagnostic step — it takes the GPU driver out of the video path entirely.

1. In **Chrome/Edge**, go to **Settings > System** and turn off **Use hardware acceleration when available** (in Firefox: **Settings > General > Performance**, uncheck **Use recommended performance settings**, then uncheck hardware acceleration).
2. Restart the browser and watch YouTube for a while.
3. If crashes stop, the trigger is the browser/GPU interaction — continue to Fix 2 to fix the driver properly so you can re-enable acceleration later.
4. If crashes continue with acceleration off, the problem is elsewhere (likely network driver or RAM) — skip to Fix 4.

### Fix 2: Clean-reinstall the graphics driver

A corrupted GPU driver is the most common root cause behind acceleration-triggered IRQL crashes.

1. Download **Display Driver Uninstaller (DDU)** and the latest stable driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or Intel's driver detection tool.
2. Disconnect from the internet, boot into **Safe Mode**, run DDU (**Clean and restart**).
3. Install the fresh driver with the **Clean installation** option.
4. Re-enable hardware acceleration in the browser and test YouTube again.
5. If you have switchable graphics, also update the integrated GPU driver — the browser may use either one.

### Fix 3: Reset the browser

A corrupted browser profile can keep crashing even a healthy driver.

1. Back up your bookmarks (they sync if you're signed in, but verify).
2. In Chrome: **Settings > Reset settings > Restore settings to their original defaults**. In Edge: **Settings > Reset settings**. In Firefox: **Help > More Troubleshooting Information > Refresh Firefox**.
3. Disable all extensions, then re-enable them one at a time over a few days — video downloaders and aggressive ad blockers are the usual suspects.
4. Clear the browser's GPU cache by deleting the **GPUCache** folder in the browser's user-data directory if crashes persist after reset.

### Fix 4: Update the network driver

Hours of streaming hammer the network driver, and an old one can IRQL-crash under sustained throughput.

1. Open **Device Manager** (**Win + X**) and expand **Network adapters**.
2. Right-click your Wi-Fi adapter and choose **Update driver > Search automatically for drivers**.
3. If Windows finds nothing, download the latest driver from your laptop maker's support site — Intel and Realtek both publish newer drivers than Windows Update carries.
4. As a test, try YouTube over Ethernet or a different Wi-Fi network; if crashes stop, the wireless driver or its power-management settings are implicated.
5. In the adapter's **Properties > Power Management**, uncheck **Allow the computer to turn off this device to save power**.

### Fix 5: Test your RAM

Video decoding hits memory in patterns that general use doesn't, so test even if everything else seems fine.

1. Press **Win + R**, type `mdsched.exe`, and choose **Restart now and check for problems**.
2. Check results in **Event Viewer > Windows Logs > System** (MemoryDiagnostics-Results).
3. Errors mean reseating or replacing RAM — see our [Memory Management BSOD guide](/articles/memory-management-bsod-windows-11-fix/) for the full memory-testing walkthrough.
4. No errors means memory is cleared; move on.

### Fix 6: Check thermals during playback

Sustained video decode on a dusty laptop can overheat the CPU/GPU package.

1. Play a 4K YouTube video for 15 minutes while monitoring temperatures with HWiNFO.
2. CPU/GPU package temperatures pinned above 90°C indicate a cooling problem.
3. Blow compressed air through the vents, elevate the laptop, and retest.
4. Also try lowering YouTube quality to 1080p temporarily — if crashes stop at lower resolutions, heat or GPU load is confirmed as the trigger.

### Fix 7: Repair system files and check for bad updates

When hardware and drivers check out, the OS itself may be damaged.

1. Open an admin Terminal and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Check **Settings > Windows Update > Update history** for a driver or cumulative update installed just before crashes began; uninstall suspects via **Uninstall updates**.
3. Run a full scan with **Windows Security** to rule out malware-damaged drivers.
4. As a final step before considering a reset, create a fresh Windows user profile and test YouTube there — a corrupted user profile can produce bizarre, app-specific crashes that nothing else explains. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents profile troubleshooting in detail.

## Closing

An IRQL crash that only happens on YouTube is good news in disguise — the trigger is narrow, which makes it diagnosable. Disable hardware acceleration to confirm the GPU's involvement, clean-reinstall the graphics and network drivers, reset the browser, and test the RAM. One of those steps almost always ends it, and you'll be back to videos without the blue-screen intermission.
