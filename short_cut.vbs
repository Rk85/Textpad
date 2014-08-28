set WshShell = WScript.CreateObject("WScript.Shell" )
set oShellLink = WshShell.CreateShortcut( Environment.GetFolderPath(Environment.SpecialFolder.Desktop)) & "\Textpad.lnk")
oShellLink.TargetPath = WshShell.GetAbsolutePathName(".") & "\dist\Textpad.exe"
oShellLink.WindowStyle = 1
oShellLink.IconLocation = WshShell.GetAbsolutePathName(".") & "\dist\short_icon.ico"
oShellLink.Save
