---
title: "How to Fix Click to Do Missing in the File Explorer Preview Pane"
slug: click-to-do-file-explorer-preview-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["click to do", "file explorer", "preview pane", "copilot+ pc", "windows 11", "troubleshooting"]
description: "Fix Click to Do not appearing in the File Explorer preview pane on your Copilot+ PC with settings, NPU, and file-type checks that restore it quickly today."
thumbnail: "/images/thumbs/click-to-do-file-explorer-preview-fix.webp"
faqs:
  - q: "Why does Click to Do work in screenshots but not in File Explorer?"
    a: "File Explorer uses a separate preview-pane integration that depends on the file type, the preview handler, and the Copilot+ runtime. A screenshot passes through a different Click to Do path, so one can work while the other stays silent."
  - q: "Which files support Click to Do in the preview pane?"
    a: "Images such as JPG and PNG are the most reliable. PDFs, text files, and some Office documents may show a preview without Click to Do actions, depending on the installed preview handler and app."
  - q: "Does Click to Do in File Explorer need an internet connection?"
    a: "No, the on-device actions run locally on the NPU, but Windows may still check for updates and language components. A missing or outdated component can block the preview-pane actions even offline."
  - q: "Will reinstalling File Explorer fix Click to Do?"
    a: "File Explorer cannot be reinstalled separately. Instead, repair the Click to Do feature, reset the preview pane, and update the Copilot+ components — those steps fix the integration without touching your files."
---

The pane shows the image, yet the small Click to Do icon never lights up, and right-clicking the preview offers no AI actions at all.

On Copilot+ PCs, Click to Do in File Explorer is not the same feature as Click to Do on a screenshot. The preview pane has its own integration: Windows must recognise the file type, load the right preview handler, and hand the image to the on-device AI runtime. If any link in that chain is missing, the preview still renders while the AI actions stay hidden.

This guide walks you through the checks in technician order, from the preview-pane setting itself to the Copilot+ components underneath it. Work through the fixes in sequence, and test with the same JPG or PNG file after each step so you can tell exactly which change restored it.

## Why this happens

- **Preview pane turned off or too narrow:** Click to Do actions only appear when the preview pane is actually open and wide enough to render its toolbar. A collapsed pane shows the image but hides the controls.
- **Unsupported file type or preview handler:** Click to Do needs an image preview it can analyse. A file opened through a third-party preview handler, or a format such as WebP or HEIC without the right codec, may preview without AI actions.
- **Click to Do feature disabled:** The feature can be switched off in Settings, by a group policy, or after a Windows update resets it. When it is off, no surface — including File Explorer — shows actions.
- **Outdated Copilot+ or NPU components:** The preview-pane actions depend on the Windows AI runtime and NPU drivers. A stale driver or a failed component update leaves the feature installed but non-functional.
- **File selected from a cloud or network location:** Files that are online-only in OneDrive, or stored on a network drive, may preview as a placeholder. Click to Do cannot analyse a file that has not fully downloaded.
- **Corrupt thumbnail or preview cache:** A damaged preview cache can make File Explorer render a stale preview that never triggers the AI pipeline, even though the file itself is perfectly fine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn on the preview pane and give it room

Before blaming drivers, confirm the pane itself is open and usable. This is the most common cause, and it takes less than a minute to rule out — especially after a window resize or a new File Explorer layout reset the view.

1. Open File Explorer and press **Alt + P** to toggle the preview pane on.
2. Select a JPG or PNG photo that you know works elsewhere on the PC.
3. Drag the pane divider leftwards so the preview is at least a third of the window width.
4. Look for the Click to Do icon or prompt inside the preview area, not just in the toolbar.
5. If the icon appears now, the feature was fine all along — the pane was simply too narrow or closed.

### Fix 2: Confirm Click to Do is enabled in Settings

One toggle controls Click to Do across Windows. If it was switched off by an update or a policy, File Explorer will never show the actions, no matter how healthy the system is.

