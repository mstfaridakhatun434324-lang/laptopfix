---
title: "How to Stop Windows Restarting Automatically After a Blue Screen"
slug: how-to-disable-automatic-restart-after-bsod
date: 2026-10-03
categories: ["windows-errors"]
tags: ["bsod", "automatic-restart", "startup-and-recovery"]
description: "Windows reboots before you can read the blue screen. Here is how to disable automatic restart in about 30 seconds so the stop code stays visible."
thumbnail: "/images/thumbs/how-to-disable-automatic-restart-after-bsod.webp"
faqs:
  - q: "Why does Windows restart immediately after a blue screen?"
    a: "The default Startup and Recovery setting tells Windows to reboot automatically on system failure. It is meant to get servers and unattended PCs back online fast, but on a laptop it just robs you of the stop code you need for diagnosis. Disabling it is safe and reversible."
  - q: "Will disabling automatic restart harm my computer?"
    a: "Not at all. It only changes what happens after a crash: instead of rebooting instantly, the machine waits on the blue screen until you hold the power button. Windows still writes the crash dump either way, so no diagnostic data is lost."
  - q: "Can I disable automatic restart if Windows will not boot?"
    a: "Yes — use the recovery environment. Boot from Windows installation media, choose **Repair your computer > Troubleshoot > Command Prompt**, and run `wmic recoveros set AutoReboot = False`. That flips the same setting without needing a working desktop."
  - q: "Does this setting survive Windows updates?"
    a: "Almost always, yes. Feature updates occasionally reset peripheral settings, but the automatic-restart flag is rarely touched. If you notice instant reboots returning after a big update, just check the checkbox again — it takes ten seconds."
---
The most annoying thing about a blue screen is not the crash — it is that Windows reboots before you can read what it says. That stop code and driver name on the screen are the two most valuable clues you will ever get, and the default setting throws them away. The reboot is so fast that most people never see more than a flash of blue and a sad emoticon before Windows is already restarting — which is exactly why this setting exists.

Disabling automatic restart takes about thirty seconds and changes nothing else about how your PC behaves. Here is how to do it, plus what to do with the information once you can actually read it. You will also learn how to make sure Windows saves a crash dump each time, so even if you miss the screen, the evidence is preserved on disk for later analysis.

## Why this happens

- **The default favors uptime over diagnosis.** Microsoft ships Windows set to reboot on failure, which suits servers but frustrates troubleshooting.
- **The stop code vanishes in seconds.** Without disabling the restart, you get a two-second glimpse of the error — not enough to write anything down.
- **Crash dumps still get written either way.** Disabling the reboot does not affect dump creation; it only keeps the screen visible.
- **It is a per-installation setting.** A fresh Windows install or major reset restores the default, which is why the reboot behavior can mysteriously return.
- **Safe Mode and recovery tools do not change it.** You have to flip this setting explicitly, from a running Windows or the recovery command prompt.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Disable it from System Properties (the classic way)

This is the setting itself — one checkbox, and the instant reboots stop. See [Microsoft's guide to startup and recovery options](https://support.microsoft.com/en-us/windows) for the official documentation of this dialog. This checkbox is the master switch — every other method in this guide flips the same underlying setting, so you only need one of them to take effect.

1. Press **Win + R**, type `sysdm.cpl`, and press **Enter**.
2. Open the **Advanced** tab and click **Settings** under **Startup and Recovery**.
3. Uncheck **Automatically restart** under **System failure**.
4. Click **OK** twice. The next blue screen will stay put until you power off manually.

### Fix 2: Disable it from the Settings app

The same setting through the modern interface, if you prefer it. Use this path if you prefer the modern Settings interface; it opens the same classic dialog behind the scenes, so the result is identical.

1. Open **Settings > System > About**.
2. Click **Advanced system settings** on the right side.
3. In the window that opens, go to the **Advanced** tab and click **Settings** under **Startup and Recovery**.
4. Uncheck **Automatically restart** and click **OK**.

### Fix 3: Disable it from the recovery command prompt

For when Windows will not boot far enough to reach the desktop at all. The WMIC command writes directly to the recovery configuration, which is why it works even when Windows cannot boot to the desktop at all.

1. Boot from Windows installation media and choose **Repair your computer**.
2. Go to **Troubleshoot > Advanced options > Command Prompt**.
3. Run `wmic recoveros set AutoReboot = False` and wait for the success message.
4. Type `exit`, remove the media, and restart. If you need a refresher on reaching these tools, see our [guide to booting into Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/).

### Fix 4: Confirm crash dumps are being written

With the screen now staying visible, make sure the dump file is also being saved for deeper analysis. Minidumps are tiny — a few hundred kilobytes each — and Windows keeps several, so enabling them costs nothing in disk space while giving you a crash history.

1. In the same **Startup and Recovery** window, check **Write an event to the system log** is ticked.
2. Set **Write debugging information** to **Automatic memory dump**.
3. Note the dump file path (usually `%SystemRoot%\MEMORY.DMP` for full dumps, minidumps land in `C:\Windows\Minidump`).
4. Click **OK**. Future crashes will now leave both a readable screen and a dump file.

### Fix 5: Photograph the next blue screen

Old-fashioned, but it works — and it captures everything in one shot. A photo also captures the QR code Windows 11 shows on the blue screen, which links to Microsoft's troubleshooting page for that stop code.

1. When the next crash holds on the blue screen, take a clear phone photo of the entire screen.
2. Make sure the stop code (in ALL_CAPS_WITH_UNDERSCORES) and any named `.sys` file are legible.
3. Look up the stop code with the filename together — that combination identifies the faulty component. Our [blue screen fix guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) shows how to turn that information into a fix.

### Fix 6: Re-enable it once you are done troubleshooting

Automatic restart is genuinely useful day to day — you only needed it off while diagnosing. There is no performance benefit to leaving it off — the only thing the unchecked box does is wait for you, so turn it back on once you have your diagnosis.

1. Return to **Startup and Recovery** via `sysdm.cpl` as in Fix 1.
2. Re-check **Automatically restart** and click **OK**.
3. Leave it on during normal use; flip it off again any time a new blue screen appears and you need to read it.

### Fix 7: Use Event Viewer as a backup record

Even with the screen held visible, the Event Viewer keeps a permanent log of every crash — useful when you forget to photograph the screen.

1. Press **Win + X** and choose **Event Viewer**.
2. Expand **Windows Logs** and click **System**.
3. Click **Filter Current Log** on the right, tick **Critical** and **Error**, and click **OK**.
4. Look for events from source **BugCheck** — the details pane shows the exact stop code in hex and the faulting module.
5. Double-click any BugCheck event to read the full details, which you can copy-paste into a search instead of retyping from a photo.

## Closing

This is a thirty-second change that pays for itself the very next time your laptop blue-screens. Read the stop code, photograph the screen, and you will troubleshoot from evidence instead of guesswork — which is the difference between fixing it today and fighting it for a week. Thirty seconds of settings change, and every future blue screen becomes a readable clue instead of a mystery reboot.
