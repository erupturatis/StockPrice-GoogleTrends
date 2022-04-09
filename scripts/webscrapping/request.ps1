function GetRequest($search_param) {
    
    $session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
    $session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
    Invoke-WebRequest -UseBasicParsing -Uri "https://api.nasdaq.com/api/autocomplete/slookup/10?search=$search_param" `
    -WebSession $session `
    -Headers @{
    "method"="GET"
    "authority"="api.nasdaq.com"
    "scheme"="https"
    "path"="/api/autocomplete/slookup/10?search=tesla"
    "sec-ch-ua"="`" Not A;Brand`";v=`"99`", `"Chromium`";v=`"99`", `"Google Chrome`";v=`"99`""
    "accept"="application/json, text/plain, */*"
    "sec-ch-ua-mobile"="?0"
    "sec-ch-ua-platform"="`"Windows`""
    "origin"="https://www.nasdaq.com"
    "sec-fetch-site"="same-site"
    "sec-fetch-mode"="cors"
    "sec-fetch-dest"="empty"
    "referer"="https://www.nasdaq.com/"
    "accept-encoding"="gzip, deflate, br"
    "accept-language"="en-US,en;q=0.9"
    }

}

function Test {
   
    $name = "John"
    Write-Output "He is good $name"
    return $name
}

$res = GetRequest($args[0])
$var = $res.Content
return $var

