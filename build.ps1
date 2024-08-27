$exclude = @("venv", "loginAutomation.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "loginAutomation.zip" -Force