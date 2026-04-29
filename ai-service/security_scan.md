# Security Scan — Week 2 Day 7

Tool Used: OWASP ZAP

Findings:
- No High severity vulnerabilities found
- Missing security headers were detected

Fixes Applied:
- Added Content-Security-Policy header
- Added X-Frame-Options header
- Added X-Content-Type-Options header
- Removed server version exposure

Conclusion:
Application is secure with no critical vulnerabilities after fixes.