---
title: "How to Fix Windows Update Error 0x80080005 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80080005-in-windows-11-24h2
date: 2026-09-07
categories: ["windows-update"]
tags: ["windows update", "0x80080005", "error code", "windows 11", "com server"]
description: "Error 0x80080005 means a COM server Windows Update needs failed to start. Re-register its DLLs and repair the engine with this guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80080005-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80080005 mean?"
    a: "CO_E_SERVER_EXEC_FAILURE: a Component Object Model server that Windows Update depends on could not be launched. The update engine is built from COM components registered in the system, and when those registrations break, the engine cannot even start — so every update attempt dies instantly."
  - q: "Which DLLs should I re-register for this error?"
    a: "The core set is wuapi.dll, wuaueng.dll, wups.dll, wuwebv.dll, atl.dll, and msxml3.dll — the libraries behind the update engine's COM interfaces. Re-register each with regsvr32 from an elevated prompt. This rebuilds the registry entries the engine needs to launch its components."
  - q: "Why would the registrations break on their own?"
    a: "Interrupted updates, botched software uninstalls, overaggressive registry cleaners, and antivirus quarantines can all damage COM registrations. Disk faults corrupt the registry hives themselves. The damage is usually silent — everything seems fine until the next update check tries to start the engine and fails."
  - q: "Re-registering did not help. What is next?"
    a: "Repair the underlying system files with DISM RestoreHealth followed by SFC, since damaged binaries can keep even correct registrations from working. If that fails too, reset the update components and try again. Persistent CO_E_SERVER_EXEC_FAILURE after all of that points to registry or store damage deep enough for an in-place upgrade."
---

Imagine turning a key and hearing nothing — not even a click. The engine is there, the fuel is there, but the starter motor never engages. That is 0x80080005: Windows Update cannot even begin because one of its COM server components refuses to launch. Every update attempt dies at the starting line, before any downloading or installing happens.

Laptops on 24H2 land here through several routes. A crashed update half-unregistered the engine's DLLs, a registry cleaner "optimized" the COM registrations into oblivion, an antivirus quarantine seized a system library, or a disk fault nibbled the registry hives. In practical terms, the engine cannot assemble itself: its DLL registrations or the hosting services are broken.

The repairs below start with the direct fix — rebuilding the registrations — and escalate toward the heavy machinery. Begin at the top and work down; stop at the first fix that gets updates running again, since later steps exist only for stubborn cases.

## Why this happens

- **The engine's DLL registrations are broken.** Unregistered or mis-registered libraries leave COM unable to launch the components.
- **System files behind the registrations are damaged.** Correct registry entries cannot help if the binaries they point to are corrupt.
- **The COM registry area is wounded.** Class registrations mapping components to their DLLs can corrupt after bad shutdowns.
- **System folder permissions drifted.** Broken ACLs on System32 or WinSxS keep COM servers from loading their libraries.
- **Antivirus quarantined an engine file.** A seized DLL leaves a hole the next update check falls into.
- **A botched uninstall tore out shared components.** Poorly written uninstallers sometimes remove libraries other software still needs.
- **An interrupted update left half-written registrations.** A crash during servicing can strand the engine mid-reconfiguration.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Bounce the engine's services to rule out a wedge

A wedged service can mimic registration damage, and a simple bounce resolves it when that is all it is. Bouncing the engine's services is the quickest way to rule that out before attempting the heavier repairs below.

1. Bring up an administrator Command Prompt.
2. Run `net stop wuauserv`, then `net stop bits`, then `net stop cryptsvc`.
3. Start them again in order: `net start cryptsvc`, `net start bits`, `net start wuauserv`.
4. Try the update check once more.

### Fix 2: Re-register the update engine's DLLs

This is the signature repair for this code: rebuild the COM registrations the engine needs to start itself. Each regsvr32 call writes the registry entries for one library, and the full set restores the engine's ability to launch its components.

1. In the elevated prompt, stop the update service: `net stop wuauserv`.
2. Register each library in turn, confirming each dialog:
   `regsvr32 wuapi.dll`
   `regsvr32 wuaueng.dll`
   `regsvr32 wups.dll`
   `regsvr32 wuwebv.dll`
   `regsvr32 atl.dll`
   `regsvr32 msxml3.dll`
3. Restart the service: `net start wuauserv`.
4. Run the update check and see whether the engine finally starts. A successful check here means the registrations were the whole problem.

### Fix 3: Repair system files and permissions

Broken registrations sometimes sit atop damaged binaries — correct registry entries cannot rescue corrupt DLLs. This pass repairs the files themselves and resets the permissions COM needs to load them.

1. From the elevated prompt, run `sfc /scannow` and let it finish.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to 100 percent.
3. Reboot and retry the update.

### Fix 4: Run the automated troubleshooter

The Windows Update troubleshooter detects dead services and broken registrations, applying its own safe repairs before you attempt anything manual. It is quick, harmless, and occasionally resolves the code by itself.

1. Fire up Settings and proceed to System > Troubleshoot > Other troubleshooters.
2. Tap Run next to the Windows Update entry.
3. After completion, restart the laptop and retest.

### Fix 5: Reset the update components

When the engine and its registrations are both suspect, a full component reset wipes the engine's state so the freshly registered DLLs start from nothing. None of your files are involved — only the update cache gets rebuilt.

1. Idle the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Shift the two cache folders aside: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Raise the services back up: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Survey for updates.

### Fix 6: Reinstall Windows over the existing copy

If the engine still will not start, its damage runs deeper than registrations — reinstalling 24H2 over itself rebuilds the whole COM and servicing infrastructure. Use the ISO from [Microsoft's Windows 11 download site](https://www.microsoft.com/en-us/software-download/windows11) only.

1. Present the ISO and initiate `setup.exe`.
2. Ratify the license terms while keeping **Keep personal files and apps** chosen.
3. Apportion 30 to 90 minutes with multiple restarts; never meddle with it.
4. Sign in and attest that updates run.

### Fix 7: Rebuild the store with DISM, then sweep with SFC

Many of these failures sit on a damaged component store or corrupt system files, and these two utilities repair exactly that kind of damage. DISM fetches fresh copies from Windows Update while SFC inspects the protected files. Microsoft documents both in its [Windows support hub](https://support.microsoft.com/en-us/windows); allow 15 to 30 minutes.

1. Launch `DISM /Online /Cleanup-Image /RestoreHealth` from the elevated prompt and let it reach 100 percent without closing the window.
2. Then run `sfc /scannow` and reboot.
3. Attempt the update check again.

## Closing

When the update engine cannot launch its own components, rebuilding the DLL registrations is what brings it back. Once the engine runs but updates still fail, the [24H2 update-error guide](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) translates the next code you meet, while the [troubleshooter walkthrough](/articles/best-way-to-fix-windows-update-with-troubleshooter/) handles the automated service checks. COM component behavior is documented in [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).
