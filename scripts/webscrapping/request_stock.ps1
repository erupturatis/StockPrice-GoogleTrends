function get2($symbol, $start) {
    Write-Output $symbol
    
    $session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
    $session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    Invoke-WebRequest -UseBasicParsing -Uri "https://api.nasdaq.com/api/quote/$symbol/chart?assetclass=stocks&fromdate=2021-10-09&todate=2022-04-09" `
    -WebSession $session `
    -Headers @{
    "authority"="api.nasdaq.com"
    "method"="GET"
    "path"="/api/quote/$symbol/chart?assetclass=stocks&fromdate=2021-10-09&todate=2022-04-09"
    "scheme"="https"
    "accept"="application/json, text/plain, */*"
    "accept-encoding"="gzip, deflate, br"
    "accept-language"="en-US,en;q=0.9"
    "origin"="https://www.nasdaq.com"
    "referer"="https://www.nasdaq.com/"
    "sec-ch-ua"="`" Not A;Brand`";v=`"99`", `"Chromium`";v=`"100`", `"Google Chrome`";v=`"100`""
    "sec-ch-ua-mobile"="?0"
    "sec-ch-ua-platform"="`"Windows`""
    "sec-fetch-dest"="empty"
    "sec-fetch-mode"="cors"
    "sec-fetch-site"="same-site"
    } 
}
 

get2($args[0], $args[1])
#$res = GetRequest($symbol,$start_date,$end_date)

#$var = $res.Content
#return $var

