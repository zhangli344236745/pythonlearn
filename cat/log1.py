# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/3/22
import logging
import logging.config

logging.config.fileConfig("log.ini")

logger = logging.getLogger("root")

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')