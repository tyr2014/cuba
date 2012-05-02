#!/bin/bash
## kill all celeryd instances found. supervisord will restart it.
ps aux | grep celery | grep feed_tasks | awk '{print $2}' | sudo xargs -n 1 kill -9
