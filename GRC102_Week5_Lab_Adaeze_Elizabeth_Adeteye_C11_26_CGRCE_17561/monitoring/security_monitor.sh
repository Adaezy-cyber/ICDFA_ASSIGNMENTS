#!/bin/bash
# Security Monitoring Script - polls for suspicious activity every 5 minutes via cron

grep -i "Content-Type.*multipart/form-data" /var/log/nginx/access.log > /tmp/suspicious_requests.log 2>/dev/null

mysql -u root -ppassword -e "SHOW PROCESSLIST" > /tmp/database_access.log 2>/dev/null

find /var/www -type f -mtime -1 > /tmp/recent_file_changes.log 2>/dev/null

if [ -s /tmp/suspicious_requests.log ]; then
    echo "ALERT: Suspicious HTTP requests detected" >> /tmp/security_alerts.log
fi

if grep -q "customer_data" /tmp/database_access.log 2>/dev/null; then
    echo "ALERT: Access to customer_data database detected" >> /tmp/security_alerts.log
fi

if [ -s /tmp/recent_file_changes.log ]; then
    echo "ALERT: Recent file changes detected" >> /tmp/security_alerts.log
fi
