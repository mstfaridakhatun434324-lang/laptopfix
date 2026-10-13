---
title: "How to Remove Bloatware from Your Windows 11 Laptop"
slug: how-to-remove-bloatware-from-windows-11-laptop
date: 2026-09-30
categories: ["performance"]
tags: ["bloatware", "remove bloatware", "debloat", "preinstalled apps"]
description: "New laptop full of junk? Remove Windows 11 bloatware safely — what to uninstall, what to leave alone, and why debloat scripts are risky."
thumbnail: "/images/thumbs/how-to-remove-bloatware-from-windows-11-laptop.webp"
faqs:
  - q: "What counts as bloatware on a Windows 11 laptop?"
    a: "Three categories: manufacturer utilities you don't use (support assistants, game hubs, 'experience' apps), third-party trials (antivirus trials, Office trials, WildTangent-style game portals), and Microsoft's own preinstalled apps (Candy Crush-style games, TikTok, Spotify, Clipchamp if you don't use them). Bloatware is anything preinstalled that consumes resources or attention without providing value to you specifically."
  - q: "Is it safe to use debloat scripts like Chris Titus Tech's utility?"
    a: "Popular debloat scripts are powerful but blunt — they remove components other software depends on, break Windows Update in some configurations, and their effects are hard to reverse precisely. Manual removal through Settings is slower but safer and fully reversible. If you use a script, read exactly what it removes first, create a restore point, and avoid the most aggressive options."
  - q: "Will removing bloatware speed up my laptop?"
    a: "Moderately. Removing startup-running bloatware helps boot time and frees RAM/CPU — that's real. But bloatware is rarely the main cause of a slow laptop; a full drive, insufficient RAM, or a spinning hard drive matter far more. Debloat as hygiene, not as a miracle cure, and diagnose the real bottleneck with Task Manager."
  - q: "Can I reinstall something if I remove it by mistake?"
    a: "Usually yes. Microsoft Store apps reinstall from the Store in one click. Manufacturer utilities reinstall from the manufacturer's support page. Third-party trials generally aren't worth reinstalling. The risky removals are system components (via scripts or PowerShell) — those are the ones that sometimes don't come back cleanly, which is why manual Store-app removal is the safe path."
---

Every new Windows laptop arrives carrying someone else's software: the manufacturer's "experience" apps, antivirus trials nagging for subscriptions, game portals, and a rotating cast of Microsoft Store apps you never asked for. This bloatware costs you boot time, RAM, notification spam, and occasionally real money when a trial converts. Cleaning it out is satisfying — but there's a safe way and a reckless way, and the reckless way (aggressive debloat scripts) breaks Windows features people later miss.

The safe method: uninstall through Settings, disable what can't be uninstalled, clean up startup entries, and leave system components alone. For the startup-entry cleanup specifically, see [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/); for the broader performance picture, [speeding up a slow laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Manufacturers get paid to preinstall**: Bloatware is a revenue stream — trials and partnerships subsidize the laptop's price.
- **Microsoft preinstalls Store apps**: Sponsored apps (games, social, streaming) ship with Windows and reinstall after feature updates.
- **Trials are designed to convert**: Antivirus and Office trials nag until you pay or remove them.
- **Utilities duplicate Windows features**: Manufacturer "support assistants" often duplicate what Windows Update and Settings already do.
- **Preinstalled apps run at startup**: Many add startup entries and background services you never approved.
- **Feature updates reinstall some apps**: Major Windows updates can bring back removed sponsored apps.
- **"Free" software isn't free**: The cost is your boot time, RAM, and attention.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Inventory what's actually installed

Know your enemy before uninstalling.

1. Open **Settings** > **Apps** > **Installed apps**, sort by **Size** or **Date installed** — preinstalled apps cluster around the laptop's manufacturing date.
2. Make a quick list (mental or written) in three buckets: **definitely remove** (games, trials, apps you've never opened), **maybe** (manufacturer utilities — research each), **keep** (drivers' control panels you use, apps you chose).
3. Check **Task Manager** > **Startup apps** for the **Startup impact** column — bloatware with High impact is costing you boot time right now.
4. Check `services.msc` for manufacturer services running constantly (support assistants, telemetry) — note names for Fix 3.
5. This inventory takes ten minutes and prevents the classic mistake: removing something in a hurry that you actually needed.

### Fix 2: Uninstall the obvious junk through Settings

The safe bulk removal.