1. Open **Settings > Privacy & security > Click to Do** (on some builds, look under **Bluetooth & devices** or search for "Click to Do").
2. Make sure the main **Click to Do** switch is turned **On**.
3. Check any sub-options for image actions and make sure they are not individually disabled.
4. Restart File Explorer by opening Task Manager, right-clicking **Windows Explorer**, and choosing **Restart**.
5. Select your test photo again and check the preview pane for the Click to Do prompt.

### Fix 3: Test a local JPG and rule out cloud placeholders

Online-only files are a quiet trap. File Explorer can show a preview of a cloud file without downloading the full image, and Click to Do has nothing to analyse until the real file lands on disk.

1. Copy your test photo to the local **Pictures** folder so it is definitely stored on the PC.
2. In File Explorer, right-click the original cloud file and choose **Always keep on this device** if it shows a cloud icon.
3. Wait for the download to finish, then select the local copy instead.
4. Check whether Click to Do now appears in the preview pane for the local file.
5. If it does, your issue was the file location, not the feature — keep working copies local when you need AI actions. The same local-versus-cloud distinction trips up other AI features too, as seen with [live captions in Chrome](/articles/live-captions-not-working-in-chrome-fix/), where the source stream matters as much as the setting.

### Fix 4: Reset the preview pane and clear the thumbnail cache

A stale preview cache can freeze File Explorer into showing an old, action-free preview. Clearing it forces Windows to rebuild the preview and re-run the Click to Do pipeline from scratch.

1. Open **Settings > System > Storage > Temporary files** and tick **Thumbnails**, then click **Remove files**.
2. Alternatively, open Disk Cleanup, select your system drive, tick **Thumbnails**, and confirm.
3. In File Explorer, go to **View > Show** and toggle the preview pane off and back on.
4. Select a different photo first, then return to your test photo so the preview rebuilds fresh.
5. Check for the Click to Do icon — a rebuilt preview often restores actions that a cached one suppressed.

### Fix 5: Update Windows and the NPU driver

Click to Do in the preview pane depends on the Copilot+ runtime, which ships through Windows Update and your laptop maker's NPU driver. A mismatch between the two can leave the feature visible in Settings but dead in File Explorer.

1. Open **Settings > Windows Update** and install every pending update, then restart.
2. Open **Device Manager > Neural processors** and check for warning icons on the NPU entry.
3. Download the latest NPU and chipset drivers from your maker's support page — [Dell](https://www.dell.com/support) or [Lenovo](https://support.lenovo.com/us/en/) — rather than relying on a generic driver.
4. Install the driver, restart, and select your test photo again in File Explorer.
5. If Windows Update offers a newer Click to Do component afterwards, install it and retest before moving on. Similar component mismatches also break other Copilot+ tools, which is why [Click to Do in Snipping Tool](/articles/click-to-do-snipping-tool-not-working/) follows the same update-first logic.

### Fix 6: Repair the Click to Do component and check for conflicts

When settings, files, and drivers are all correct, the Click to Do package itself may be damaged. Repairing it through Windows' built-in tools, and removing a conflicting preview handler, is the last local step before a broader reset.

1. Open **Settings > System > Optional features** or **Apps > Installed apps** and look for Click to Do or AI-related components.
2. If a repair option is offered, run it; otherwise, toggle Click to Do off, restart, and toggle it back on.
3. Think about recently installed preview tools or codec packs — temporarily uninstall any third-party preview handler and retest with the built-in Photos preview.
4. Create a new local user account, sign in, and test File Explorer there to rule out a corrupt user profile.
5. If Click to Do works in the new account, migrate your files there; if it fails everywhere, run System File Checker (`sfc /scannow` in an elevated terminal) and check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for the latest Copilot+ repair guidance. A related on-device AI install issue, [Fooocus on a laptop](/articles/fooocus-ai-laptop-install-fix/), shows how a single broken AI package can block an otherwise healthy feature.

## Closing

Click to Do in the File Explorer preview pane fails quietly because the preview can look normal while the AI layer underneath never starts. Confirm the pane, the toggle, and a local image file first, then update the NPU runtime — in most cases one step brings the actions back without a reset.
