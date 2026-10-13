---
title: "Windows Update Service Missing? A Complete Step-by-Step Recovery"
slug: how-to-fix-windows-update-service-missing-step-by-step
date: 2026-09-03
categories: ["windows-update"]
tags: ["wuauserv", "service missing", "step by step", "registry", "windows 11 24h2"]
description: "A meticulous step-by-step recovery for a missing Windows Update service: verify, rebuild, re-register, and verify updates work again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-service-missing-step-by-step.webp"
faqs:
  - q: "What is the wuauserv service and why does Windows need it?"
    a: "Wuauserv is the Windows Update service: it scans for, downloads, and installs updates. Without it, the Settings page cannot check for updates, the update troubleshooter cannot run its checks, and no patch — security or otherwise — can install. It is the single orchestrator for the entire update pipeline, which is why its absence breaks everything at once."
  - q: "How can I tell if the service is missing versus disabled?"
    a: "Open services.msc. A disabled service appears in the list with Startup type Disabled; a missing service is absent from the list entirely. The command sc query wuauserv answers definitively: it reports a state for existing services and says the service does not exist for missing ones."
  - q: "Do I need another computer to fix this?"
    a: "It helps but is not required. A healthy PC lets you export the correct registry keys in seconds. Without one, you can rebuild the keys manually from documented defaults or repair the damage with DISM, which restores many service registrations. A second PC just makes the job faster by providing a known-good registry export; every step has a documented manual alternative."
  - q: "Will this fix work on Windows 10 too?"
    a: "Yes, the same steps apply: the wuauserv registry layout and DLL set are essentially identical between Windows 10 and 11. Only the Settings navigation paths differ slightly between the two versions. The wuauserv architecture has been stable for years, so the diagnosis, rebuild, and verification steps transfer directly between the two versions."
---

When the Windows Update service vanishes from `services.msc`, most guides tell you to "just restart it" — impossible advice for a service that does not exist. This is the meticulous, no-shortcuts version: every step verified before moving on, every command explained, nothing assumed. If you follow it exactly, you will know at each checkpoint whether you are on track, and you will end with a working update pipeline.

Read each fix fully before executing it. The order matters — verification first, registry rebuild second, DLL registration third, service start fourth, and root-cause removal last so the problem never returns.

## Why this happens

- **Deleted registry keys:** The service's identity lives in `HKLM\SYSTEM\CurrentControlSet\Services\wuauserv`. Debloater scripts and bad guides delete this key, erasing the service.
- **Corrupted service binary registration:** Even with keys present, broken COM registration of the service DLLs makes the Service Control Manager unable to launch it.
- **Failed servicing operation:** A crashed update can leave the service configuration half-written, which Windows reads as "does not exist."
- **Malware and overzealous cleanup:** Infections disable update services; some removal tools delete the service instead of restoring it.
- **Registry hive damage:** Bad sectors or crashes corrupt the SYSTEM hive, dropping service entries silently.
- **Imaging and sysprep errors:** Badly captured deployment images ship without proper service registrations.
- **Policy-based deletion:** Rare group-policy or MDM configurations remove rather than disable the service.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the missing service with two independent checks

1. Press **Win + R**, type `services.msc`, press Enter. Scroll slowly through the entire list and confirm **Windows Update** is genuinely absent.
2. Open an elevated Command Prompt and run `sc query wuauserv` — expect "The specified service does not exist as an installed service."
3. Open **Settings > Windows Update** and click **Check for updates**; note the error code (typically 0x80070424).
4. Two independent confirmations plus the Settings error means the diagnosis is certain — proceed to the rebuild.

### Fix 2: Create a safety net before touching the registry

1. Create a System Restore point: search **Create a restore point**, select C:, click **Create**, and name it "Before wuauserv rebuild."
2. Back up the Services key: in `regedit`, right-click `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services` and **Export** it to your Documents folder.
3. These two safety nets take two minutes and make every subsequent step reversible.
4. If anything behaves unexpectedly later, the restore point returns the machine to this exact state.

