---
title: "How to Fix Click to Do Crashing File Explorer on Windows 11"
slug: click-to-do-crashes-file-explorer
date: 2026-10-21
categories: ["ai-pc"]
tags: ["click to do crashing", "file explorer crash", "explorer.exe", "copilot+ pc", "windows 11", "shell extension"]
description: "Fix Click to Do crashing File Explorer on your AI PC with six step-by-step methods covering shell extensions, context menus, NPU drivers, and system repair."
thumbnail: "/images/thumbs/click-to-do-crashes-file-explorer.webp"
faqs:
  - q: "Why does File Explorer crash when I use Click to Do?"
    a: "Click to Do integrates with Explorer through shell and context-menu handlers. If a handler is corrupt, conflicts with a third-party shell extension, or the AI runtime fails, Explorer restarts instead of showing the menu."
  - q: "Is it safe that Explorer keeps restarting?"
    a: "It is annoying but not dangerous — Windows automatically restarts explorer.exe and your files are safe. But repeated crashes can interrupt file operations, so fix the underlying conflict."
  - q: "Can a third-party context menu tool cause this?"
    a: "Yes, very commonly. Tools that customize the right-click menu install shell extensions that load into every Explorer process. When Click to Do's handler and a third-party extension disagree, Explorer crashes."
  - q: "Will disabling Click to Do stop the Explorer crashes?"
    a: "Usually yes, which is a useful diagnostic step — but it is a workaround, not a fix. The guide below shows how to keep Click to Do and stop the crashes by isolating the conflicting component."
---

You right-click a file or invoke Click to Do inside a folder window, and File Explorer vanishes — taskbar, desktop icons, everything — then flickers back seconds later. When the crash lines up exactly with using Click to Do, the feature's Explorer integration is the trigger, even though Explorer itself takes the fall.

Click to Do reaches into File Explorer through shell extensions and context-menu handlers — small pieces of code that load inside the Explorer process. That in-process design means any fault in the handler, or any conflict with another extension, takes the whole Explorer window down with it.

This guide walks through six fixes in order: confirming Click to Do is the trigger, disabling conflicting shell extensions, repairing the AI runtime, updating drivers, and rebuilding Explorer's configuration.

## Why this happens

- **Conflicting third-party shell extension:** Context-menu customizers, cloud-storage overlays, and archive tools inject handlers into Explorer. When Click to Do's handler initializes alongside a buggy one, the process crashes — the most common cause.
- **Corrupt Click to Do shell handler registration:** If the handler's registry registration is damaged after a failed update or registry cleaner, Explorer crashes loading a handler that points nowhere.
- **AI runtime failure under the hood:** Click to Do leans on the on-device AI stack. If that stack fails to engage the hardware — the same class of problem as [DirectML not using the NPU](/articles/directml-not-using-npu-windows-11/) — the handler can fault instead of failing gracefully.
- **NPU or graphics driver crash:** The handler touches the NPU and the GPU composition path. An unstable driver can fault when the AI overlay initializes inside Explorer.
- **Corrupt thumbnail or preview cache:** A poisoned thumbnail cache entry for a specific file type can crash Explorer the moment Click to Do queries the selection.
- **BitLocker or encryption filter interference:** On encrypted drives, filter drivers sit between Explorer and the disk. If [BitLocker has issues on your Snapdragon laptop](/articles/bitlocker-issues-snapdragon-laptop/), the added filter complexity can destabilize shell handlers — and a [missing Studio Effects mic](/articles/studio-effects-mic-not-detected/) alongside points at the same shaky driver stack.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Click to Do is the trigger and disable it temporarily

First prove the correlation. If Explorer is stable with Click to Do off and crashes with it on, you have isolated the trigger. This is diagnostic — you will re-enable it after the real fix.

1. Open **Settings > Privacy & security > Click to Do** and turn the feature off.
2. Use File Explorer normally for 15 minutes: right-click files, open folders, preview documents.
3. If no crashes occur, turn Click to Do back on and invoke it (**Win + Q**) inside a folder window.
4. If the crash returns immediately, Click to Do's Explorer integration is confirmed as the trigger.
5. Leave it on for now — the next fixes remove the conflict instead of the feature.

