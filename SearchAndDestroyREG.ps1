$Reg = Read-Host "Enter Parent Key Name"
Get-ChildItem -Path HKCU:\ -Recurse -Include "*$reg*" | Select-Object Name # Restituisce solo il percorso della chiave
# just for testing.. 
# this script can clean the registry after have uninstalled program

$KeyName = Read-Host "Enter Sub Key Name"

# Searching all SubKeys
# searching on HKCU
for (($i = 1); $i -lt 10; $i++)
{
    $var = "\*"*$i
    Write-Host "Searching under HKCU:$var the subkey $KeyName"
    Get-ItemProperty -Path HKCU:$var -Name "*$KeyName*" -ErrorAction SilentlyContinue
}
Write-Host "Finished: HKCU - $KeyName"

# searching on HKLM
for (($i = 1); $i -lt 10; $i++)
{
    $var = "\*"*$i
    Write-Host "Searching under HKLM:$var the subkey $KeyName"
    Get-ItemProperty -Path HKLM:$var -Name "*$KeyName*" -ErrorAction SilentlyContinue
}
Write-Host "Finished: HKLM - $KeyName"

# Removing all subkeys...
<#
for (($i = 1); $i -lt 10; $i++)
{
    $var = "\*"*$i
    Write-Host "Removing under HKCU:$var the subkey $KeyName"
    Remove-ItemProperty -Path HKCU:$var -Name "*$KeyName*" -ErrorAction SilentlyContinue
}
Write-Host "All key of $KeyName are cleaned"
#>
