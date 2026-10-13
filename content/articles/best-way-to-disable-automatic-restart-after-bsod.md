---
title: "How to Disable Automatic Restart After a Blue Screen"
slug: best-way-to-disable-automatic-restart-after-bsod
date: 2026-09-14
categories: ["windows-errors"]
tags: ["bsod", "automatic restart", "stop code", "troubleshooting"]
description: "Blue screen vanishes before you can read it? Disable automatic restart so the error stays on screen long enough to diagnose."
thumbnail: "/images/thumbs/best-way-to-disable-automatic-restart-after-bsod.webp"
faqs:
  - q: "Why does Windows restart automatically after a blue screen?"
    a: "It's the default 'Automatically restart' setting under Startup and Recovery — designed to get servers and unattended PCs back online fast. On a personal laptop it just hides the error message you need to diagnose the crash."
  - q: "Is it safe to disable automatic restart?"
    a: "Yes, completely. It changes nothing about the crash itself — Windows still writes the dump file and logs the event. It only stops the instant reboot, leaving the blue screen visible until you restart manually."
  - q: "What if Windows won't boot long enough to change the setting?"
    a: "Use the recovery environment: interrupt boot three times, go to Troubleshoot > Advanced options > Startup Settings > Restart, and press 9 to 'Disable automatic restart after failure' for that boot. Or set it via bcdedit from the recovery Command Prompt."
  - q: "Will I still get crash dumps with auto-restart off?"
    a: "Yes. Dump file creation is a separate setting ('Write debugging information') and is unaffected. Disabling auto-restart only controls the reboot behavior."
---

Windows' default behavior after a blue screen is to reboot immediately — often so fast you can't read the stop code, let alone the driver name in parentheses. That default makes sense for a server in a closet; for your laptop, it destroys the single most useful piece of diagnostic information the crash gives you. Disabling automatic restart costs nothing, changes nothing about system stability, and turns every future blue screen into a readable error message instead of a blink-and-miss-it flash.

Do this now, before the next crash — you can't read the error after the fact any other way (well, mostly: the dump file still records it, and our [WinDbg guide](/articles/how-to-read-dump-files-with-windbg-on-windows-11/) shows how to read that — but the on-screen message is instant and free). There are several methods depending on whether Windows currently boots.

## Why this happens (why the setting exists and why you'd change it)

- **It's on by default**: Windows enables "Automatically restart" on every installation. Most users never know the option exists until a crash flashes past.
- **The reboot destroys the evidence**: The stop code and failing driver name shown on the blue screen are the fastest diagnostic clues — the auto-restart hides them.
- **It can mask a crash loop**: If Windows crashes during boot, auto-restart creates a rapid reboot loop that's harder to interrupt than a static blue screen.
- **Dump files still get written**: Disabling the restart doesn't affect crash dump creation — you lose nothing diagnostically.
- **Servers vs. laptops**: The default optimizes for unattended machines. Your laptop has you sitting in front of it — the tradeoff is backwards for personal use.
- **The setting sometimes re-enables**: Major Windows updates occasionally reset it. Worth re-checking after feature updates if crashes return to flashing past.

## How to fix it (disable the auto-restart)

Work through these in order — use the first method that applies to your situation.

### Fix 1: Disable it in System Properties (Windows boots normally)

The standard method — thirty seconds.

1. Press **Windows + R**, type `sysdm.cpl`, and press Enter.
2. Go to the **Advanced** tab and click **Settings** under **Startup and Recovery**.
3. Under **System failure**, untick **Automatically restart**.
4. While you're here, verify **Write debugging information** is set to **Automatic memory dump** or **Small memory dump** — this ensures crash dumps keep being created.
5. Click **OK**. The next blue screen will stay on screen until you hold the power button. Microsoft's [guide to startup and recovery settings](https://support.microsoft.com/en-us/windows) covers these options in more detail.

### Fix 2: Disable it from Settings (alternative path)

Same setting, different route — useful if you prefer the modern Settings app.

1. Open **Settings** > **System** > **About**.
2. Click **Advanced system settings** (opens the same System Properties dialog).
3. Follow Fix 1 from step 2 onward.

There's no pure-Settings toggle for this — Microsoft kept it in the classic dialog. The path above is the quickest way there.

### Fix 3: Disable it for one boot from Startup Settings (Windows won't stay booted)

When crashes happen too fast to change the setting normally:

1. Force the recovery environment: interrupt the boot three times (power off at the logo/spinning dots).
2. Go to **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
3. Press **9** for **Disable automatic restart after failure**.
4. Windows boots with auto-restart off for this session — the next crash will hold on the blue screen so you can read it. Then use Fix 1 to make it permanent.

### Fix 4: Disable it via Command Prompt (recovery or admin terminal)

For scripting, remote help, or when the GUI is unreachable.

1. Open **Terminal (Admin)** — or the **Command Prompt** from the recovery environment (**Troubleshoot** > **Advanced options** > **Command Prompt**).
2. Run: `wmic recoveros set AutoReboot = False`
3. Verify with: `wmic recoveros get AutoReboot` — it should report **FALSE**.
4. Alternatively, the registry method: open `regedit`, navigate to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CrashControl`, and set **AutoReboot** to **0**.

The `wmic` command is the cleanest — one line, immediate effect, no reboot needed.

### Fix 5: What to do with the visible blue screen

Now that the error stays on screen, use it — this is the entire point of the change.

1. **Photograph it** with your phone — the stop code (e.g., `IRQL_NOT_LESS_OR_EQUAL`) and any driver name in parentheses (e.g., `(rtwlanu.sys)`). Phone photos are more reliable than memory; in the stress of a crash you'll misremember the exact code.
2. Note the **stop code** — search it on this site or with the driver name to find the targeted fix.
3. Note the **driver name in parentheses** if present — it names the exact `.sys` file involved, which usually maps directly to a device (network, graphics, storage) you can update or roll back.
4. Check whether a **dump was created**: after rebooting, look in `C:\Windows\Minidump` for a new `.dmp` file matching the crash time.
5. Common next steps by stop code: driver updates for `DRIVER_IRQL` / `SYSTEM_THREAD_EXCEPTION`, memory tests for `MEMORY_MANAGEMENT`, storage checks for `INACCESSIBLE_BOOT_DEVICE`. Our [blue screen hub](/articles/how-to-fix-blue-screen-of-death-windows-11/) routes each code to its fix.

### Fix 6: Re-check after major Windows updates

Feature updates sometimes reset this setting.

1. After each annual Windows feature update, re-open `sysdm.cpl` > **Advanced** > **Startup and Recovery Settings** and confirm **Automatically restart** is still unticked.
2. Consider adding it to a post-update checklist alongside driver updates and backup verification.

## Closing

Disabling automatic restart is the rare tweak that's pure upside: zero risk, and it converts every future blue screen from a mystery into a readable diagnosis. It won't fix anything by itself — but it's the step that makes all the actual fixes findable, because you can finally see what you're fixing. Do it now while the system is stable; in the middle of a crash loop is a much worse time to learn where the setting lives. And once you've captured a stop code from the held screen, the dump file in `C:\Windows\Minidump` has the full story whenever you're ready to dig deeper.
