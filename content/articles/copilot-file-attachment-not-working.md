---
title: "How to Fix Copilot File Attachment Not Working on Your Windows 11 AI PC"
slug: copilot-file-attachment-not-working
date: 2026-10-21
categories: ["ai-pc"]
tags: ["copilot file attachment", "copilot app", "file upload not working", "windows 11", "ai pc", "troubleshooting"]
description: "Fix Copilot's file attachment problems on your AI PC laptop with six step-by-step methods covering file limits, app updates, permissions, and network issues."
thumbnail: "/images/thumbs/copilot-file-attachment-not-working.webp"
faqs:
  - q: "Why is the attach button greyed out in Copilot?"
    a: >
      A greyed-out attach icon almost always means one of three things: the file type
      is not supported, you are signed in with a work or school account whose admin
      disabled uploads, or the Copilot app is too old to expose the feature. Check the
      file type and size first, then update the app — those two cover most cases.
  - q: "What file types can Copilot open?"
    a: >
      It depends on the surface. Copilot on the web handles PDFs, Word and text
      documents, code files, and common image formats. The Windows Copilot app supports
      a narrower set and changes with updates. If one surface rejects a file, try
      uploading it on the web version before assuming the file itself is the problem.
  - q: "Can I attach files with a work or school account?"
    a: >
      Sometimes not. Microsoft 365 administrators can disable file uploads to Copilot
      through tenant policy, and there is no user-side override. If attachments work
      on your personal account but not your work account on the same laptop, your
      organization's policy is the cause — your IT admin has to allow it.
  - q: "Are my attached files uploaded to Microsoft's servers?"
    a: >
      Yes. When you attach a file, a copy is sent to the cloud for processing — the
      analysis does not happen locally on your NPU. Avoid uploading sensitive
      documents, and review your privacy settings in your Microsoft account if you
      want to limit how that data is used.
---

You tap the paperclip icon in the Copilot app, pick a PDF, and... nothing. No preview, no progress bar, no error message — the file just refuses to attach. On an AI PC laptop this stings more than it should, because Copilot is supposed to be the centerpiece: summarizing long contracts, explaining dense spreadsheets, and reviewing documents should all be one drag-and-drop away.

This breaks every file workflow Copilot offers. PDF summaries, Word document Q&A, image analysis, and code review from uploaded files all stop at the same wall. The chat itself usually keeps working fine, which makes the failure feel random — but it is not. Attachments fail for a small set of specific reasons, and each one has a fix.

This guide walks you through six fixes in technician order: quick checks on the file and your account first, then app repair, permissions, network, sign-in state, and finally fallback surfaces that get you working today. Work through them in sequence and test an upload after each step.

## Why this happens

- **Unsupported file type or size**: Copilot accepts a defined set of formats, and oversized files fail silently. A 200 MB scanned PDF or an unusual archive format will simply never attach.
- **Outdated Copilot app**: The attach feature depends on current app builds. Older versions can show the paperclip icon while the upload call behind it fails every time.
- **Work or school account policy**: Tenant administrators can disable file uploads. On a managed device, attachments may be blocked by policy even though personal chat works.
- **Broken file-picker bridge on Arm**: On Snapdragon X AI PCs, the picker dialog that hands files to the app can glitch after updates — the same class of compatibility gap that leaves [anti-cheat drivers unsupported on Arm laptops](/articles/anti-cheat-unsupported-arm-laptop/).
- **Network or proxy blocking uploads**: VPNs, corporate proxies, and metered connections can block the upload endpoint while plain chat text still flows normally.
- **Corrupt app cache or stale sign-in token**: A damaged cache or expired auth token makes the server reject the upload without any visible error on your screen.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the file type, size, and which account you are using

Before touching the app, rule out the two most common causes. Copilot rejects files it cannot parse, and managed accounts can have uploads disabled entirely — both look identical to a broken app.

