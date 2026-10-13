---
title: "How to Fix File Explorer High CPU on Windows 10"
slug: how-to-fix-file-explorer-high-cpu-on-windows-10
date: 2026-10-08
categories: ["performance"]
tags: ["file explorer", "high cpu", "explorer.exe", "windows 10"]
description: "Explorer.exe spiking CPU on Windows 10? Fix classic shell issues: context menu handlers, thumbnail cache, Quick Access dead links, and preview pane hangs."
thumbnail: "/images/thumbs/how-to-fix-file-explorer-high-cpu-on-windows-10.webp"
faqs:
  - q: "Why does Explorer.exe use CPU on Windows 10 when no folder is open?"
    a: "On Windows 10, Explorer.exe hosts the entire shell — taskbar, desktop, Start menu, notification area, and file windows. CPU usage with no visible folder open usually comes from shell extensions (context-menu handlers), the taskbar's News and interests feed, thumbnail generation for the desktop background slideshow, or Quick Access retrying unreachable network paths. The open window is rarely the cause."
  - q: "Is restarting Explorer safe on Windows 10?"
    a: "Completely safe. Task Manager > Windows Explorer > Restart kills and relaunches the shell; your applications keep running untouched, and the taskbar/desktop reappear within seconds. It's the standard first response to a glitched Explorer. If high CPU returns immediately after the restart, the trigger — extension, thumbnail, network path — is persistent and needs the fixes below."
  - q: "Do I need third-party tools to find bad shell extensions?"
    a: "ShellExView (NirSoft, free and portable) is the practical standard — it lists every shell extension with its vendor, lets you disable non-Microsoft ones in bulk, and changes take effect after an Explorer restart. You can do it manually via registry, but with dozens of handlers registered across several registry locations, the tool turns an hour of registry spelunking into two minutes."
  - q: "Windows 10 is out of support — is it still worth fixing Explorer issues?"
    a: "The fixes here are configuration changes, not updates, so they work regardless of support status. But Windows 10 reached end of support in October 2025, meaning no more security patches. If your hardware qualifies, upgrading to Windows 11 via the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) is the wiser long-term move — though these Explorer fixes will keep a Windows 10 machine usable in the meantime."
---

