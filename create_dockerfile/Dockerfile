From centos

RUN yum install crontabs -y && yum install python36 -y && yum install tc -y 

# Copy cronjob file to the cron.d directory
COPY cronjob /etc/cron.d/cronjob
COPY test_crontab.py /test_crontab.py
COPY crond /etc/pam.d/crond
COPY Shanghai /etc/localtime


RUN chmod +x /test_crontab.py

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cronjob

# Apply cron job
RUN crontab /etc/cron.d/cronjob

