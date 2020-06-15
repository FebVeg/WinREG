#$Reg = Read-Host "Enter Parent Key Name"
#Get-ChildItem -Path HKCU:\ -Recurse -Include "*$reg*" | Select-Object Name # Restituisce solo il percorso della chiave
# just for testing.. 
# this script can clean the registry after have uninstalled program

$KeyName = Read-Host "Enter Sub Key Name: "
# Searching all SubKeys
for (($i = 1); $i -lt 10; $i++)
{
    $var = "\*"*$i
    Get-ItemProperty -Path HKCU:$var -Name "$KeyName" -ErrorAction SilentlyContinue
    Write-Host "Cerco sotto HKCU:$var la sottochiave $KeyName"
}
Write-Host "Done for $KeyName"

# Removing all subkeys...
for (($i = 1); $i -lt 10; $i++)
{
    $var = "\*"*$i
    Remove-ItemProperty -Path HKCU:$var -Name "*$KeyName*" -ErrorAction SilentlyContinue
    Write-Host "Cerco sotto HKCU:$var"
}
Write-Host "All key of $KeyName are cleaned"
