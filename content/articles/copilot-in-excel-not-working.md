---
title: "How to Fix Copilot Not Working in Excel on Your Laptop"
slug: copilot-in-excel-not-working
date: 2026-10-23
categories: ["ai-pc"]
tags: ["copilot", "microsoft excel", "windows 11", "microsoft 365", "troubleshooting"]
description: "Copilot not working in Excel on your laptop? Fix sign-in, AutoSave, OneDrive file location, updates, connected experiences, and Office repair step by step."
thumbnail: "/images/thumbs/copilot-in-excel-not-working.webp"
faqs:
  - q: "Why is Copilot missing from Excel but works in Word?"
    a: >
      Excel has extra requirements Word does not: the workbook must be saved to OneDrive or SharePoint with AutoSave turned on. A locally saved file hides Copilot in Excel even when your license is fine and Word works.
  - q: "Does Copilot in Excel need a special file format?"
    a: >
      Yes. Copilot in Excel works with modern .xlsx workbooks stored in the cloud. Older .xls files, and workbooks with certain legacy features, are not supported and will not show the Copilot button.
  - q: "Why does Copilot in Excel say my data isn't supported?"
    a: >
      Copilot works best with data formatted as an Excel Table. Unstructured ranges, merged cells, or sheets with heavy macros can trigger the unsupported-data message. Convert your range to a Table with Ctrl+T.
  - q: "Is an internet connection required for Copilot in Excel?"
    a: >
      Yes. Every Copilot request goes to Microsoft's cloud service, and the workbook itself must live on OneDrive or SharePoint. Offline files and offline PCs cannot use Copilot in Excel at all.
---

You open a spreadsheet, ready to let Copilot analyze the numbers, and the Copilot button is nowhere in the Excel ribbon — or it is there but refuses to touch your data. Stranger still, Copilot works fine in your Word on the same laptop. The inconsistency makes it feel random, but Excel's Copilot has its own private set of rules.

Copilot in Excel is pickier than its Word sibling. Beyond the usual license, sign-in, and update requirements, Excel demands that your workbook live on OneDrive or SharePoint with AutoSave enabled, in the modern .xlsx format. A spreadsheet saved to your local drive — the default habit for years — silently disqualifies itself, and Excel never explains why the button vanished.

This guide gives you six fixes in technician order: license and sign-in first, then the file-location rules Excel enforces, then updates and connected experiences, and finally add-in conflicts and Office repair. Work through them in sequence and check the ribbon after each step.

## Why this happens

- **Workbook saved locally instead of the cloud:** Copilot in Excel only works on files stored in OneDrive or SharePoint with AutoSave on. A local file hides the button completely — the most common Excel-specific cause.
- **No Copilot license on the signed-in account:** Like Word, Excel needs Microsoft 365 plus a Copilot license. The wrong signed-in account, or an expired subscription, removes Copilot silently.
- **Legacy file format or unsupported data layout:** Old .xls files, and sheets full of merged cells or unstructured ranges, are not supported. Copilot needs a modern .xlsx workbook, ideally with data in Tables.
- **Outdated Excel build:** Copilot features ship in current Microsoft 365 builds of Excel. Deferred update channels and old installs lack the integration.
- **Connected experiences disabled:** Excel's privacy toggle for connected experiences gates the cloud AI. If it is off, Copilot cannot reach the service.
- **Conflicting COM add-ins:** Third-party Excel add-ins — especially data connectors and analysis packs — can intercept or break Copilot's cloud calls.
- **Offline or blocked network:** Copilot processes in Microsoft's cloud. No internet, or a firewall blocking Microsoft 365 endpoints, kills every prompt.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the license and the signed-in account

Before blaming Excel's quirks, rule out the universal gates: Copilot needs a Microsoft 365 subscription with a Copilot license, held by the account actually signed in to Excel. License drift between apps is common on laptops used for both work and personal tasks.

1. In Excel, click your profile picture in the top-right and note the signed-in account.
2. Verify at account.microsoft.com that this exact account holds an active Microsoft 365 subscription with Copilot included.
3. If the accounts differ, sign out inside Excel and sign back in with the licensed account.
4. Close Excel completely and reopen it so the ribbon re-evaluates the license.
5. If Copilot appears in Word but not Excel under the same account, the license is fine — the problem is Excel-specific, and the next fix is almost certainly the answer. Mixed-identity machines also trip up tooling, as with [Java JDK installs on ARM Windows](/articles/java-jdk-arm-windows-install/).

### Fix 2: Move the workbook to OneDrive and turn on AutoSave

