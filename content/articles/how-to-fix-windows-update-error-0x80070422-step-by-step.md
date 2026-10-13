---
title: "How to Fix Windows Update Error 0x80070422 Step by Step"
slug: how-to-fix-windows-update-error-0x80070422-step-by-step
date: 2026-09-25
categories: ["windows-update"]
tags: ["windows update", "0x80070422", "update service", "windows 11"]
description: "Error 0x80070422 means the Windows Update service is disabled or blocked. Follow this step-by-step guide to re-enable the service, clear policy blocks, and get updates installing again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070422-step-by-step.webp"
faqs:
  - q: "What does Windows Update error 0x80070422 mean?"
    a: "The code translates to ERROR_SERVICE_DISABLED: Windows tried to start the Windows Update service (wuauserv) and found it disabled. Because the service cannot run, Windows cannot check for, download, or install updates. It is almost always a configuration problem — the service was switched off by a policy, a registry tweak, or a third-party tool — rather than a broken system file."
  - q: "Can antivirus software cause error 0x80070422?"
    a: "Yes, although indirectly. Some aggressive security suites and so-called PC optimizer tools disable the Windows Update service or block it from starting, believing they are saving resources. If the error appeared right after installing new security software, check its settings for an option that disables automatic updates, or uninstall it temporarily to see whether the update service starts again."
  - q: "Is it safe to re-enable the Windows Update service myself?"
    a: "Yes, on a normal home or small-office laptop it is completely safe. The service is supposed to run on a Manual (Triggered Start) or Automatic startup type; changing it back restores Microsoft's intended behavior. You are not granting anything new permissions — you are simply returning a core Windows component to its default state so updates can install."
  - q: "What if the error returns after every restart?"
    a: "A returning error means something is re-disabling the service on boot: a Group Policy refresh from a work or school account, a third-party updater tool, or a registry script. Check Fix 4's policy and registry steps carefully, and remove any PC tune-up utilities. If the laptop is managed by an organization, the fix must come from its administrator, because policy will keep overwriting your change."
---

Error 0x80070422 is one of the most straightforward Windows Update failures, and also one of the most frustrating when you don't know what it means. Instead of a helpful message, Windows just hands you a hexadecimal code and refuses to check for updates. The translation of that code is plain: **ERROR_SERVICE_DISABLED**. Windows tried to start its own update engine, found it switched off, and gave up.

On laptops this usually isn't random corruption — it's configuration. A tweaked registry file, a "debloat" script, a third-party updater, or a Group Policy from a school or work account can all park the Windows Update service in the Disabled state. The good news is that a service that was switched off can be switched back on, and once it is, updates almost always flow normally again. Below is the order a technician would work through, from the quickest check to the deepest repair.

## Why this happens

- **The Windows Update service (wuauserv) is set to Disabled.** This is the direct cause in the vast majority of cases — the service physically cannot start, so every update operation fails with this code.
- **BITS or related services are also disabled.** Windows Update depends on helpers like Background Intelligent Transfer Service and the Cryptographic Services; if they are disabled too, updates stall even after wuauserv is fixed.
- **A Group Policy or registry setting blocks updates.** Policies under Windows Components > Windows Update can disable the service at a level the Services console cannot override.
- **Third-party "optimizer" or "debloat" tools.** Utilities that promise to speed up Windows sometimes disable update services aggressively and never restore them.
- **A work or school account manages the laptop.** MDM or domain policies re-apply the Disabled state at every reboot, so manual fixes seem to "undo themselves."
- **The service configuration is corrupted.** Rarely, the service's registry keys or binaries are damaged, so Windows reports it as disabled when the real problem is deeper.
- **Antivirus or firewall interference.** Overprotective security software can block the update service from launching or from reaching Microsoft's servers, producing the same symptom.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the failing service in Services

Before changing anything, verify that the update service is actually the problem so you don't chase the wrong cause.

1. Press **Windows key + R**, type `services.msc`, and press Enter.
2. Scroll to **Windows Update**, right-click it, and open **Properties**.
3. Note the **Startup type** field. If it says **Disabled**, you've found your culprit — continue to Fix 2.
4. While you're here, also check **Background Intelligent Transfer Service** and **Cryptographic Services**; both should be on Manual or Automatic, not Disabled.

### Fix 2: Re-enable the Windows Update service

This single change resolves the error for most home users.

1. In the **Windows Update Properties** window, open the **Startup type** dropdown and select **Manual** (the Windows 11 default) or **Automatic**.
2. Click **Apply**, then click **Start** under Service status.
3. Wait for the service to show **Running**, then click **OK**.
4. Open **Settings > Windows Update** and click **Check for updates**. If the check runs without the error, you're done.

### Fix 3: Set the helper services correctly

Windows Update rarely works alone. A disabled helper service produces identical failures.

1. Back in `services.msc`, open **Background Intelligent Transfer Service** properties and set its startup type to **Manual**, then start it.
2. Do the same for **Cryptographic Services** (startup type **Automatic**) and **Windows Installer** (startup type **Manual**).
3. Restart the laptop — don't skip this, because service dependencies re-register during boot.
4. Retry **Settings > Windows Update > Check for updates** and confirm the 0x80070422 error is gone.

### Fix 4: Clear Group Policy and registry blocks

If the service flips back to Disabled on its own, something above your user settings is enforcing it.

1. Press **Windows key + R**, type `gpedit.msc`, and press Enter (skip this if you're on Windows Home — it has no Group Policy editor).
2. Navigate to **Computer Configuration > Administrative Templates > Windows Components > Windows Update** and make sure nothing here is set to **Disabled** in a way that blocks the service; set suspicious entries to **Not Configured**.
3. Open Registry Editor (`regedit`), and check `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` — if an `AU` subkey contains `NoAutoUpdate` set to 1, a policy is blocking updates; back up the key, then delete it.
4. Restart and repeat Fix 2. If the laptop is managed by a school or employer, ask its IT administrator instead — the policy will keep returning otherwise.

### Fix 5: Run the troubleshooter and repair system files

If the service settings look right but updates still fail, the service configuration itself may be damaged.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run the **Windows Update** troubleshooter.
2. Open Command Prompt as administrator and run `sfc /scannow` to repair protected system files; restart when it finishes.
3. If SFC reports unfixable damage, run `DISM /Online /Cleanup-Image /RestoreHealth` in the same elevated prompt, then run SFC again.
4. Microsoft documents additional guided steps for stubborn update failures in its official [Windows Update support hub](https://support.microsoft.com/en-us/windows), which is worth a visit if the error persists.

### Fix 6: Reset the update components as a last resort

When the service starts but updates still error out, the download cache or component registration may be broken.

1. In an administrator Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, and `net stop msiserver`.
2. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with `net start wuauserv`, `net start bits`, `net start cryptsvc`, and `net start msiserver`.
4. Check for updates again. If nothing works, an in-place upgrade using the ISO from [Microsoft's official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) — choosing "Keep personal files and apps" — reinstalls the update stack cleanly.

## Closing

Error 0x80070422 looks cryptic, but in practice it is almost always a service that someone or something switched off, and switching it back on is a five-minute job. If your updates fail with a different code instead, the companion walkthrough for [fixing Windows Update error 0x80070490 on an HP laptop](/articles/how-to-fix-windows-update-error-0x80070490-on-hp-laptop/) covers that "element not found" failure, while our general guide to [fixing another update source error, 0x800F0900](/articles/how-to-fix-windows-update-error-0x800f0900-on-lenovo-laptop/) handles a related component failure.