1. In **Settings** > **Apps** > **Installed apps**, click the **...** on each unwanted app > **Uninstall**. Start with: preinstalled games, TikTok/Spotify/Disney+ (if you don't use them), antivirus trials, Office trials (if you use another office suite), WildTangent-style game portals, and manufacturer "experience"/shopping apps.
2. For Microsoft Store apps that lack an uninstall option in Settings, right-click them in the **Start menu** > **Uninstall** — the Start menu can remove some apps Settings can't.
3. Work through the list methodically rather than in a rage — ten minutes of calm clicking beats a script's collateral damage.
4. After uninstalling, check **Settings** > **Apps** > **Startup** and **Task Manager** > **Startup apps** — some apps leave startup entries behind; disable those too.
5. Restart and verify your daily apps still work before continuing to the trickier removals.

### Fix 3: Evaluate manufacturer utilities individually

Don't nuke these blindly — some are genuinely useful.

1. **Usually safe to remove**: manufacturer app stores, "experience" programs, shopping/deals apps, game hubs (if you don't game), and duplicate "support assistants" when Windows Update handles drivers fine.
2. **Usually worth keeping**: the thermal/fan control utility (often the only fan control you have), battery charge-limit tools, BIOS update utilities, and fingerprint/Windows Hello companion apps.
3. **Research the unclear ones**: search "[app name] safe to uninstall" — someone has asked about every manufacturer utility ever shipped.
4. If you remove a utility and later miss a feature (fan control, battery limiter), reinstall just that utility from the manufacturer's support page — [Dell's support page](https://www.dell.com/support) (or HP's or Lenovo's).
5. Disable rather than uninstall when unsure — a disabled startup entry costs nothing and is instantly reversible.

### Fix 4: Remove provisioned apps with PowerShell (carefully)

For the stubborn preinstalled apps that resist normal uninstall.

1. Open **Terminal (Admin)**. List provisioned apps with `Get-AppxProvisionedPackage -Online | Select DisplayName` to see what's baked into the image.
2. Remove specific apps by name, e.g.: `Get-AppxPackage *CandyCrush* | Remove-AppxPackage` (current user) — do them one at a time, by exact name, never with wildcards that could match system packages.
3. **Never remove**: `Microsoft.Store`, `Microsoft.DesktopAppInstaller` (winget), anything with `Windows.` or `ShellExperience` in the name, or packages you can't identify — unidentified packages stay.
4. To prevent re-provisioning for new users: `Remove-AppxProvisionedPackage -Online -PackageName <name>` — this stops the app reinstalling for new accounts.
5. Create a **restore point** before any PowerShell removal session — this is the layer where reversibility gets murky.

### Fix 5: Stop removed apps from coming back

Feature updates love to reinstall sponsored apps.

1. After each major Windows feature update (annual), recheck **Settings** > **Apps** > **Installed apps** for resurrected apps — remove them again; it takes two minutes.
2. For a more durable block on consumer features: **Group Policy** (Pro) > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Cloud Content** > enable **Turn off Microsoft consumer experiences** — this stops the automatic installation of suggested apps.
3. On Home edition, the equivalent registry value exists but tread carefully — document any registry change you make.
4. Keep a short text list of what you removed — re-running your personal "remove list" after feature updates is faster than re-deciding each time.
5. Don't obsess: a couple of reinstalled megabytes aren't worth registry surgery. Remove, move on.

### Fix 6: Clean up startup, services, and notifications

The bloatware afterlife — remnants that keep costing resources.

1. **Task Manager** > **Startup apps**: disable every removed app's leftover entry, plus anything with High impact you don't need at login.
2. `services.msc`: set manufacturer telemetry/support services you don't use to **Manual** (not Disabled — Manual lets them run if actually needed, Disabled can break things).
3. **Settings** > **System** > **Notifications**: turn off notifications for apps you kept but don't need pinging you — notification spam is bloatware's other tax.
4. Check **Task Scheduler** for manufacturer maintenance tasks (telemetry uploads, "experience improvement") and disable the ones that are pure data collection.
5. Our [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) covers the complete startup audit if you want the deep version.

### Fix 7: The clean-install alternative (for the thorough)

When the laptop is new and you want zero bloat from minute one.

1. On a brand-new laptop, consider a clean Windows install using the [Windows 11 Media Creation Tool](https://www.microsoft.com/en-us/software-download/windows11) — this wipes all manufacturer bloatware at once.
2. Back up the manufacturer's driver packages first (download the essentials: chipset, Wi-Fi, graphics, audio — or at least the network driver on a USB stick so you can get online).
3. During setup, decline every optional offer and skip Microsoft account tricks per your preference — fewer preinstalled apps attach to local accounts in some configurations.
4. After install: chipset drivers first, then device drivers, then Windows Update — our [chipset guide](/articles/how-can-i-install-chipset-drivers/) covers the order.
5. Honest assessment: clean-install is the best debloat but costs an afternoon. For most people, Fixes 1–6 get 90% of the benefit in 30 minutes. Also note: clean installs can lose manufacturer-specific features (battery limiters, fan control) — reinstall those utilities selectively afterward. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the reset and reinstall options officially.

## Closing

Debloating is hygiene, not heroics: uninstall the obvious junk through Settings, evaluate manufacturer utilities individually, disable the leftovers, and leave system components alone. The aggressive scripts promise a one-click clean machine and deliver a machine with subtly broken features you'll discover months later. Thirty careful minutes beats a script's afternoon of regret.