1. Try a small, simple file first: a one-page PDF or a plain .txt under 5 MB. If that attaches, your original file was the problem.
2. Rename the file to remove special characters and confirm the extension matches a supported format (PDF, DOCX, TXT, common images).
3. Check which account is signed in — tap your profile picture in Copilot. If it is a work or school account, test with a personal Microsoft account.
4. If the personal account works and the work account does not, stop here: your organization's policy blocks uploads, and only your IT admin can change it.

### Fix 2: Update or repair the Copilot app

An outdated or damaged Copilot package is the most common real failure on personal accounts. The Microsoft Store build changes fast, and a stuck update leaves the upload pipeline half-broken. If the Store itself is misbehaving, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) has the official Store repair steps.

1. Open the **Microsoft Store**, go to **Library**, and install all pending updates — Copilot included.
2. If it is already current, go to **Settings > Apps > Installed apps**, find **Microsoft Copilot**, and use **Advanced options > Repair**.
3. Test an upload. If it still fails, return to Advanced options and use **Reset** — you will need to sign in again.
4. After a reset, attach the small test file from Fix 1 before retrying your real document.

### Fix 3: Re-grant file system and storage permissions

Windows 11 can revoke an app's access to your files after major updates, and Copilot then fails to read the file you picked. The picker opens, you choose a file, and the app silently gets nothing.

1. Go to **Settings > Privacy & security > File system** and confirm **Microsoft Copilot** is allowed.
2. Also check **Settings > Apps > Installed apps > Microsoft Copilot > Advanced options** and verify all listed permissions are on.
3. Sign out of Copilot, close it fully from the system tray, and reopen it so the new permissions take effect.
4. Try the upload again with the test file.

### Fix 4: Test uploads off VPN and on a clean network

Uploads travel to a different endpoint than chat text, so your network can break one while the other works. This is especially common on corporate networks and VPNs with strict egress rules.

1. Disconnect your VPN completely and try the upload on your normal connection.
2. If it works off-VPN, the VPN's egress policy is blocking the upload endpoint — ask your network admin or use split tunneling for Copilot.
3. On a work network, also try a mobile hotspot for one test to confirm the office proxy is the blocker.
4. Turn off any third-party firewall's "web shield" temporarily and retest; re-enable it right after.

### Fix 5: Sign out, clear the cache, and sign back in

A stale authentication token is the classic invisible cause: chat keeps working on a cached session while the server rejects your uploads. If every AI feature is misbehaving at once rather than just attachments, compare with the [NPU not showing in dxdiag](/articles/npu-not-showing-in-dxdiag/) guide — but for attachments-only failures, this fix is the one.

1. In the Copilot app, open your profile and choose **Sign out**.
2. Close Copilot fully, then go to **Settings > System > Storage > Temporary files** and clear app caches.
3. Reopen Copilot and sign back in with the account you want to use.
4. Attach the test file before opening any long conversation — a fresh session rules out conversation-state bugs too.

### Fix 6: Use Copilot on the web or reinstall the app

If the Windows app still refuses uploads, the web surface often works — it uses a different upload path. This also tells you definitively whether the problem is the app or your account.

1. Go to copilot.microsoft.com in Edge, sign in with the same account, and try the upload there.
2. If the web version works, uninstall the Windows Copilot app, restart, and reinstall it fresh from the Microsoft Store.
3. If the web version fails identically, the issue is your account or network — revisit Fix 1 and Fix 4.
4. If [Copilot is not responding at all](/articles/copilot-not-responding/), treat it as a session or account problem rather than an attachment bug, and work that guide next.

## Closing

File attachments fail for boring reasons far more often than mysterious ones: a file Copilot cannot parse, an account policy you cannot see, an app build that is one update behind, or a token that quietly expired. Work the list in order and you will find your culprit quickly — and keep the web version bookmarked, because it is the fastest fallback whenever the Windows app acts up. If Copilot also stumbles on [AI image generation](/articles/copilot-image-generation-not-working/), the underlying cause is usually the same account or app-state problem.