Windows 10's `Explorer.exe` is the whole shell — taskbar, desktop, Start menu, and file windows in one process — so when it burns CPU, everything feels broken at once. The causes on Windows 10 are the classics: third-party right-click handlers, thumbnail generation stuck on a bad file, Quick Access chasing dead network paths, and the taskbar's News and interests feed churning in the background. (For Windows 11's tabbed Explorer and its quirks, see [our Windows 11 guide](/articles/how-to-fix-file-explorer-high-cpu-on-windows-11/).) For Explorer that's slow rather than CPU-hungry, general [Windows 11 slowdown fixes](/articles/laptop-running-slow-windows-11-how-to-speed-up/) cover the system side.

## Why this happens

- **Context-menu shell extensions**: Third-party right-click handlers loading into Explorer and spinning on interaction.
- **Thumbnail cache corruption**: Damaged thumbcache databases causing endless regeneration.
- **Quick Access dead pins**: Pinned network/USB locations that no longer exist, retried constantly.
- **Preview pane on malformed files**: Preview handlers burning CPU trying to render broken documents.
- **News and interests feed**: The taskbar feed's background refreshes adding shell CPU.
- **Desktop slideshow**: Rapid background changes keeping thumbnail/compositing work constant.
- **Network discovery churn**: Explorer polling unreachable network devices in the Network folder.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart Explorer and map the trigger

Confirm the pattern before changing anything.

1. Open **Task Manager**, right-click **Windows Explorer** > **Restart** — taskbar and desktop blink back; apps are unaffected.
2. Watch CPU for 5 minutes with no Explorer windows open: drops to ~0% = transient glitch; climbs again = persistent trigger.
3. Open a folder and test specific actions: right-click spikes = shell extensions (Fix 2); opening one folder spikes = thumbnails/contents (Fix 3); constant = Quick Access/feed (Fix 4).
4. Check the **Details** tab to confirm it's `explorer.exe` and not a similarly-named process.
5. Test in **Safe Mode**: calm there means a third-party extension or startup item; still high means system-level corruption.

### Fix 2: Disable bad context-menu extensions

The classic Windows 10 Explorer fix — still the #1 cause.

1. Download **ShellExView** (NirSoft, free portable) and run as Administrator.
2. **Options** > **Filter by Extension Type** > **Context Menu**; sort by **Company** and select all non-Microsoft entries.
3. Right-click > **Disable Selected Items**, then restart Explorer from Task Manager.
4. Test right-clicks and general use for 15 minutes — calm? Re-enable in halves to find the culprit.
5. Usual suspects on Windows 10: cloud-storage overlays, archive utilities, antivirus "scan" entries, old printer software handlers, and graphics control panels. Leave the offender disabled; check the vendor for an updated version.

### Fix 3: Rebuild the thumbnail and icon caches

For folder-specific or desktop-related spikes.

1. Open **Disk Cleanup** (`cleanmgr`), select C:, check **Thumbnails**, and run it — the safe GUI method.
2. For the thorough version, close all Explorer windows, open Command Prompt, and run: `taskkill /f /im explorer.exe`, then `del /f /s /q %LocalAppData%\Microsoft\Windows\Explorer\thumbcache_*.db`, then `del /f /s /q %LocalAppData%\IconCache.db`, then `start explorer.exe`.
3. In **File Explorer Options** (Control Panel or View > Options) > **View** tab, you can check **"Always show icons, never thumbnails"** as a temporary test — if CPU normalizes, thumbnails were definitively the trigger.
4. Turn off the **Preview pane** (View tab > Preview pane) while testing — preview handlers for malformed Office/PDF files are notorious CPU burners.
5. For the corrupt-file hunt: in the problem folder, sort by **Date modified**, move recent media files out in batches until the spike stops, then narrow it down.

### Fix 4: Clean Quick Access and silence the taskbar feed

Stops the shell chasing ghosts.

1. In Explorer's left pane, right-click each **Quick Access** pin pointing to network drives, removed USB sticks, or deleted folders > **Remove from Quick access**.
2. **File Explorer Options** > **General**: set **"Open File Explorer to"** = **This PC**; under Privacy, uncheck both history options and click **Clear**.
3. Right-click the taskbar > **News and interests** > **Turn off** — this feed is Explorer-hosted and its refresh cycles add background CPU.
4. Right-click taskbar > **Search** > uncheck **Show search box** (use the icon) — the full search box's background activity is heavier than the icon.
5. Disconnect stale mapped drives in **This PC** (right-click > Disconnect) and restart Explorer — the shell should no longer retry dead paths.

### Fix 5: Repair system files and reset folder views

When the shell itself is damaged.

1. Run `sfc /scannow` from an elevated Command Prompt, then `DISM /Online /Cleanup-Image /RestoreHealth` — in that order.
2. Reset all folder views: **File Explorer Options** > **View** tab > **Reset Folders** — corrupt saved views cause per-folder CPU loops.
3. Check **Windows Update** (Settings > Update & Security) for pending updates — Explorer fixes shipped in cumulative updates through end of support; the [Update Catalog](https://www.catalog.update.microsoft.com/) has specific KBs if Update is stuck.
4. Create a **new local user account** and test Explorer there — calm in the new account means your profile's shell registry hive is corrupt; migrate rather than repair.
5. Check **Event Viewer** > **Windows Logs** > **Application** for Explorer crash/hang events (event 1000/1002) around the spikes — the faulting module name identifies the culprit directly.

### Fix 6: Reduce Explorer's ongoing workload

Lighten the shell for older hardware.

1. **File Explorer Options** > **View**: check **"Always show icons, never thumbnails"** permanently if thumbnails keep causing trouble (reversible anytime).
2. Set desktop background to a **static picture** instead of Slideshow (Settings > Personalization > Background).
3. In **This PC**, avoid leaving the **Network** folder open — with network discovery on, Explorer polls the LAN continuously; turn discovery off (Control Panel > Network and Sharing Center > Advanced sharing settings) if you don't browse network devices.
4. Uninstall unused cloud-storage clients and archive tools — fewer shell extensions installed means fewer that can misbehave.
5. Keep the system maintained: monthly **Disk Cleanup**, current drivers from your maker, and the guidance in Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for File Explorer options.

## Closing

Windows 10 Explorer CPU issues are almost always the classics: a toxic context-menu extension, a corrupt thumbnail cache, or Quick Access chasing dead paths. Restart to confirm the pattern, sweep the extensions with ShellExView, rebuild the caches, and unpin the ghosts — the shell goes quiet again.