This is the fix for most "Copilot works in Word but not Excel" cases. Excel's Copilot refuses local files — the workbook must live on OneDrive or SharePoint with AutoSave enabled, because Copilot analyzes the cloud-saved version of your data.

1. In Excel, check the top-left of the window: if AutoSave is off or the title bar shows a local path like C:\Users, the file is disqualified.
2. Go to **File > Save As** and save a copy to **OneDrive** (personal or work, matching your licensed account).
3. Toggle **AutoSave** on in the top-left corner — the switch must stay on, not just be enabled once.
4. Wait for the save to sync (the cloud icon should show synced, not pending), then look for the Copilot button in the **Home** tab.
5. Make it a habit: any workbook Copilot should analyze must go through this OneDrive + AutoSave path first — local files are invisible to Copilot by design.

### Fix 3: Convert to .xlsx and format data as a Table

Even a cloud-saved workbook can stump Copilot if it is in a legacy format or the data is unstructured. Copilot reads Excel Tables — plain ranges with merged cells and scattered headers trigger "data not supported" or a missing button.

1. Check the file extension: if it is .xls, go to **File > Save As** and save as **Excel Workbook (*.xlsx)**.
2. Select your data range and press **Ctrl + T** to convert it to an official Excel Table, confirming "My table has headers" if appropriate.
3. Remove merged cells in the data area — Copilot cannot parse them; unmerge and fill values down.
4. Keep the sheet free of heavy macros aimed at the data range while testing; you can re-add complexity later.
5. With the file saved to OneDrive, AutoSave on, and data in a Table, reopen the workbook and check for Copilot. A clean, structured sheet is what the AI was built to read. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) cover the current file requirements for Copilot in Excel.

### Fix 4: Update Excel and enable connected experiences

An outdated Excel build may predate Copilot entirely, and disabled connected experiences block the cloud calls even on a current build. Both live in places users rarely visit, so check them deliberately.

1. In Excel, go to **File > Account > Update Options > Update Now** and install all available updates.
2. Confirm you are on a current Microsoft 365 Click-to-Run build via **File > Account > About Excel**.
3. Then go to **File > Account > Manage Settings** and make sure **Enable connected experiences** is turned on.
4. Close Excel fully, reopen your OneDrive-saved workbook, and test Copilot with a simple prompt like "Summarize this table."
5. On a work laptop, connected experiences may be locked off by admin policy — a grayed-out toggle means IT must allow it, and no local step overrides that.

### Fix 5: Disable conflicting add-ins

Excel power users accumulate COM add-ins — data connectors, analysis toolbars, automation helpers — and some intercept the same cloud pathways Copilot uses. When Copilot dies only in Excel while Word is fine, a rogue add-in is the prime suspect.

1. In Excel, go to **File > Options > Add-ins**.
2. Set the **Manage** dropdown to **COM Add-ins**, click **Go**, and uncheck every third-party add-in.
3. Restart Excel, open your OneDrive workbook, and test Copilot.
4. If Copilot works, re-enable add-ins one at a time, testing after each, until you find the one that breaks it.
5. Leave the culprit disabled or check its maker for an update. Add-in conflicts are the Excel equivalent of background processes skewing diagnostics — the same class of interference that makes [Recall snapshot encryption behave oddly](/articles/recall-snapshot-encryption-issues/) when other software hooks the same system paths.

### Fix 6: Repair the Office installation

When license, file location, format, updates, settings, and add-ins are all correct, the Office install itself is damaged — a broken Click-to-Run component can disable Copilot in one app while the others work. An Online Repair reinstalls Office without touching your documents.

1. Open **Settings > Apps > Installed apps**, find **Microsoft 365**, click the three dots, and choose **Modify**.
2. Select **Online Repair** and let it run (15–30 minutes on a decent connection).
3. Restart the laptop when the repair completes — a full reboot matters here, not just closing apps.
4. Open Excel, sign in with your licensed account, re-save a test workbook to OneDrive with AutoSave on, and check for Copilot.
5. If the button is still missing after a repair, uninstall Office completely and reinstall from your Microsoft account portal. If Excel misbehaves alongside sleep issues, check the [modern standby battery drain guide](/articles/modern-standby-battery-drain-ai-pc/) for the same class of firmware-level gremlins.

## Closing

Copilot in Excel fails for Excel-specific reasons more often than general ones: the number-one cause is a locally saved file, followed by unstructured data, then the usual license, update, and connected-experiences gates. Move the workbook to OneDrive with AutoSave on, format the data as a Table, and the button comes back.
