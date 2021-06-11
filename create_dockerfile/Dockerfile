From centos

RUN yum install crontabs -y && yum install python36 -y && yum install tc -y 

COPY cronjob /etc/cron.d/cronjob
COPY test_crontab.py /test_crontab.py
COPY crond /etc/pam.d/crond
COPY Shanghai /etc/localtime


RUN chmod +x /test_crontab.py
RUN chmod 0644 /etc/cron.d/cronjob

RUN crontab /etc/cron.d/cronjob

RUN touch /var/log/cron.log

CMD crond && tail -f /var/log/cron.log
