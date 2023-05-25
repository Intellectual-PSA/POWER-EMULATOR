# Set up the performance counter to monitor power usage for all processes
$counter = "\Process(*)\Power Usage"
$interval = 1
$counterHandle = New-Object System.Diagnostics.PerformanceCounter($counter)

# Loop continuously and check if the power usage surges
while ($true) {
    $powerUsage = $counterHandle.NextValue()
    if (2 -le $powerUsage -and $powerUsage -le 3) {
        $message = "Power usage has surged to $powerUsage watts!"
        [System.Windows.Forms.MessageBox]::Show($message, "Power Surge", [System.Windows.Forms.MessageBoxButtons]::OK, [System.Windows.Forms.MessageBoxIcon]::Warning)
    }
    Start-Sleep -Seconds $interval
}