### Fix 2: Disable third-party shell extensions with ShellExView

Third-party context-menu and overlay extensions are the top suspect. NirSoft's free ShellExView lists every shell extension and lets you disable them safely without uninstalling anything.

1. Download **ShellExView** (free, portable) and run it as administrator.
2. Sort by **Type** and focus on **Context Menu** handlers from non-Microsoft companies (pink background = third party).
3. Select all non-Microsoft context-menu extensions, right-click, and choose **Disable Selected Items**.
4. Restart Explorer from ShellExView (**Options > Restart Explorer**) and test Click to Do in a folder.
5. If crashes stop, re-enable extensions in small batches until the crash returns — then leave that one disabled or update it.

### Fix 3: Clear the thumbnail and icon caches

A corrupt thumbnail cache can crash Explorer when it renders the area around your Click to Do invocation. Clearing the caches forces a rebuild — quick, safe, and effective when crashes happen on specific folders or file types.

1. Open **Disk Cleanup**, select your system drive, check **Thumbnails**, and click OK.
2. For a deeper clear: `taskkill /f /im explorer.exe`, then delete `%localappdata%\Microsoft\Windows\Explorer\thumbcache_*.db`, then `start explorer.exe` in Command Prompt.
3. Delete `iconcache_*.db` in the same folder with Explorer closed.
4. Reopen the folder that crashed, let thumbnails regenerate, and invoke Click to Do.
5. If crashes were tied to one file type, reinstall that file type's preview handler afterward.

### Fix 4: Repair the AI runtime and re-register the Click to Do handler

If no third-party extension is at fault, the Click to Do handler itself or the AI runtime beneath it is damaged. Start with Windows Update, since Click to Do ships as a system component.

1. Go to **Settings > Windows Update**, install all pending updates, and restart.
2. In an elevated PowerShell, try re-registering the app package: `Get-AppxPackage -AllUsers | Where-Object {$_.Name -like "*ClickToDo*"} | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`.
3. If the command finds nothing, the handler is part of the core OS — run `sfc /scannow` then `DISM /Online /Cleanup-Image /RestoreHealth` instead.
4. Restart and test Click to Do in File Explorer with third-party extensions still disabled.
5. Re-enable your shell extensions afterward and confirm the crash does not return.

### Fix 5: Update NPU and graphics drivers

The Click to Do overlay inside Explorer exercises the NPU and the GPU composition path together. A driver that is stable in normal use can still fault when the AI overlay initializes — especially after Windows Update replaced your OEM driver with a generic one.

1. Download the latest NPU/chipset and graphics drivers for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. Install as administrator, restarting when prompted between the two packages.
3. In Device Manager, confirm neither the NPU nor the display adapter shows a warning icon.
4. Test Click to Do in Explorer immediately after the restart.
5. If crashes persist only with a specific driver version, roll back in Device Manager.

### Fix 6: Reset File Explorer's configuration to defaults

When everything else checks out, Explorer's own saved configuration — folder views, Quick Access database, navigation pane state — can harbor the corruption. Resetting it clears per-folder baggage without touching your files.

1. Open **Folder Options**; on the **General** and **View** tabs, click **Restore Defaults**.
2. In the same dialog, click **Clear** next to "Clear File Explorer history."
3. Delete the `*.automaticDestinations-ms` files in `%APPDATA%\Microsoft\Windows\Recent\AutomaticDestinations` (resets jump lists).
4. Restart Explorer via Task Manager (right-click **Windows Explorer > Restart**).
5. Re-enable Click to Do fully and test across several folders.

## Closing

Click to Do crashing File Explorer looks like an Explorer problem but is almost always a handler conflict: a third-party shell extension, a corrupt registration, or a driver that faults when the AI overlay loads. Isolate with ShellExView, clear the caches, and update the drivers — in that order.