### Fix 3: Import the wuauserv registry key

1. On any healthy Windows 11 PC, open `regedit`, go to `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\wuauserv`, right-click, and **Export** to a USB drive.
2. On the broken laptop, double-click the .reg file and approve the merge. Confirm you see "keys and values have been successfully added."
3. Open `regedit` on the laptop and verify the `wuauserv` key now exists with its subkeys (Parameters, Security, TriggerInfo).
4. If you have no second PC, DISM's component repair (Fix 5) can regenerate many service registrations — continue through the steps and circle back.

### Fix 4: Re-register the Windows Update DLLs

1. Open an elevated Command Prompt (right-click Start > **Terminal (Admin)**).
2. Run these four commands one at a time, confirming each success dialog: `regsvr32 wuapi.dll` then `regsvr32 wuaueng.dll` then `regsvr32 wups.dll` then `regsvr32 wuwebv.dll`.
3. Then run `regsvr32 wucltux.dll` and `regsvr32 wudriver.dll` for the client UX and driver-install components.
4. Run `sc query wuauserv` — it should now report the service in a STOPPED state rather than "does not exist." That state change is your proof the rebuild took.

### Fix 5: Repair the servicing stack with DISM and SFC

1. In the same elevated prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for 100 percent.
2. Follow with `sfc /scannow` to verify protected system files.
3. These tools repair any neighboring damage from whatever deleted the service — corrupted manifests, broken component registrations, missing manifests.
4. Restart the laptop. After the reboot, open `services.msc` and confirm **Windows Update** is listed.

### Fix 6: Start the service and confirm it stays up

1. In `services.msc`, double-click **Windows Update**, set **Startup type** to **Manual**, and click **Start**.
2. Watch for 30 seconds — if it stops on its own, open **Event Viewer > Windows Logs > System** and read the service error; a missing dependency is the usual cause, and starting that dependency fixes it.
3. Verify the **Dependencies** tab shows **Remote Procedure Call (RPC)** and that RPC is running.
4. A service that starts and stays running is a rebuilt service — the hard part is done. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) describe these default service states if you want to cross-check.

### Fix 7: Remove the root cause and prove updates work

1. Uninstall any debloater, "privacy," or registry-cleaner tool that may have deleted the keys — check **Installed apps** and your downloads for scripts you ran.
2. Reset any Group Policy under **Windows Components > Windows Update** to **Not configured**.
3. Open **Settings > Windows Update**, click **Check for updates**, and install whatever appears; confirm the history shows success.
4. Run the [update troubleshooter](/articles/best-way-to-fix-windows-update-troubleshooter-not-working/) once as a final systems check — a green result means the whole pipeline, service included, is healthy. Keep drivers healthy afterward with our [driver update walkthrough](/articles/best-way-to-update-drivers-on-windows-11/).

### Fix 8: Verify the repair survives a reboot and a policy refresh

1. Restart the laptop, then immediately run `sc query wuauserv` again — the service must still exist and be startable after a cold boot.
2. Run `gpupdate /force` in an elevated prompt to refresh Group Policy, then re-check `services.msc` — a policy that deletes the service would reappear here, and you would catch it now instead of next month.
3. Schedule a weekly reminder to glance at **Settings > Windows Update**; a healthy pipeline shows recent successful checks, and early detection beats another full rebuild.
4. Document what deleted the service (the tool name, the guide you followed) in a text file on the machine — future-you will thank present-you if this ever recurs.

## Closing

Step by step, verified at every checkpoint: confirm the absence, back up, import the key, re-register the DLLs, repair the stack, start the service, remove the cause, prove it works. That is the entire recovery, and it beats reinstalling Windows by several hours. The service is back because you rebuilt exactly what was deleted — nothing more, nothing less.
